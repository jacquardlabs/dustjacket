<!-- dustjacket example — the tokenbucket library rendered in the `standard` format. -->
# tokenbucket

A token-bucket rate limiter for Python. Zero dependencies, Python 3.9+.

## Install

```bash
pip install tokenbucket
```

## Usage

```python
from tokenbucket import TokenBucket

# 10 tokens/sec, burst up to 50.
bucket = TokenBucket(rate=10, capacity=50)

if bucket.take():
    handle(request)   # a token was available
else:
    reject(request)   # bucket empty
```

Consume several tokens at once for weighted calls:

```python
if bucket.take(5):
    ...
```

## API

- `TokenBucket(rate: float, capacity: int)` — a bucket that refills `rate` tokens per second up to `capacity`, starting full.
- `take(n: int = 1) -> bool` — consume `n` tokens if available; returns whether the call is allowed.

## Contributing

Issues and pull requests welcome. See `CONTRIBUTING.md`.

## License

MIT
