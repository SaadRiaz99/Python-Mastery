# Unit Testing with unittest

import unittest

# Functions to test
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

def is_even(n):
    return n % 2 == 0

def process_string(s):
    if not s:
        return ''
    return s.strip().upper()

# Test class
class TestMathFunctions(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

class TestStringFunctions(unittest.TestCase):

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))

    def test_process_string(self):
        self.assertEqual(process_string('  hello  '), 'HELLO')
        self.assertEqual(process_string(''), '')

if __name__ == '__main__':
    unittest.main()

