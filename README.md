# gcs-mutex-lock

A global file-based mutex lock using Google Cloud Storage. Supports retries with exponential backoff via [backoff](https://github.com/litl/backoff).

This library is inspired by [gcslock](https://github.com/marcacohen/gcslock).

## Installation

```bash
pip install git+https://github.com/thinkingmachines/gcs-mutex-lock.git
```

## Usage

Simple usage:

```python
from gcs_mutex_lock import gcs_lock

# Acquire a lock
acquired = gcs_lock.lock('gs://bucket-name/lock-name')
print(acquired)

# Release the lock
gcs_lock.unlock('gs://bucket-name/lock-name')
```

Wait for lock to be freed, then acquire it:

```python
from gcs_mutex_lock import gcs_lock

# Acquire lock, then retry with (truncated) exponential backoff
acquired = gcs_lock.wait_for_lock_expo('gs://bucket-name/lock-name')
print(acquired)
```

## Backoff

To configure backoff parameters, see the [backoff](https://github.com/litl/backoff) library.

The backoff parameters can be passed as `*args` and `**kwargs` to any of the `wait_for_lock` functions.

### Exponential Backoff w/Jitter

Use the `wait_for_lock_expo` for exponential backoff. Full jitter is included by default, so pass `jitter=None` to see pure exponential behavior.

The default backoff behavior for `wait_for_lock_expo` is defined in this AWS [post](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/).
