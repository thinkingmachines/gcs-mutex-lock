from gcs_file_lock import gcs_lock
import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.info("Test start")
acquired = gcs_lock.wait_for_lock_expo('gs://psc-demand/dataflow/temp_lock.txt', max_time=60, jitter=None)
print('Acquired? '+str(acquired))

gcs_lock.unlock('gs://psc-demand/dataflow/temp_lock.txt')
