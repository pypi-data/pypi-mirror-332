import unittest

from src.dataform_unit_testing.sql_unit_test_builder import replace_table_refs_with_test_inputs

class TestReplaceTableRefsWithTestInputs(unittest.TestCase):
    def test_replace_single_table(self):
        """Test for 'Replacing Single Table'"""
        query_to_replace = "SELECT * FROM `test-project.sources.aims_events`"
        test = {
            "input_data": {
                "sources.aims_events": [
                    {
                        "submission_id": ["NKHWN-SHTJ", "STRING"],
                        "version": ["1", "STRING"],
                        "status": ["COMPLETED", "STRING"]
                    }
                ]
            },
            "expected_output": [
                {
                    "submission_id": "NKHWN-SHTJ",
                    "version": "1",
                    "status": "COMPLETED"
                }
            ]
        }
        expected_output = "actual_output AS (\nSELECT `submission_id`,`version`,`status` FROM (\nSELECT * FROM sources_aims_events\n))"
        self.assertEqual(replace_table_refs_with_test_inputs(test, query_to_replace), expected_output)

    
    def test_replace_multiple_tables(self):
        """Test for 'Replacing Multiple Tables'"""
        query_to_replace = "SELECT * FROM `test-project.sources.aims_events` AS a INNER JOIN `test-project.sources.injuries` AS b ON a.submission_id = b.submission_id"
        test = {
            "input_data": {
                "sources.aims_events": [
                    {
                        "submission_id": ["NKHWN-SHTJ", "STRING"],
                        "version": ["1", "STRING"],
                        "status": ["COMPLETED", "STRING"]
                    }
                ],
                "sources.injuries": [
                    {
                        "submission_id": ["NKHWN-SHTJ", "STRING"]
                    }
                ]
            },
            "expected_output": [
                {
                    "submission_id": "NKHWN-SHTJ",
                    "version": "1",
                    "status": "COMPLETED"
                }
            ]
        }
        expected_output = "actual_output AS (\nSELECT `submission_id`,`version`,`status` FROM (\nSELECT * FROM sources_aims_events AS a INNER JOIN sources_injuries AS b ON a.submission_id = b.submission_id\n))"
        self.assertEqual(replace_table_refs_with_test_inputs(test, query_to_replace), expected_output)
    

    def test_replace_multiple_same_tables(self):
        """Test for 'Replacing Multiple Same Tables'"""
        query_to_replace = "WITH test AS (SELECT * FROM `test-project.sources.aims_events`), test2 AS (SELECT * FROM `test-project.sources.aims_events`) SELECT * FROM test AS a INNER JOIN test 2 AS b ON a.submission_id = b.submission_id"
        test = {
            "input_data": {
                "sources.aims_events": [
                    {
                        "submission_id": ["NKHWN-SHTJ", "STRING"],
                        "version": ["1", "STRING"],
                        "status": ["COMPLETED", "STRING"]
                    }
                ],
                "sources.injuries": [
                    {
                        "submission_id": ["NKHWN-SHTJ", "STRING"]
                    }
                ]
            },
            "expected_output": [
                {
                    "submission_id": "NKHWN-SHTJ",
                    "version": "1",
                    "status": "COMPLETED"
                }
            ]
        }
        expected_output = "actual_output AS (\nSELECT `submission_id`,`version`,`status` FROM (\nWITH test AS (SELECT * FROM sources_aims_events), test2 AS (SELECT * FROM sources_aims_events) SELECT * FROM test AS a INNER JOIN test 2 AS b ON a.submission_id = b.submission_id\n))"
        self.assertEqual(replace_table_refs_with_test_inputs(test, query_to_replace), expected_output)

    
    def test_replace_mixed_usage_tables(self):
        """Test for 'Replacing Mixed Usage of Tables'"""
        query_to_replace = "WITH test AS (SELECT * FROM `test-project.sources.aims_events`), test2 AS (SELECT * FROM `test-project.sources.aims_events`) SELECT * FROM `test-project.sources.injuries` AS i INNER JOIN test AS a ON i.submission_id = a.submission_id INNER JOIN test 2 AS b ON a.submission_id = b.submission_id"
        test = {
            "input_data": {
                "sources.aims_events": [
                    {
                        "submission_id": ["NKHWN-SHTJ", "STRING"],
                        "version": ["1", "STRING"],
                        "status": ["COMPLETED", "STRING"]
                    }
                ],
                "sources.injuries": [
                    {
                        "submission_id": ["NKHWN-SHTJ", "STRING"]
                    }
                ]
            },
            "expected_output": [
                {
                    "submission_id": "NKHWN-SHTJ",
                    "version": "1",
                    "status": "COMPLETED"
                },
                {
                    "submission_id": "NKHWN-SHTJ",
                    "version": "1",
                    "status": "COMPLETED"
                },
            ]
        }
        expected_output = "actual_output AS (\nSELECT `submission_id`,`version`,`status` FROM (\nWITH test AS (SELECT * FROM sources_aims_events), test2 AS (SELECT * FROM sources_aims_events) SELECT * FROM sources_injuries AS i INNER JOIN test AS a ON i.submission_id = a.submission_id INNER JOIN test 2 AS b ON a.submission_id = b.submission_id\n))"
        self.assertEqual(replace_table_refs_with_test_inputs(test, query_to_replace), expected_output)


if __name__ == "__main__":
    unittest.main()
