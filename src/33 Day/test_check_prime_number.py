''' 
    Testcase for is_prime_number function 

    Output:
    Ran 3 tests in 0.000s

    OK
'''

import unittest
from check_prime_number import is_prime_number

class TestClass(unittest.TestCase):
    ''' Unit tests for is_prime_number function'''
    def test_check_prime_true(self):
        self.assertTrue(is_prime_number(2))

    def test_check_prime_false(self):
        self.assertFalse(is_prime_number(6))

    def test_check_prime_number_one(self):
        self.assertFalse(is_prime_number(1))


if __name__=='__main__':
    unittest.main()

