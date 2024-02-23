''' 
    Testcase for handle_invalid_inputs function

    Output:
    Ran 3 tests in 0.002s

    OK
'''
import unittest
from unittest.mock import patch
from handle_invalid_inputs import user_input_int

class TestClass(unittest.TestCase):
    ''' Unit tests for handle_invalid_inputs function '''

    @patch('builtins.input', return_value = '5')
    def test_input_integer(self, mock_input):
        result = user_input_int()
        self.assertEqual(result, 5)

    @patch('builtins.input', return_value = 'a')
    def test_input_char(self, mock_input):
        result = user_input_int()
        self.assertEqual(result, None)

    @patch('builtins.input', return_value = '1.5')
    def test_input_float(self, mock_input):
        result = user_input_int()
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()
