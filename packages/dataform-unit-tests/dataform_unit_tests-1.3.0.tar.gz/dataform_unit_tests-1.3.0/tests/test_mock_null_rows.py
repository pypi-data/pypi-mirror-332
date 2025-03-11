import unittest

from src.dataform_unit_testing.unit_test_parser import mock_null_rows

class TestCreateInputCTEs(unittest.TestCase):
    def test_null_rows(self):
        """Test for 'Null Rows'"""
        rows = None
        column_dtypes = {"submission_id": "STRING", "version": "STRING", "status": "STRING", "occurrence_date": "STRING", "occurrence_at": "STRING", "created_at": "TIMESTAMP"}
        expected_output = [
            {
                "submission_id": None,
                "version": None,
                "status": None,
                "occurrence_date": None,
                "occurrence_at": None,
                "created_at": None
            }
        ]
        self.assertEqual(mock_null_rows(rows, column_dtypes), expected_output)


    def test_non_null_rows(self):
        """Test for 'Non Null Rows'"""
        rows = [
            {
                "submission_id": "NKHWN-SHTJ",
                "version": "1",
                "status": "COMPLETED",
                "occurrence_date": "2024-09-22",
                "occurrence_at": "19:00",
                "created_at": "2024-10-09 18:00:30.005000 UTC"
            }
        ]
        column_dtypes = {"submission_id": "STRING", "version": "STRING", "status": "STRING", "occurrence_date": "STRING", "occurrence_at": "STRING", "created_at": "TIMESTAMP"}
        expected_output = [
            {
                "submission_id": "NKHWN-SHTJ",
                "version": "1",
                "status": "COMPLETED",
                "occurrence_date": "2024-09-22",
                "occurrence_at": "19:00",
                "created_at": "2024-10-09 18:00:30.005000 UTC"
            }
        ]
        self.assertEqual(mock_null_rows(rows, column_dtypes), expected_output)


if __name__ == "__main__":
    unittest.main()
