import unittest

from src.dataform_unit_testing.sql_unit_test_builder import handle_array_numeric

class TestHandleArrayNumeric(unittest.TestCase):
    def test_array_numbers(self):
        """Test for 'Array Numbers'"""
        array_numbers = "[1, 5.83, 23.25581395348837]"
        expected_output = "[SAFE_CAST(1 AS NUMERIC), SAFE_CAST(5.83 AS NUMERIC), SAFE_CAST(23.25581395348837 AS NUMERIC)]"
        self.assertEqual(handle_array_numeric(array_numbers), expected_output)


if __name__ == "__main__":
    unittest.main()
