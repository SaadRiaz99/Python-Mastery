"""Day 14: Use the failed assertions and log output to locate the formula bug."""

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def calculate_bill(units):
    logger.info("Calculating bill for %s units", units)
    if units <= 100:
        return units * 10
    return 100 * 10 + (units - 100 * 15)

assert calculate_bill(50) == 500
assert calculate_bill(120) == 1300
print("Day 14 passed")
