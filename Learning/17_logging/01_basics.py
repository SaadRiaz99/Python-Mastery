# Python Logging

import logging

# Basic logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Different log levels
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# Custom format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger('myapp')

# Logger with file handler
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.warning('This goes to file')

# Logger with multiple handlers
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.info('This goes to console and maybe file')

# Practical example
def divide_numbers(a, b):
    logger.info(f'Dividing {a} by {b}')
    try:
        result = a / b
        logger.debug(f'Result: {result}')
        return result
    except ZeroDivisionError:
        logger.error('Division by zero attempted')
        raise

divide_numbers(10, 2)
divide_numbers(10, 0)

