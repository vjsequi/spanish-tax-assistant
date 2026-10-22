"""Loopback-only synthetic adapter; not the planned production HTTP server."""

from __future__ import annotations

import argparse
import json
import os
import secrets
import subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, cast

from renta_assistant.application.workbench import Workbench
from renta_assistant.domain.calculation import InputError
from renta_assistant.infrastructure.export import pdf_packet
from renta_assistant.infrastructure.repository import ROOT, Sources
from renta_assistant.infrastructure.state import FileStore

ASSETS = Path(__file__).parent / "assets"


def make_server(workbench: Workbench, sources: Sources, port: int = 8020) -> ThreadingHTTPServer:
    token = secrets.token_urlsafe(32)

    class Handler(BaseHTTPRequestHandler):
        def setup(self) -> None:
            super().setup()
            self.connection.settimeout(10)

        def log_message(self, format: str, *args: object) -> None:
            # No document text, request payloads, query strings or financial values in access logs.
            pass

        def send(self, raw: bytes, kind: str, status: int = 200, *, download: str = "") -> None:
            self.send_response(status)
            self.send_header("Content-Type", kind)
            self.send_header("Content-Length", str(len(raw)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Referrer-Policy", "no-referrer")
            self.send_header(
                "Content-Security-Policy",
                "default-src 'self'; frame-ancestors 'none'; object-src 'none'",
            )
            if download:
                self.send_header("Content-Disposition", f'attachment; filename="{download}"')
            self.end_headers()
            self.wfile.write(raw)

        def json(self, data: dict[str, Any], status: int = 200) -> None:
            self.send(
                json.dumps(data, ensure_ascii=False).encode(),
                "application/json; charset=utf-8",
                status,
            )

        def host_allowed(self) -> bool:
            return (
                self.headers.get("Host")
                == f"127.0.0.1:{cast(ThreadingHTTPServer, self.server).server_port}"
            )

        def do_GET(self) -> None:
            if not self.host_allowed():
                self.json({"error": "Host local no permitido."}, 403)
                return
            try:
                if self.path == "/":
                    self.send((ASSETS / "index.html").read_bytes(), "text/html; charset=utf-8")
                elif self.path in {"/assets/app.js", "/assets/app.css"}:
                    name = self.path.rsplit("/", 1)[1]
                    self.send(
                        (ASSETS / name).read_bytes(),
                        "text/javascript" if name.endswith("js") else "text/css",
                    )
                elif self.path == "/api/case":
                    self.json({**workbench.view(), "csrf_token": token})
                elif self.path.startswith("/source/") and self.path.count("/") == 2:
                    self.send(sources.image(self.path.split("/")[-1]), "image/png")
                elif self.path == "/export.json":
                    self.send(
                        json.dumps(workbench.packet(), ensure_ascii=False, indent=2).encode(),
                        "application/json",
                        download="C001-provisional.json",
                    )
                elif self.path == "/export.pdf":
                    self.send(
                        pdf_packet(workbench.packet()),
                        "application/pdf",
                        download="C001-provisional.pdf",
                    )
                else:
                    self.json({"error": "Ruta no disponible."}, 404)
            except InputError as exc:
                self.json({"error": str(exc)}, 422)
            except ValueError, OSError, subprocess.SubprocessError:
                self.json(
                    {"error": "La operación local no se completó. Revise las fuentes o el estado."},
                    500,
                )

        def do_POST(self) -> None:
            expected_origin = (
                f"http://127.0.0.1:{cast(ThreadingHTTPServer, self.server).server_port}"
            )
            if (
                not self.host_allowed()
                or self.path != "/api/calculate"
                or self.headers.get("Origin") != expected_origin
                or not secrets.compare_digest(self.headers.get("X-CSRF-Token", ""), token)
            ):
                self.json({"error": "Petición fuera de la sesión local permitida."}, 403)
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if (
                    not 0 < length <= 32768
                    or self.headers.get("Content-Type") != "application/json"
                ):
                    raise InputError("Tamaño o tipo de petición no permitido.")
                data = json.loads(self.rfile.read(length))
                if not isinstance(data, dict):
                    raise InputError("Comando JSON no válido.")
                self.json({**workbench.confirm_and_calculate(data), "csrf_token": token})
            except (InputError, ValueError) as exc:
                self.json(
                    {"error": str(exc) if isinstance(exc, InputError) else "JSON no válido."}, 422
                )

    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    server.timeout = 10
    return server


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8020)
    args = parser.parse_args()
    sources = Sources(ROOT)
    workbench = Workbench(
        sources,
        FileStore(ROOT / ".runtime/workbench"),
        profile=os.environ.get("TAX_PROFILE", "local-synthetic"),
    )
    # Fail before opening a socket if a pinned source/rule or fixture has drifted.
    sources.case("C001")
    sources.policy()
    server = make_server(workbench, sources, args.port)
    print(f"Local synthetic workbench: http://127.0.0.1:{server.server_port}/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
