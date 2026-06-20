"""A token-bucket rate limiter."""
import time

__all__ = ["TokenBucket"]


class TokenBucket:
    """Refills `rate` tokens per second up to `capacity`. `take` returns True if allowed."""

    def __init__(self, rate: float, capacity: int):
        self.rate = rate
        self.capacity = capacity
        self._tokens = float(capacity)
        self._last = time.monotonic()

    def take(self, n: int = 1) -> bool:
        now = time.monotonic()
        self._tokens = min(self.capacity, self._tokens + (now - self._last) * self.rate)
        self._last = now
        if self._tokens >= n:
            self._tokens -= n
            return True
        return False
