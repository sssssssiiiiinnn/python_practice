"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""


import logging


import log_test


formatter = '%(asctime)s;%(levelname)s;%(name)s;%(message)s'
# logging.basicConfig(level=logging.INFO, filename='test.log', format=formatter)
logging.basicConfig(level=logging.INFO, format=formatter)

# logging.critical('critical ')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')
# logging.critical('critical: {}'.format('test'))


class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message

logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())
logger.setLevel(logging.INFO)
logger.info('username')
logger.info('password')

log_test.do_something()


