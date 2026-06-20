<!-- dustjacket example — the tokenbucket library rendered in the `landing` format.
     The hero uses a placeholder image; a real repo would ship its own logo under docs/assets/. -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://placehold.co/640x140/0d1117/e6edf3?text=tokenbucket">
    <img alt="tokenbucket" src="https://placehold.co/640x140/ffffff/24292f?text=tokenbucket" width="640">
  </picture>
</p>

# tokenbucket

Rate-limit any call to a steady rate, with bursts.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](#license)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)

## ✦ Why tokenbucket

| | |
|---|---|
| **Zero dependencies** | Pure stdlib. Imports only `time`. |
| **Monotonic clock** | Uses `time.monotonic()`, so clock changes never corrupt the bucket. |
| **Fractional rates** | `rate` is a `float`: 0.5 or 100.5 tokens/sec, same precision. |
| **Weighted calls** | `take(n)` consumes `n` tokens in one call. |

## ⚡ Quick start

```bash
pip install tokenbucket
```

```python
from tokenbucket import TokenBucket

bucket = TokenBucket(rate=10, capacity=50)
if bucket.take():
    ...  # allowed
```

## 📖 Documentation

`TokenBucket(rate, capacity)` and `take(n=1) -> bool`. Refills continuously up to `capacity`.

## License

MIT
