import unittest

from unittest.mock import Mock, patch
from src.dataform_unit_testing.unit_test_runner import run_tests

MOCK_COMPILATION_RESULT = Mock()
MOCK_GCP_PROJECT_ID = Mock()
MOCK_TEST_CASE_ONE = {"name": "Test One"}
MOCK_TEST_CASE_TWO = {"name": "Test Two"}
MOCK_TEST_CASE_THREE = {"name": "Test Three"}

class TestRunTests(unittest.TestCase):
    @patch('src.dataform_unit_testing.unit_test_extractor.get_unit_tests')
    @patch('src.dataform_unit_testing.unit_test_parser.validate_schema')
    @patch('src.dataform_unit_testing.unit_test_extractor.get_model_to_test')
    @patch('src.dataform_unit_testing.unit_test_runner.validate_mocked_tables')
    @patch('src.dataform_unit_testing.unit_test_runner.execute_test')
    @patch('src.dataform_unit_testing.unit_test_runner.is_passed_test')
    def test_two_fail_one_pass_test_on_validation(self, mock_is_passed_test, mock_execute_test, mock_validated_mocked_tables, mock_get_model_to_test, mock_validate_schema, mock_get_unit_tests):
        """Test for 'Two Failed Tests and One Passed Test on Validation'"""
        mock_get_unit_tests.return_value = [MOCK_TEST_CASE_ONE, MOCK_TEST_CASE_TWO, MOCK_TEST_CASE_THREE]
        mock_validate_schema.side_effect = [False, False, True]
        mock_get_model_to_test.return_value = True, "SELECT * FROM test"
        mock_validated_mocked_tables.return_value = True
        mock_result = Mock()
        mock_execute_test.return_value = mock_result
        mock_is_passed_test.return_value = True
        self.assertEqual(run_tests(MOCK_COMPILATION_RESULT, MOCK_GCP_PROJECT_ID), ["Test One", "Test Two"])


if __name__ == "__main__":
    unittest.main()
