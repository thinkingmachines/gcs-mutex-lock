from subprocess import check_output, Popen, PIPE, STDOUT, CalledProcessError
import backoff
import logging


def lock(lock_path):
    """
    Creates a lock with the specified GCS path.
    :param lock_path: the lock's GCS path with the gs://bucket-name/file-name format
    :return: boolean, if lock acquired or not
    """
    logging.debug("Acquiring lock: {}".format(lock_path))
    echo = Popen('echo "lock"', shell=True, stdout=PIPE)
    try:
        gsutil_command = 'gsutil -q -h "x-goog-if-generation-match:0" cp - {}'.format(lock_path)
        check_output(gsutil_command, stdin=echo.stdout, shell=True, stderr=STDOUT)
        echo.wait()
        logging.debug("Lock acquired: {}".format(lock_path))
        return True
    except CalledProcessError:
        logging.debug("Cannot acquire lock: {}".format(lock_path))
        return False


def unlock(lock_path):
    """
    Releases the specified lock.
    :param lock_path: the lock's GCS path with the gs://bucket-name/file-name format
    :return: None
    """
    gsutil_command = 'gsutil -q rm {}'.format(lock_path)
    check_output(gsutil_command, shell=True, stderr=STDOUT)
    logging.debug("Lock released: {}".format(lock_path))


def wait_for_lock(lock_path, *backoff_args, **backoff_kwargs):
    """
    Tries to acquire the specified lock. If the lock cannot be acquired, waits for the lock to be freed.
    :param lock_path: the lock's GCS path with the gs://bucket-name/file-name format
    :param backoff_args: Args to be passed to @backoff.on_predicate
    :param backoff_kwargs: Kwargs to be passed to @backoff.on_predicate
    :return: If the lock was acquired or not
    """

    @backoff.on_predicate(*backoff_args, **backoff_kwargs)
    def backoff_lock():
        return lock(lock_path)

    return backoff_lock()


def wait_for_lock_expo(lock_path, base=2, factor=1, max_value=10, max_time=60, jitter=backoff.full_jitter, *args,
                       **kwargs):
    """
    A helper function for `wait_for_lock` that uses exponential backoff.
    :param lock_path:  the lock's GCS path with the gs://bucket-name/file-name format
    :param base: waiting time (sec) is: factor * (base ** n)
    :param factor: waiting time (sec) is: factor * (base ** n)
    :param max_value: the ceiling value for retry time, in seconds
    :param max_time: total retry timeout, in seconds
    :param jitter: See backoff.on_predicate for details. Pass jitter=None for no jitter.
    :return: If the lock was acquired or not
    """
    return wait_for_lock(lock_path, wait_gen=backoff.expo, base=base, factor=factor, max_value=max_value,
                         max_time=max_time, jitter=jitter, *args, **kwargs)
