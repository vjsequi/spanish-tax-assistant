"""Atomic local storage for synthetic development; not a multi-worker hosted database."""

from __future__ import annotations

import fcntl
import json
import os
import tempfile
from pathlib import Path
from typing import Any

from renta_assistant.domain.calculation import InputError
from renta_assistant.infrastructure.repository import obj


class FileStore:
    def __init__(self, directory: Path) -> None:
        self.path = directory / "C001.json"
        for path in (directory.parent, directory, self.path):
            if path.is_symlink():
                raise InputError("El estado local no admite enlaces simbólicos.")
        directory.mkdir(parents=True, exist_ok=True, mode=0o700)

    def load(self) -> dict[str, Any] | None:
        if not self.path.exists():
            return None
        if self.path.is_symlink() or self.path.stat().st_size > 4 * 1024 * 1024:
            raise InputError("El estado local no es admisible.")
        return obj(self.path)

    def save(self, data: dict[str, Any]) -> None:
        lock_path = self.path.with_suffix(".lock")
        descriptor = os.open(lock_path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
        with os.fdopen(descriptor, "w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            current = self.load()
            current_version = current["version"] if current is not None else 0
            if current_version != data["version"] - 1:
                raise InputError("Versión obsoleta: otro proceso ha guardado el expediente.")
            self._replace(data)

    def _replace(self, data: dict[str, Any]) -> None:
        descriptor, temporary = tempfile.mkstemp(dir=self.path.parent, prefix=".state-")
        try:
            with os.fdopen(descriptor, "w") as output:
                json.dump(data, output, ensure_ascii=False, indent=2)
                output.flush()
                os.fsync(output.fileno())
            os.replace(temporary, self.path)
        finally:
            Path(temporary).unlink(missing_ok=True)
