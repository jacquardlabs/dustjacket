<!-- dustjacket example — the tokenbucket library rendered in the `tutorial` format. -->
# tokenbucket

Rate-limit any function in three steps.

## ✦ Getting started

Prerequisites: Python 3.9+. No other dependencies.

```bash
pip install tokenbucket
```

## ✦ Walkthrough

1. **Create a bucket.** Allow 10 calls per second, bursting up to 50.

   ```python
   from tokenbucket import TokenBucket

   bucket = TokenBucket(rate=10, capacity=50)
   ```

2. **Gate each call.** `take()` returns `True` when a token is available.

   ```python
   if bucket.take():
       handle(request)
   else:
       reject(request)
   ```

3. **Charge heavier calls more.** Pass `n` to consume several tokens at once.

   ```python
   if bucket.take(5):
       run_expensive_job()
   ```

## ✦ What just happened

The bucket refilled continuously between calls, so steady traffic passes and bursts are capped at
`capacity`. No background thread runs; refill is computed on each `take`.

## Next steps

- Tune `rate` and `capacity` to your traffic.
- Wrap `take` in your framework's middleware.

## License

MIT
