from gcs_mutex_lock import gcs_lock

TEST_LOCK = 'gs://circleci-gcs-mutex-lock/test.lock'


# noinspection PyProtectedMember
def test_lock_basic():
    acquired = gcs_lock.lock(TEST_LOCK)
    assert acquired
