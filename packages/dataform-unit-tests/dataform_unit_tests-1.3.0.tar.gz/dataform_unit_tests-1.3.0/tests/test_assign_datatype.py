import unittest

from src.dataform_unit_testing.unit_test_parser import assign_datatype, mock_null_rows

class TestAssignDatatype(unittest.TestCase):
    def test_one_row(self):
        """Test for 'One Row'"""
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
                "submission_id": ["NKHWN-SHTJ", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"],
                "occurrence_date": ["2024-09-22", "STRING"],
                "occurrence_at": ["19:00", "STRING"],
                "created_at": ["2024-10-09 18:00:30.005000 UTC", "TIMESTAMP"]
            }
        ]
        assign_datatype(rows, column_dtypes)
        self.assertEqual(rows, expected_output)

        
    def test_multiple_rows(self):
        """Test for 'Multiple Rows'"""
        rows = [
            {
                "submission_id": "NKHWN-SHTJ",
                "version": "1",
                "status": "COMPLETED",
                "occurrence_date": "2024-09-22",
                "occurrence_at": "19:00",
                "created_at": "2024-10-09 18:00:30.005000 UTC"
            },
            {
                "submission_id": "NKHWN-SHTK",
                "version": "1",
                "status": "COMPLETED",
                "occurrence_date": "2024-09-23",
                "occurrence_at": "19:00",
                "created_at": "2024-10-10 18:00:30.005000 UTC"
            }
        ]
        column_dtypes = {"submission_id": "STRING", "version": "STRING", "status": "STRING", "occurrence_date": "STRING", "occurrence_at": "STRING", "created_at": "TIMESTAMP"}
        expected_output = [
            {
                "submission_id": ["NKHWN-SHTJ", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"],
                "occurrence_date": ["2024-09-22", "STRING"],
                "occurrence_at": ["19:00", "STRING"],
                "created_at": ["2024-10-09 18:00:30.005000 UTC", "TIMESTAMP"]
            },
            {
                "submission_id": ["NKHWN-SHTK", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"],
                "occurrence_date": ["2024-09-23", "STRING"],
                "occurrence_at": ["19:00", "STRING"],
                "created_at": ["2024-10-10 18:00:30.005000 UTC", "TIMESTAMP"]
            }
        ]
        assign_datatype(rows, column_dtypes)
        self.assertEqual(rows, expected_output)


    def test_nested_rows(self):
        """Test for 'Nested Rows'"""
        rows = [
            {
                "submission_id": "NKHWN-SHTJ",
                "version": "1",
                "status": "COMPLETED",
                "occurrence_date": "2024-09-22",
                "occurrence_at": "19:00",
                "created_at": "2024-10-09 18:00:30.005000 UTC",
                "injured": [
                    {
                        "injured_individual": "Nandoca",
                        "injured_age": "24"
                    }
                ]
            }
        ]
        column_dtypes = {
            "submission_id": "STRING",
            "version": "STRING",
            "status": "STRING",
            "occurrence_date": "STRING",
            "occurrence_at": "STRING",
            "created_at": "TIMESTAMP",
            "injured": "RECORD",
            "injured.injured_individual": "STRING",
            "injured.injured_age": "STRING"
        }
        expected_output = [
            {
                "submission_id": ["NKHWN-SHTJ", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"],
                "occurrence_date": ["2024-09-22", "STRING"],
                "occurrence_at": ["19:00", "STRING"],
                "created_at": ["2024-10-09 18:00:30.005000 UTC", "TIMESTAMP"],
                "injured": [[
                    {
                        "injured_individual": ["Nandoca", "STRING"],
                        "injured_age": ["24", "STRING"]
                    }
                ], "RECORD"]
            }
        ]
        assign_datatype(rows, column_dtypes)
        self.assertEqual(rows, expected_output)
    
    
    def test_multiple_nested_rows(self):
        """Test for 'Multiple Nested Rows'"""
        rows = [
            {
                "submission_id": "NKHWN-SHTJ",
                "version": "1",
                "status": "COMPLETED",
                "occurrence_date": "2024-09-22",
                "occurrence_at": "19:00",
                "created_at": "2024-10-09 18:00:30.005000 UTC",
                "injured": [
                    {
                        "injured_individual": "Nandoca",
                        "injured_age": "24"
                    }
                ]
            },
            {
                "submission_id": "NKHWN-SHTK",
                "version": "1",
                "status": "COMPLETED",
                "occurrence_date": "2024-09-23",
                "occurrence_at": "19:00",
                "created_at": "2024-10-10 18:00:30.005000 UTC",
                "injured": [
                    {
                        "injured_individual": "Nandoca",
                        "injured_age": "21"
                    }
                ]
            }
        ]
        column_dtypes = {
            "submission_id": "STRING",
            "version": "STRING",
            "status": "STRING",
            "occurrence_date": "STRING",
            "occurrence_at": "STRING",
            "created_at": "TIMESTAMP",
            "injured": "RECORD",
            "injured.injured_individual": "STRING",
            "injured.injured_age": "STRING"
        }
        expected_output = [
            {
                "submission_id": ["NKHWN-SHTJ", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"],
                "occurrence_date": ["2024-09-22", "STRING"],
                "occurrence_at": ["19:00", "STRING"],
                "created_at": ["2024-10-09 18:00:30.005000 UTC", "TIMESTAMP"],
                "injured": [[
                    {
                        "injured_individual": ["Nandoca", "STRING"],
                        "injured_age": ["24", "STRING"]
                    }
                ], "RECORD"]
            },
            {
                "submission_id": ["NKHWN-SHTK", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"],
                "occurrence_date": ["2024-09-23", "STRING"],
                "occurrence_at": ["19:00", "STRING"],
                "created_at": ["2024-10-10 18:00:30.005000 UTC", "TIMESTAMP"],
                "injured": [[
                    {
                        "injured_individual": ["Nandoca", "STRING"],
                        "injured_age": ["21", "STRING"]
                    }
                ], "RECORD"]
            }
        ]
        assign_datatype(rows, column_dtypes)
        self.assertEqual(rows, expected_output)


    def test_multiple_nested_rows_with_nested_rows(self):
        """Test for 'Multiple Nested Rows with Nested Rows'"""
        rows = [
            {
                "submission_id": "NKHWN-SHTJ",
                "version": "1",
                "status": "COMPLETED",
                "occurrence_date": "2024-09-22",
                "occurrence_at": "19:00",
                "created_at": "2024-10-09 18:00:30.005000 UTC",
                "injured": [
                    {
                        "injured_individual": "Nandoca",
                        "injured_age": "24",
                        "injury": [
                            {
                                "injury_1": "Broken ankle",
                                "injury_2": "Bruised shoulder"
                            }
                        ]
                    }
                ]
            },
            {
                "submission_id": "NKHWN-SHTK",
                "version": "1",
                "status": "COMPLETED",
                "occurrence_date": "2024-09-23",
                "occurrence_at": "19:00",
                "created_at": "2024-10-10 18:00:30.005000 UTC",
                "injured": [
                    {
                        "injured_individual": "Nandoca",
                        "injured_age": "21",
                        "injury": [
                            {
                                "injury_1": "Broken ankle",
                                "injury_2": "Bruised shoulder"
                            }
                        ]
                    }
                ]
            }
        ]
        column_dtypes = {
            "submission_id": "STRING",
            "version": "STRING",
            "status": "STRING",
            "occurrence_date": "STRING",
            "occurrence_at": "STRING",
            "created_at": "TIMESTAMP",
            "injured": "RECORD",
            "injured.injured_individual": "STRING",
            "injured.injured_age": "STRING",
            "injured.injury": "RECORD",
            "injured.injury.injury_1": "STRING",
            "injured.injury.injury_2": "STRING"
        }
        expected_output = [
            {
                "submission_id": ["NKHWN-SHTJ", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"],
                "occurrence_date": ["2024-09-22", "STRING"],
                "occurrence_at": ["19:00", "STRING"],
                "created_at": ["2024-10-09 18:00:30.005000 UTC", "TIMESTAMP"],
                "injured": [[
                    {
                        "injured_individual": ["Nandoca", "STRING"],
                        "injured_age": ["24", "STRING"],
                        "injury": [[
                            {
                                "injury_1": ["Broken ankle", "STRING"],
                                "injury_2": ["Bruised shoulder", "STRING"]
                            }
                        ], "RECORD"]
                    }
                ], "RECORD"]
            },
            {
                "submission_id": ["NKHWN-SHTK", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"],
                "occurrence_date": ["2024-09-23", "STRING"],
                "occurrence_at": ["19:00", "STRING"],
                "created_at": ["2024-10-10 18:00:30.005000 UTC", "TIMESTAMP"],
                "injured": [[
                    {
                        "injured_individual": ["Nandoca", "STRING"],
                        "injured_age": ["21", "STRING"],
                        "injury": [[
                            {
                                "injury_1": ["Broken ankle", "STRING"],
                                "injury_2": ["Bruised shoulder", "STRING"]
                            }
                        ], "RECORD"]
                    }
                ], "RECORD"]
            }
        ]
        assign_datatype(rows, column_dtypes)
        self.assertEqual(rows, expected_output)

    
    def test_null_rows(self):
        """Test for 'Null Rows'"""
        rows = None
        column_dtypes = {"submission_id": "STRING", "version": "STRING", "status": "STRING", "occurrence_date": "STRING", "occurrence_at": "STRING", "created_at": "TIMESTAMP"}
        expected_output = [
            {
                "submission_id": [None, "STRING"],
                "version": [None, "STRING"],
                "status": [None, "STRING"],
                "occurrence_date": [None, "STRING"],
                "occurrence_at": [None, "STRING"],
                "created_at": [None, "TIMESTAMP"]
            }
        ]
        rows = mock_null_rows(rows, column_dtypes)
        assign_datatype(rows, column_dtypes)
        self.assertEqual(rows, expected_output)
    

if __name__ == "__main__":
    unittest.main()
