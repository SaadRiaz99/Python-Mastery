# Advanced Logging

import logging
import logging.config

# Dict config
LOGGING_CONFIG = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

# Context logging
import contextvars
request_id = contextvars.ContextVar('request_id', default='unknown')

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id.get()
        return True

logger.addFilter(ContextFilter())
logger.propagate = False

request_id.set('req-123')
logger.info('Processing request')

# Performance logging
import time
from functools import wraps

def log_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        logger.info(f'{func.__name__} took {elapsed:.4f}s')
        return result
    return wrapper

@log_performance
def slow_function():
    time.sleep(0.1)
    return 'done'

slow_function()

