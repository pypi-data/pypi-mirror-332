import unittest

from src.dataform_unit_testing.unit_test_parser import check_input_table_cols_match

class TestCheckInputTableColumnsMatch(unittest.TestCase):
    def test_one_table_matches(self):
        """Test for 'One Input Table Columns Match'"""
        test = {
            "input_data": {
                "sources.raw_aims_events": [
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
        }
        self.assertTrue(check_input_table_cols_match(test["input_data"]))

    
    def test_one_table_not_matches(self):
        """Test for 'One Input Table Columns Doesn't Match'"""
        test = {
            "input_data": {
                "sources.raw_aims_events": [
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
        }
        self.assertFalse(check_input_table_cols_match(test["input_data"]))
    

    def test_one_table_extra_column(self):
        """Test for 'One Input Table Has Extra Column second row'"""
        test = {
            "input_data": {
                "sources.raw_aims_events": [
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
        }
        self.assertFalse(check_input_table_cols_match(test["input_data"]))

    
    def test_two_tables_match(self):
        """Test for 'Two Input Table Columns Match'"""
        test = {
            "input_data": {
                "sources.raw_aims_events": [
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
                ],
                "staging.fake_table": [
                    {
                        "a": "x",
                        "b": "y"
                    },
                    {
                        "a": "l",
                        "b": "m"
                    }
                ]
            }
        }
        self.assertTrue(check_input_table_cols_match(test["input_data"]))


    def test_second_table_not_matches(self):
        """Test for 'Two Input Table Columns Match'"""
        test = {
            "input_data": {
                "sources.raw_aims_events": [
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
                ],
                "staging.fake_table": [
                    {
                        "a": "x",
                        "b": "y"
                    },
                    {
                        "a": "l",
                        "b": "m",
                        "c": "n"
                    }
                ]
            }
        }
        self.assertFalse(check_input_table_cols_match(test["input_data"]))


if __name__ == "__main__":
    unittest.main()
