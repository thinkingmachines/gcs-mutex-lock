from gcs_mutex_lock import gcs_lock


# noinspection PyProtectedMember
def test_lock_basic():
    # Make sure no error
    acquired = gcs_lock.lock('gs://psc-demand/dataflow/hello.txt')
    assert acquired
