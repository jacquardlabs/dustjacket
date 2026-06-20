<!-- dustjacket example — the tokenbucket library rendered in the `minimal` format. -->
# tokenbucket

A token-bucket rate limiter for Python.

## Install

```bash
pip install tokenbucket
```

## Usage

```python
from tokenbucket import TokenBucket

bucket = TokenBucket(rate=10, capacity=50)
if bucket.take():
    ...  # allowed
```

## License

MIT
