# gcs-file-lock

A global file lock using Google Cloud Storage

## Usage

Normal usage:

```python
from gcs_file_lock import gcs_lock

# Acquire a lock
acquired = gcs_lock.lock('gs://bucket-name/lock-name')
print(acquired)

# Release the lock
gcs_lock.unlock('gs://bucket-name/lock-name')
```

