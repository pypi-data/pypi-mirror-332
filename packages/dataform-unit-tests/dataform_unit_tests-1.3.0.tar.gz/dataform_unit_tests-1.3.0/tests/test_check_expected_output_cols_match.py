import unittest

from src.dataform_unit_testing.unit_test_parser import check_expected_output_cols_match

class TestCheckExpectedOutputColumnsMatch(unittest.TestCase):
    def test_one_table_matches(self):
        """Test for 'One Input Table Columns Match'"""
        test = {
            "expected_output": [
                {
                    "submission_id": "NKHWN-SHTJ",
                    "version": "1",
                    "status": "COMPLETED"
                },
                {
                    "submission_id": "NKHWN-SHTK",
                    "version": "2",
                    "status": "DRAFT"
                }
            ]
        }
        self.assertTrue(check_expected_output_cols_match(test["expected_output"]))

    
    def test_one_table_not_matches(self):
        """Test for 'One Input Table Columns Doesn't Match'"""
        test = {
            "expected_output": [
                {
                    "submission_id": "NKHWN-SHTJ",
                    "version": "1",
                    "status": "COMPLETED"
                },
                {
                    "submission_id": "NKHWN-SHTK",
                    "version": "2"
                }
            ]
        }
        self.assertFalse(check_expected_output_cols_match(test["expected_output"]))
    

    def test_one_table_extra_column(self):
        """Test for 'One Input Table Has Extra Column second row'"""
        test = {
            "expected_output": [
                {
                    "submission_id": "NKHWN-SHTJ",
                    "version": "1",
                    "status": "COMPLETED"
                },
                {
                    "submission_id": "NKHWN-SHTK",
                    "version": "2",
                    "status": "DRAFT",
                    "rms": "someone@someone.co.uk"
                }
            ]
        }
        self.assertFalse(check_expected_output_cols_match(test["expected_output"]))


if __name__ == "__main__":
    unittest.main()
