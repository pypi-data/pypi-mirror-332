import unittest

from src.dataform_unit_testing.unit_test_parser import check_input_tables_exist

class TestCheckInputTablesExist(unittest.TestCase):
    def test_one_table_exist(self):
        """Test for 'One Input Table Exist'"""
        test = {
            "input_data": {
                "sources.raw_aims_events": [
                    {
                        "submission_id": ["NKHWN-SHTJ", "STRING"],
                        "version": ["1", "STRING"],
                        "status": ["COMPLETED", "STRING"]
                    }
                ]
            }
        }
        model_to_check = "SELECT * FROM `prod-dataform-1f5f8a4e.sources.raw_aims_events`"
        self.assertTrue(check_input_tables_exist(test, model_to_check))

    
    def test_all_tables_exist(self):
        """Test for 'All Input Tables Exist'"""
        test = {
            "input_data": {
                "sources.raw_aims_events": [
                    {
                        "submission_id": ["NKHWN-SHTJ", "STRING"],
                        "version": ["1", "STRING"],
                        "status": ["COMPLETED", "STRING"]
                    }
                ],
                "staging.fake_table": [
                    {
                        "col_1": ["x", "STRING"]
                    }
                ]
            }
        }
        model_to_check = "SELECT * FROM `prod-dataform-1f5f8a4e.sources.raw_aims_events` AS a INNER JOIN `prod-dataform-1f5f8a4e.staging.fake_table` AS b ON a.submission_id = b.col_1"
        self.assertTrue(check_input_tables_exist(test, model_to_check))

    
    def test_one_table_not_exists(self):
        """Test for 'One Input Table Doesn't Exist'"""
        test = {
            "input_data": {
                "sources.raw_aims_events": [
                    {
                        "submission_id": ["NKHWN-SHTJ", "STRING"],
                        "version": ["1", "STRING"],
                        "status": ["COMPLETED", "STRING"]
                    }
                ],
                "staging.fake_table": [
                    {
                        "col_1": ["x", "STRING"]
                    }
                ]
            }
        }
        model_to_check = "SELECT * FROM `prod-dataform-1f5f8a4e.sources.raw_aims_events` AS a INNER JOIN `prod-dataform-1f5f8a4e.staging.different_table` AS b ON a.submission_id = b.col_1"
        self.assertFalse(check_input_tables_exist(test, model_to_check))

    
    def test_unqualified_schema_table_not_exists(self):
        """Test for 'Unqualified Schema Table Doesn't Exist'"""
        test = {
            "input_data": {
                "raw_aims_events": [
                    {
                        "submission_id": ["NKHWN-SHTJ", "STRING"],
                        "version": ["1", "STRING"],
                        "status": ["COMPLETED", "STRING"]
                    }
                ],
                "staging.fake_table": [
                    {
                        "col_1": ["x", "STRING"]
                    }
                ]
            }
        }
        model_to_check = "SELECT * FROM `prod-dataform-1f5f8a4e.sources.raw_aims_events` AS a INNER JOIN `prod-dataform-1f5f8a4e.staging.fake_table` AS b ON a.submission_id = b.col_1"
        self.assertFalse(check_input_tables_exist(test, model_to_check))


if __name__ == "__main__":
    unittest.main()
