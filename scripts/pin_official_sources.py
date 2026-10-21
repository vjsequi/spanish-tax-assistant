"""Explicit, bounded collection of public tax references; offline verification by default."""

from __future__ import annotations

import argparse
import hashlib
import json
import ssl
import time
from datetime import UTC, datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlsplit
from urllib.request import HTTPRedirectHandler, HTTPSHandler, Request, build_opener

from scripts.check_repository import ROOT, inside, read_object, require

CATALOG = "data/rules/2025/catalog.json"
MANIFEST = "data/rules/2025/manifest.json"
HOSTS = {"sede.agenciatributaria.gob.es", "www.boe.es"}
PREFIX = "data/rules/2025/originals/"
MAX_TOTAL = 128 * 1024 * 1024
MAX_SECONDS = 300


class SelectedVersion(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.dates: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if tag == "a" and "version-selected" in (data.get("class") or "").split():
            self.dates.extend(parse_qs(urlsplit(data.get("href") or "").query).get("p", []))


def verify_selected_version(entry: dict[str, Any], raw: bytes) -> str | None:
    expected = entry.get("selected_version")
    if expected is None:
        return None
    parser = SelectedVersion()
    parser.feed(raw.decode("utf-8"))
    require(parser.dates == [expected], "BOE served a different consolidation version")
    return str(expected)


def approved_url(url: str) -> None:
    value = urlsplit(url)
    require(
        value.scheme == "https"
        and value.hostname in HOSTS
        and value.port in (None, 443)
        and value.username is None
        and value.password is None
        and not value.fragment,
        "Reference URL is outside the public official-source allowlist",
    )


class OfficialRedirects(HTTPRedirectHandler):
    def redirect_request(
        self, req: Any, fp: Any, code: int, msg: str, headers: Any, newurl: str
    ) -> Any:
        approved_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def catalog(root: Path) -> list[dict[str, Any]]:
    data = read_object(inside(root, CATALOG))
    entries: list[dict[str, Any]] = data["entries"]
    require(0 < len(entries) <= 32, "Invalid source count")
    require(len({entry["id"] for entry in entries}) == len(entries), "Repeated source ID")
    require(
        len({entry["destination"] for entry in entries}) == len(entries),
        "Repeated source destination",
    )
    for entry in entries:
        approved_url(entry["url"])
        relative = Path(entry["destination"])
        require(
            entry["destination"].startswith(PREFIX)
            and ".." not in relative.parts
            and not relative.is_absolute(),
            "Source destination must stay in the original-reference directory",
        )
        require(entry["kind"] in ("pdf", "html"), "Unsupported reference type")
        require(entry["tax_year"] == 2025, "Wrong source-set tax year")
        current = root
        for part in relative.parts:
            current = current / part
            require(not current.is_symlink(), "Source paths must not contain symbolic links")
    return entries


def verify(root: Path = ROOT, *, complete: bool = True) -> int:
    selected = {entry["id"]: entry for entry in catalog(root)}
    data = read_object(inside(root, MANIFEST))
    require(data["schema_version"] == 1, "Unknown source manifest version")
    require(data["approved_for_application"] is False, "Sources still require tax review")
    entries = data["entries"]
    require(len({entry["id"] for entry in entries}) == len(entries), "Repeated pinned ID")
    require({entry["id"] for entry in entries} <= selected.keys(), "Unselected pinned source")
    if complete:
        require({entry["id"] for entry in entries} == selected.keys(), "Missing pinned source")
    for entry in entries:
        wanted = selected[entry["id"]]
        require(entry["url"] == wanted["url"], "Pinned URL drift")
        require(entry["destination"] == wanted["destination"], "Pinned destination drift")
        approved_url(entry["final_url"])
        path = inside(root, entry["destination"])
        require(type(entry["bytes"]) is int and 0 < entry["bytes"] <= MAX_TOTAL, "Bad source size")
        require(path.stat().st_size == entry["bytes"], "Pinned source size drift")
        raw = path.read_bytes()
        require(hashlib.sha256(raw).hexdigest() == entry["sha256"], "Pinned source hash drift")
        verify_selected_version(wanted, raw)
    return len(entries)


def download(root: Path = ROOT, *, ca_file: str | None = None) -> int:
    selected = catalog(root)
    manifest_path = root / MANIFEST
    if manifest_path.exists():
        verify(root, complete=False)
        result = read_object(manifest_path)
    else:
        result = {
            "schema_version": 1,
            "tax_year": 2025,
            "approved_for_application": False,
            "review_status": "pinned_references_pending_independent_tax_review",
            "entries": [],
        }
    existing = {entry["id"] for entry in result["entries"]}
    opener = build_opener(
        OfficialRedirects(), HTTPSHandler(context=ssl.create_default_context(cafile=ca_file))
    )
    deadline = time.monotonic() + MAX_SECONDS
    total = sum(entry["bytes"] for entry in result["entries"])
    for entry in selected:
        if entry["id"] in existing:
            continue
        require(time.monotonic() < deadline, "Reference collection exceeded time bound")
        path = root / entry["destination"]
        require(not path.exists(), "Unrecorded reference exists; inspect before replacing it")
        path.parent.mkdir(parents=True, exist_ok=True)
        require(path.parent.resolve().is_relative_to(root.resolve()), "Source path escape")
        limit = (32 if entry["kind"] == "pdf" else 5) * 1024 * 1024
        request = Request(entry["url"], headers={"User-Agent": "TaxReferencePin/1.0"})
        with opener.open(request, timeout=min(45, max(1, deadline - time.monotonic()))) as reply:
            approved_url(reply.url)
            chunks: list[bytes] = []
            size = 0
            while block := reply.read(65536):
                size += len(block)
                require(size <= limit and total + size <= MAX_TOTAL, "Reference size bound")
                require(time.monotonic() < deadline, "Reference collection exceeded time bound")
                chunks.append(block)
            raw = b"".join(chunks)
            if entry["kind"] == "pdf":
                require(raw.startswith(b"%PDF-"), "Expected a PDF, not an error document")
            else:
                require(b"<html" in raw.lower(), "Expected HTML")
                for token in entry.get("required_tokens", []):
                    require(token.encode() in raw, "Reference response lacks its identity token")
            selected_version = verify_selected_version(entry, raw)
            receipt = {
                **entry,
                "final_url": reply.url,
                "retrieved_at": datetime.now(UTC).isoformat(),
                "content_type": reply.headers.get("Content-Type"),
                "last_modified": reply.headers.get("Last-Modified"),
                "etag": reply.headers.get("ETag"),
                "bytes": size,
                "sha256": hashlib.sha256(raw).hexdigest(),
                "reported_consolidation_version": selected_version,
            }
        path.write_bytes(raw)
        result["entries"].append(receipt)
        temporary = manifest_path.with_suffix(".tmp")
        temporary.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
        temporary.replace(manifest_path)
        total += size
        print(f"Pinned {entry['id']}: {size} bytes")
    return verify(root)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download", action="store_true", help="Explicit public-reference fetch")
    parser.add_argument("--ca-file", help="Verified CA bundle; TLS verification is never disabled")
    args = parser.parse_args()
    count = download(ca_file=args.ca_file) if args.download else verify()
    print(f"Verified {count} pinned references; independent tax approval is pending.")


if __name__ == "__main__":
    main()
