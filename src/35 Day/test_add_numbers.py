''' 
    Testcase for add_numbers(num1, num2) function

    Output:
    Note: Addition of strings is not supported in this method
    ...Error 10 + b: unsupported operand type(s) for +: 'int' and 'str'
    .
    ----------------------------------------------------------------------
    Ran 4 tests in 0.001s

    OK
'''

import unittest
from add_numbers import add_numbers

class TestClass(unittest.TestCase):
    ''' Unit tests for add_numbers function '''

    def test_check_int(self):
        n1 = 10
        n2 = 20
        self.assertEqual(add_numbers(n1, n2), 30)

    def test_check_float(self):
        n1 = 1.55
        n2 = 2.55
        self.assertEqual(add_numbers(n1, n2), 4.1)

    def test_check_char(self):
        char1 = "a"
        char2 = "b"
        self.assertEqual(add_numbers(char1, char2), None)

    def test_check_mixed_types(self):
        n1 = 10
        char2 = "b"
        self.assertEqual(add_numbers(n1, char2), None)

if __name__=='__main__':
    unittest.main()
