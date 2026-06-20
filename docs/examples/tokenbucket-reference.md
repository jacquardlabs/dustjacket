<!-- dustjacket example — the tokenbucket library rendered in the `reference` format. -->
# tokenbucket

Token-bucket rate limiter for Python. Refills at a configurable rate; `take` returns a boolean so the
caller decides how to handle rejection.

## Contents

- [Install](#install)
- [Usage](#usage)
- [API](#api)
- [Algorithm](#algorithm)
- [License](#license)

## Install

```bash
pip install tokenbucket
```

**[⬆ back to top](#contents)**

## Usage

```python
from tokenbucket import TokenBucket

bucket = TokenBucket(rate=10, capacity=50)
bucket.take()      # consume 1 token
bucket.take(5)     # consume 5
```

**[⬆ back to top](#contents)**

## API

### `TokenBucket(rate, capacity)`

| Parameter | Type | Description |
|-----------|------|-------------|
| `rate` | `float` | Tokens added per second. |
| `capacity` | `int` | Maximum token ceiling. The bucket starts full. |

### `take(n=1) -> bool`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `n` | `int` | `1` | Tokens to consume. |

Returns `True` and consumes `n` tokens if at least `n` are available; otherwise returns `False` without
consuming any. Never blocks.

**[⬆ back to top](#contents)**

## Algorithm

Implements the [token bucket](https://en.wikipedia.org/wiki/Token_bucket) algorithm with
`time.monotonic` for drift-free timing. Each `take` adds `elapsed * rate` tokens (capped at `capacity`),
then consumes if enough are present. Refill is lazy; there is no background thread.

**[⬆ back to top](#contents)**

## License

MIT
