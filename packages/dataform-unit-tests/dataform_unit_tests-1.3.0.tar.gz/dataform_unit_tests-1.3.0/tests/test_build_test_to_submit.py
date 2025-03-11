import unittest

from src.dataform_unit_testing.sql_unit_test_builder import build_test_to_submit, queries_to_test

class TestBuildTestToSubmit(unittest.TestCase):
    def test_single_table_input(self):
        """Test for 'Single Table Input'"""
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
                    "submission_id": ["NKHWN-SHTJ", "STRING"],
                    "version": ["1", "STRING"],
                    "status": ["COMPLETED", "STRING"]
                }
            ]
        }
        final_ctes = queries_to_test()
        expected_output = f"WITH sources_aims_events AS (\nSELECT\n\tSAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`\n),\nexpected_output AS (\nSELECT\n\tSAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`\n),\nactual_output AS (\nSELECT `submission_id`,`version`,`status` FROM (\nSELECT * FROM sources_aims_events\n)),\n{final_ctes}"
        self.maxDiff = None
        self.assertEqual(build_test_to_submit(test, query_to_replace), expected_output)
    

    def test_multiple_table_input(self):
        """Test for 'Multiple Table Input'"""
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
                    "submission_id": ["NKHWN-SHTJ", "STRING"],
                    "version": ["1", "STRING"],
                    "status": ["COMPLETED", "STRING"]
                }
            ]
        }
        final_ctes = queries_to_test()
        expected_output = f"WITH sources_aims_events AS (\nSELECT\n\tSAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`\n),\nsources_injuries AS (\nSELECT\n\tSAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`\n),\nexpected_output AS (\nSELECT\n\tSAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`\n),\nactual_output AS (\nSELECT `submission_id`,`version`,`status` FROM (\nSELECT * FROM sources_aims_events AS a INNER JOIN sources_injuries AS b ON a.submission_id = b.submission_id\n)),\n{final_ctes}"
        self.maxDiff = None
        self.assertEqual(build_test_to_submit(test, query_to_replace), expected_output)

    
    def test_single_table_input_with_bytes(self):
        """Test for 'Single Table Input with Bytes'"""
        query_to_replace = "SELECT * FROM `test-project.sources.aims_events`"
        test = {
            "input_data": {
                "sources.aims_events": [
                    {
                        "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"],
                        "version": ["1", "STRING"],
                        "status": ["COMPLETED", "STRING"]
                    }
                ]
            },
            "expected_output": [
                {
                    "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"],
                    "version": ["1", "STRING"],
                    "status": ["COMPLETED", "STRING"]
                }
            ]
        }
        final_ctes = queries_to_test()
        expected_output = f"WITH sources_aims_events AS (\nSELECT\n\tFROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA==') AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`\n),\nexpected_output AS (\nSELECT\n\tFROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA==') AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`\n),\nactual_output AS (\nSELECT `submission_id`,`version`,`status` FROM (\nSELECT * FROM sources_aims_events\n)),\n{final_ctes}"
        self.maxDiff = None
        self.assertEqual(build_test_to_submit(test, query_to_replace), expected_output)
    

    def test_multiple_table_input_with_bytes(self):
        """Test for 'Multiple Table Input with Bytes'"""
        query_to_replace = "SELECT * FROM `test-project.sources.aims_events` AS a INNER JOIN `test-project.sources.injuries` AS b ON a.submission_id = b.submission_id"
        test = {
            "input_data": {
                "sources.aims_events": [
                    {
                        "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"],
                        "version": ["1", "STRING"],
                        "status": ["COMPLETED", "STRING"]
                    }
                ],
                "sources.injuries": [
                    {
                        "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"]
                    }
                ]
            },
            "expected_output": [
                {
                    "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"],
                    "version": ["1", "STRING"],
                    "status": ["COMPLETED", "STRING"]
                }
            ]
        }
        final_ctes = queries_to_test()
        expected_output = f"WITH sources_aims_events AS (\nSELECT\n\tFROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA==') AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`\n),\nsources_injuries AS (\nSELECT\n\tFROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA==') AS `submission_id`\n),\nexpected_output AS (\nSELECT\n\tFROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA==') AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`\n),\nactual_output AS (\nSELECT `submission_id`,`version`,`status` FROM (\nSELECT * FROM sources_aims_events AS a INNER JOIN sources_injuries AS b ON a.submission_id = b.submission_id\n)),\n{final_ctes}"
        self.maxDiff = None
        self.assertEqual(build_test_to_submit(test, query_to_replace), expected_output)

    
    def test_multiple_table_input_with_json(self):
        """Test for 'Multiple Table Input with JSON'"""
        query_to_replace = "SELECT * FROM `test-project.sources.aims_events` AS a INNER JOIN `test-project.sources.injuries` AS b ON a.submission_id = b.submission_id"
        test = {
            "input_data": {
                "sources.aims_events": [
                    {
                        "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"],
                        "version": ["1", "STRING"],
                        "equipment_involved": ["{'key1': 'value1', 'key2': {'key3': 'value3'}}", "JSON"]
                    }
                ],
                "sources.injuries": [
                    {
                        "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"]
                    }
                ]
            },
            "expected_output": [
                {
                    "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"],
                    "version": ["1", "STRING"],
                    "equipment_involved": ["{'key1': 'value1', 'key2': {'key3': 'value3'}}", "JSON"]
                }
            ]
        }
        final_ctes = queries_to_test()
        expected_output = f"WITH sources_aims_events AS (\nSELECT\n\tFROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA==') AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tJSON_OBJECT('key1', 'value1', 'key2', JSON_OBJECT('key3', 'value3')) AS `equipment_involved`\n),\nsources_injuries AS (\nSELECT\n\tFROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA==') AS `submission_id`\n),\nexpected_output AS (\nSELECT\n\tFROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA==') AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tJSON_OBJECT('key1', 'value1', 'key2', JSON_OBJECT('key3', 'value3')) AS `equipment_involved`\n),\nactual_output AS (\nSELECT `submission_id`,`version`,`equipment_involved` FROM (\nSELECT * FROM sources_aims_events AS a INNER JOIN sources_injuries AS b ON a.submission_id = b.submission_id\n)),\n{final_ctes}"
        self.maxDiff = None
        self.assertEqual(build_test_to_submit(test, query_to_replace), expected_output)
    

    def test_multiple_table_input_with_geography(self):
        """Test for 'Multiple Table Input with Geography'"""
        query_to_replace = "SELECT * FROM `test-project.sources.aims_events` AS a INNER JOIN `test-project.sources.injuries` AS b ON a.submission_id = b.submission_id"
        test = {
            "input_data": {
                "sources.aims_events": [
                    {
                        "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"],
                        "version": ["1", "STRING"],
                        "injury_location": ["POINT(-0.349498 51.48198)", "GEOGRAPHY"]
                    }
                ],
                "sources.injuries": [
                    {
                        "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"]
                    }
                ]
            },
            "expected_output": [
                {
                    "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"],
                    "version": ["1", "STRING"],
                    "injury_location": ["POINT(-0.349498 51.48198)", "GEOGRAPHY"]
                }
            ]
        }
        final_ctes = queries_to_test()
        expected_output = f"WITH sources_aims_events AS (\nSELECT\n\tFROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA==') AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tST_GEOGFROMTEXT('POINT(-0.349498 51.48198)') AS `injury_location`\n),\nsources_injuries AS (\nSELECT\n\tFROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA==') AS `submission_id`\n),\nexpected_output AS (\nSELECT\n\tFROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA==') AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tST_GEOGFROMTEXT('POINT(-0.349498 51.48198)') AS `injury_location`\n),\nactual_output AS (\nSELECT `submission_id`,`version`,`injury_location` FROM (\nSELECT * FROM sources_aims_events AS a INNER JOIN sources_injuries AS b ON a.submission_id = b.submission_id\n)),\n{final_ctes}"
        self.maxDiff = None
        self.assertEqual(build_test_to_submit(test, query_to_replace), expected_output)
    

    def test_multiple_table_input_with_invalid_geography(self):
        """Test for 'Multiple Table Input with Invalid Geography'"""
        query_to_replace = "SELECT * FROM `test-project.sources.aims_events` AS a INNER JOIN `test-project.sources.injuries` AS b ON a.submission_id = b.submission_id"
        test = {
            "input_data": {
                "sources.aims_events": [
                    {
                        "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"],
                        "version": ["1", "STRING"],
                        "injury_location": ["Random String", "GEOGRAPHY"]
                    }
                ],
                "sources.injuries": [
                    {
                        "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"]
                    }
                ]
            },
            "expected_output": [
                {
                    "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"],
                    "version": ["1", "STRING"],
                    "injury_location": ["Random String", "GEOGRAPHY"]
                }
            ]
        }
        self.assertRaises(Exception, build_test_to_submit, test, query_to_replace)
    

    def test_multiple_table_input_with_array_numeric(self):
        """Test for 'Multiple Table Input with Array Numeric'"""
        query_to_replace = "SELECT * FROM `test-project.sources.aims_events` AS a INNER JOIN `test-project.sources.injuries` AS b ON a.submission_id = b.submission_id"
        test = {
            "input_data": {
                "sources.aims_events": [
                    {
                        "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"],
                        "version": ["1", "STRING"],
                        "affected_restaurants": ["[14002, 14004, 14010, 14017]", "ARRAY<NUMERIC>"]
                    }
                ],
                "sources.injuries": [
                    {
                        "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"]
                    }
                ]
            },
            "expected_output": [
                {
                    "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"],
                    "version": ["1", "STRING"],
                    "affected_restaurants": ["[14002, 14004, 14010, 14017]", "ARRAY<NUMERIC>"]
                }
            ]
        }
        final_ctes = queries_to_test()
        expected_output = f"WITH sources_aims_events AS (\nSELECT\n\tFROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA==') AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST([SAFE_CAST(14002 AS NUMERIC), SAFE_CAST(14004 AS NUMERIC), SAFE_CAST(14010 AS NUMERIC), SAFE_CAST(14017 AS NUMERIC)] AS ARRAY<NUMERIC>) AS `affected_restaurants`\n),\nsources_injuries AS (\nSELECT\n\tFROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA==') AS `submission_id`\n),\nexpected_output AS (\nSELECT\n\tFROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA==') AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST([SAFE_CAST(14002 AS NUMERIC), SAFE_CAST(14004 AS NUMERIC), SAFE_CAST(14010 AS NUMERIC), SAFE_CAST(14017 AS NUMERIC)] AS ARRAY<NUMERIC>) AS `affected_restaurants`\n),\nactual_output AS (\nSELECT `submission_id`,`version`,`affected_restaurants` FROM (\nSELECT * FROM sources_aims_events AS a INNER JOIN sources_injuries AS b ON a.submission_id = b.submission_id\n)),\n{final_ctes}"
        self.maxDiff = None
        self.assertEqual(build_test_to_submit(test, query_to_replace), expected_output)

    
    def test_multiple_table_input_with_one_not_mocked(self):
        """Test for 'Multiple Table Input with One Unmocked'"""
        query_to_replace = "SELECT * FROM `test-project.sources.aims_events` AS a INNER JOIN `test-project.sources.injuries` AS b ON a.submission_id = b.submission_id"
        test = {
            "input_data": {
                "sources.injuries": [
                    {
                        "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"]
                    }
                ]
            },
            "expected_output": [
                {
                    "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"],
                    "version": ["1", "STRING"],
                    "affected_restaurants": ["[14002, 14004, 14010, 14017]", "ARRAY<NUMERIC>"]
                }
            ]
        }
        self.assertRaises(Exception, build_test_to_submit, test, query_to_replace)


if __name__ == "__main__":
    unittest.main()
