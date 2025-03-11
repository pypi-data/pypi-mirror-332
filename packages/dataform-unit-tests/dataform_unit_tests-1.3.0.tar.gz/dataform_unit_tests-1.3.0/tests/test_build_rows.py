import unittest

from src.dataform_unit_testing.sql_unit_test_builder import build_rows

class TestBuildRows(unittest.TestCase):
    def test_build_single_row(self):
        """Test for 'Build Single Row'"""
        rows_to_build = [
            {
                "submission_id": ["NKHWN-SHTJ", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"]
            }
        ]
        expected_output = "SAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`"
        self.assertEqual(build_rows(rows_to_build), expected_output)

    
    def test_build_multiple_rows(self):
        """Test for 'Build Multiple Rows'"""
        rows_to_build = [
            {
                "submission_id": ["NKHWN-SHTJ", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"]
            },
            {
                "submission_id": ["NKHWN-SHTK", "STRING"],
                "version": ["2", "STRING"],
                "status": ["DRAFT", "STRING"]
            }
        ]
        expected_output = "SAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`\nUNION ALL\nSELECT\n\tSAFE_CAST('NKHWN-SHTK' AS STRING) AS `submission_id`,\n\tSAFE_CAST('2' AS STRING) AS `version`,\n\tSAFE_CAST('DRAFT' AS STRING) AS `status`"
        self.assertEqual(build_rows(rows_to_build), expected_output)

    
    def test_build_single_row_with_record(self):
        """Test for 'Build Single Row with Record'"""
        rows_to_build = [
            {
                "submission_id": ["NKHWN-SHTJ", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"],
                "injured": [[
                    {
                        "injury": ["Broken arm", "STRING"],
                        "injured_age": ["24", "STRING"]
                    }
                ], "RECORD"]
            }
        ]
        expected_output = "SAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`,\n\tARRAY<STRUCT<`injury` STRING,`injured_age` STRING>>[(SAFE_CAST('Broken arm' AS STRING),SAFE_CAST('24' AS STRING))] AS `injured`"
        self.assertEqual(build_rows(rows_to_build), expected_output)

    
    def test_build_single_row_with_nested_records(self):
        """Test for 'Build Single Row with Nested Records'"""
        rows_to_build = [
            {
                "submission_id": ["NKHWN-SHTJ", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"],
                "injured": [[
                    {
                        "injury": ["Broken arm", "STRING"],
                        "injured_age": ["24", "STRING"],
                        "injured": [[
                            {
                                "injury_type": ["Nandoca", "STRING"],
                                "injury_location": ["Kitchen", "STRING"]
                            }
                        ], "RECORD"]
                    }
                ], "RECORD"]
            }
        ]
        expected_output = "SAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`,\n\tARRAY<STRUCT<`injury` STRING,`injured_age` STRING,`injured` ARRAY<STRUCT<`injury_type` STRING,`injury_location` STRING>>>>[(SAFE_CAST('Broken arm' AS STRING),SAFE_CAST('24' AS STRING),[(SAFE_CAST('Nandoca' AS STRING),SAFE_CAST('Kitchen' AS STRING))])] AS `injured`"
        self.assertEqual(build_rows(rows_to_build), expected_output)


    def test_build_multiple_rows_with_nested_records(self):
        """Test for 'Build Multiple Rows with Nested Records'"""
        rows_to_build = [
            {
                "submission_id": ["NKHWN-SHTJ", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"],
                "injured": [[
                    {
                        "injury": ["Broken arm", "STRING"],
                        "injured_age": ["24", "STRING"],
                        "injured": [[
                            {
                                "injury_type": ["Nandoca", "STRING"],
                                "injury_location": ["Kitchen", "STRING"]
                            }
                        ], "RECORD"]
                    }
                ], "RECORD"]
            },
            {
                "submission_id": ["NKHWN-SHTK", "STRING"],
                "version": ["2", "STRING"],
                "status": ["DRAFT", "STRING"],
                "injured": [[
                    {
                        "injury": ["Broken leg", "STRING"],
                        "injured_age": ["24", "STRING"],
                        "injured": [[
                            {
                                "injury_type": ["Nandoca", "STRING"],
                                "injury_location": ["Kitchen", "STRING"]
                            }
                        ], "RECORD"]
                    }
                ], "RECORD"]
            }
        ]
        expected_output = "SAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`,\n\tARRAY<STRUCT<`injury` STRING,`injured_age` STRING,`injured` ARRAY<STRUCT<`injury_type` STRING,`injury_location` STRING>>>>[(SAFE_CAST('Broken arm' AS STRING),SAFE_CAST('24' AS STRING),[(SAFE_CAST('Nandoca' AS STRING),SAFE_CAST('Kitchen' AS STRING))])] AS `injured`\nUNION ALL\nSELECT\n\tSAFE_CAST('NKHWN-SHTK' AS STRING) AS `submission_id`,\n\tSAFE_CAST('2' AS STRING) AS `version`,\n\tSAFE_CAST('DRAFT' AS STRING) AS `status`,\n\tARRAY<STRUCT<`injury` STRING,`injured_age` STRING,`injured` ARRAY<STRUCT<`injury_type` STRING,`injury_location` STRING>>>>[(SAFE_CAST('Broken leg' AS STRING),SAFE_CAST('24' AS STRING),[(SAFE_CAST('Nandoca' AS STRING),SAFE_CAST('Kitchen' AS STRING))])] AS `injured`"
        self.assertEqual(build_rows(rows_to_build), expected_output)


    def test_escape_single_quote(self):
        """Test for 'Escape Single Quote'"""
        rows_to_build = [
            {
                "submission_id": ["NKHWN'S", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"]
            }
        ]
        expected_output = "SAFE_CAST('NKHWN\\'S' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`"
        self.assertEqual(build_rows(rows_to_build), expected_output)


    def test_build_single_row_with_bytes(self):
        """Test for 'Build Single Row with Bytes'"""
        rows_to_build = [
            {
                "submission_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"]
            }
        ]
        expected_output = "FROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA==') AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`"
        self.assertEqual(build_rows(rows_to_build), expected_output)
    

    def test_build_single_row_with_record_and_bytes(self):
        """Test for 'Build Single Row with Record and Bytes'"""
        rows_to_build = [
            {
                "submission_id": ["NKHWN-SHTJ", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"],
                "injured": [[
                    {
                        "injury": ["Broken arm", "STRING"],
                        "injury_type_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"]
                    }
                ], "RECORD"]
            }
        ]
        expected_output = "SAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`,\n\tARRAY<STRUCT<`injury` STRING,`injury_type_id` BYTES>>[(SAFE_CAST('Broken arm' AS STRING),FROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA=='))] AS `injured`"
        self.assertEqual(build_rows(rows_to_build), expected_output)

    
    def test_build_single_row_with_record_and_json(self):
        """Test for 'Build Single Row with Record and JSON'"""
        rows_to_build = [
            {
                "submission_id": ["NKHWN-SHTJ", "STRING"],
                "version": ["1", "STRING"],
                "status": ["COMPLETED", "STRING"],
                "injured": [[
                    {
                        "injury": ["Broken arm", "STRING"],
                        "equipment_involved": ["{'key1': 'value1', 'key2': {'key3': 'value3'}}", "JSON"]
                    }
                ], "RECORD"]
            }
        ]
        expected_output = "SAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`,\n\tARRAY<STRUCT<`injury` STRING,`equipment_involved` JSON>>[(SAFE_CAST('Broken arm' AS STRING),JSON_OBJECT('key1', 'value1', 'key2', JSON_OBJECT('key3', 'value3')))] AS `injured`"
        self.assertEqual(build_rows(rows_to_build), expected_output)
    

    def test_build_single_row_with_record_and_geography(self):
        """Test for 'Build Single Row with Record and Geography'"""
        rows_to_build = [
            {
                "submission_id": ["NKHWN-SHTJ", "STRING"],
                "version": ["1", "STRING"],
                "injury_location": ["POINT(-0.349498 51.48198)", "GEOGRAPHY"],
                "injured": [[
                    {
                        "injury": ["Broken arm", "STRING"],
                        "equipment_involved": ["{'key1': 'value1', 'key2': {'key3': 'value3'}}", "JSON"]
                    }
                ], "RECORD"]
            }
        ]
        expected_output = "SAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tST_GEOGFROMTEXT('POINT(-0.349498 51.48198)') AS `injury_location`,\n\tARRAY<STRUCT<`injury` STRING,`equipment_involved` JSON>>[(SAFE_CAST('Broken arm' AS STRING),JSON_OBJECT('key1', 'value1', 'key2', JSON_OBJECT('key3', 'value3')))] AS `injured`"
        self.assertEqual(build_rows(rows_to_build), expected_output)
    

    def test_build_single_row_with_record_and_array_numeric(self):
        """Test for 'Build Single Row with Record and Array Numeric'"""
        rows_to_build = [
            {
                "submission_id": ["NKHWN-SHTJ", "STRING"],
                "version": ["1", "STRING"],
                "affected_restaurants": ["[14002, 14004, 14010, 14017]", "ARRAY<NUMERIC>"],
                "injured": [[
                    {
                        "injury": ["Broken arm", "STRING"],
                        "equipment_involved": ["{'key1': 'value1', 'key2': {'key3': 'value3'}}", "JSON"]
                    }
                ], "RECORD"]
            }
        ]
        expected_output = "SAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST([SAFE_CAST(14002 AS NUMERIC), SAFE_CAST(14004 AS NUMERIC), SAFE_CAST(14010 AS NUMERIC), SAFE_CAST(14017 AS NUMERIC)] AS ARRAY<NUMERIC>) AS `affected_restaurants`,\n\tARRAY<STRUCT<`injury` STRING,`equipment_involved` JSON>>[(SAFE_CAST('Broken arm' AS STRING),JSON_OBJECT('key1', 'value1', 'key2', JSON_OBJECT('key3', 'value3')))] AS `injured`"
        self.assertEqual(build_rows(rows_to_build), expected_output)


if __name__ == "__main__":
    unittest.main()
