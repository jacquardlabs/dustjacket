"""An HTTP response cache with memory and disk backends."""
import json
import time
from pathlib import Path

__all__ = ["Cache"]


class Cache:
    """A TTL cache. backend is "memory" or "disk"."""

    def __init__(self, backend: str = "memory", path: str = ".httpcache"):
        if backend not in ("memory", "disk"):
            raise ValueError("backend must be 'memory' or 'disk'")
        self.backend = backend
        self._mem: dict = {}
        self._dir = Path(path)
        if backend == "disk":
            self._dir.mkdir(exist_ok=True)

    def set(self, key: str, value, ttl: int = 60) -> None:
        record = {"value": value, "expires": time.time() + ttl}
        if self.backend == "memory":
            self._mem[key] = record
        else:
            (self._dir / key).write_text(json.dumps(record))

    def get(self, key: str):
        if self.backend == "memory":
            record = self._mem.get(key)
        else:
            f = self._dir / key
            record = json.loads(f.read_text()) if f.exists() else None
        if not record or record["expires"] < time.time():
            return None
        return record["value"]
