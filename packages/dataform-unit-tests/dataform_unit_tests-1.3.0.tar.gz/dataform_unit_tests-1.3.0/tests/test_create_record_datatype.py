import unittest

from src.dataform_unit_testing.sql_unit_test_builder import create_record_datatype

class TestCreateRecordDatatype(unittest.TestCase):
    def test_single_row_record(self):
        """Test for 'Single Row Record'"""
        record = [
                    {
                        "injured_individual": ["Nandoca", "STRING"],
                        "injured_age": ["24", "STRING"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<`injured_individual` STRING,`injured_age` STRING>>[(SAFE_CAST('Nandoca' AS STRING),SAFE_CAST('24' AS STRING))]"
        self.assertEqual(create_record_datatype(record), expected_output)
    

    def test_multiple_rows_record(self):
        """Test for 'Multiple Rows Record'"""
        record = [
                    {
                        "injured_individual": ["Nandoca", "STRING"],
                        "injured_age": ["24", "STRING"]
                    },
                    {
                        "injured_individual": ["Customer", "STRING"],
                        "injured_age": ["25", "STRING"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<`injured_individual` STRING,`injured_age` STRING>>[(SAFE_CAST('Nandoca' AS STRING),SAFE_CAST('24' AS STRING)), (SAFE_CAST('Customer' AS STRING),SAFE_CAST('25' AS STRING))]"
        self.assertEqual(create_record_datatype(record), expected_output)

    
    def test_single_row_nested_record(self):
        """Test for 'Single Row Nested Record'"""
        record = [
                    {
                        "injured_individual": ["Nandoca", "STRING"],
                        "injured_age": ["24", "STRING"],
                        "injuries": [[
                            {
                                "injury_1": ["Broken arm", "STRING"],
                                "injury_2": ["Bruised leg", "STRING"]
                            }
                        ], "RECORD"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<`injured_individual` STRING,`injured_age` STRING,`injuries` ARRAY<STRUCT<`injury_1` STRING,`injury_2` STRING>>>>[(SAFE_CAST('Nandoca' AS STRING),SAFE_CAST('24' AS STRING),[(SAFE_CAST('Broken arm' AS STRING),SAFE_CAST('Bruised leg' AS STRING))])]"
        self.assertEqual(create_record_datatype(record), expected_output)
    

    def test_multiple_rows_nested_record(self):
        """Test for 'Multiple Rows Nested Record'"""
        record = [
                    {
                        "injured_individual": ["Nandoca", "STRING"],
                        "injured_age": ["24", "STRING"],
                        "injuries": [[
                            {
                                "injury_1": ["Broken arm", "STRING"],
                                "injury_2": ["Bruised leg", "STRING"]
                            }
                        ], "RECORD"]
                    },
                    {
                        "injured_individual": ["Customer", "STRING"],
                        "injured_age": ["24", "STRING"],
                        "injuries": [[
                            {
                                "injury_1": ["Broken leg", "STRING"],
                                "injury_2": ["Bruised arm", "STRING"]
                            }
                        ], "RECORD"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<`injured_individual` STRING,`injured_age` STRING,`injuries` ARRAY<STRUCT<`injury_1` STRING,`injury_2` STRING>>>>[(SAFE_CAST('Nandoca' AS STRING),SAFE_CAST('24' AS STRING),[(SAFE_CAST('Broken arm' AS STRING),SAFE_CAST('Bruised leg' AS STRING))]), (SAFE_CAST('Customer' AS STRING),SAFE_CAST('24' AS STRING),[(SAFE_CAST('Broken leg' AS STRING),SAFE_CAST('Bruised arm' AS STRING))])]"
        self.assertEqual(create_record_datatype(record), expected_output)

    
    def test_escape_single_quote(self):
        """Test for 'Escape Single Quote'"""
        record = [
                    {
                        "injured_individual": ["Nandoca's", "STRING"],
                        "injured_age": ["24", "STRING"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<`injured_individual` STRING,`injured_age` STRING>>[(SAFE_CAST('Nandoca\\'s' AS STRING),SAFE_CAST('24' AS STRING))]"
        self.assertEqual(create_record_datatype(record), expected_output)
    

    def test_bytes(self):
        """Test for 'Bytes'"""
        record = [
                    {
                        "injured_individual": ["Nandoca's", "STRING"],
                        "injury_type_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<`injured_individual` STRING,`injury_type_id` BYTES>>[(SAFE_CAST('Nandoca\\'s' AS STRING),FROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA=='))]"
        self.assertEqual(create_record_datatype(record), expected_output)
    

    def test_nested_json(self):
        """Test for 'Nested JSON'"""
        record = [
                    {
                        "injured_individual": ["Nandoca's", "STRING"],
                        "equipment_involved": ["{'key1': 'value1', 'key2': {'key3': 'value3'}}", "JSON"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<`injured_individual` STRING,`equipment_involved` JSON>>[(SAFE_CAST('Nandoca\\'s' AS STRING),JSON_OBJECT('key1', 'value1', 'key2', JSON_OBJECT('key3', 'value3')))]"
        self.assertEqual(create_record_datatype(record), expected_output)
    

    def test_geography(self):
        """Test for 'Geography'"""
        record = [
                    {
                        "injured_individual": ["Nandoca's", "STRING"],
                        "injury_location": ["POINT(-0.349498 51.48198)", "GEOGRAPHY"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<`injured_individual` STRING,`injury_location` GEOGRAPHY>>[(SAFE_CAST('Nandoca\\'s' AS STRING),ST_GEOGFROMTEXT('POINT(-0.349498 51.48198)'))]"
        self.assertEqual(create_record_datatype(record), expected_output)
    

    def test_single_row_record_with_array_numeric(self):
        """Test for 'Single Row Record with Array Numeric'"""
        record = [
                    {
                        "affected_restaurants": ["[14002, 14004, 14010, 14017]", "ARRAY<NUMERIC>"],
                        "random_column": ["test", "STRING"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<`affected_restaurants` ARRAY<NUMERIC>,`random_column` STRING>>[(SAFE_CAST([SAFE_CAST(14002 AS NUMERIC), SAFE_CAST(14004 AS NUMERIC), SAFE_CAST(14010 AS NUMERIC), SAFE_CAST(14017 AS NUMERIC)] AS ARRAY<NUMERIC>),SAFE_CAST('test' AS STRING))]"
        self.maxDiff = None
        self.assertEqual(create_record_datatype(record), expected_output)


    def test_four_nested_records(self):
        """Test for 'Four Nested Record"""
        record = [
            {
                "foo": ["bar", "STRING"],
                "closures": [[
                {
                    "updated_time": ["2025-02-27 00:00:01.850000 UTC", "TIMESTAMP"],
                    "value": [[
                    {
                        "closure_id": ["1", "STRING"],
                        "open_times": [[{
                            "from": [None, "STRING"],
                            "until": [None, "STRING"]
                        }], "RECORD"],
                        "description": ["Multi day closure", "STRING"],
                        "channel": ["EAT_IN", "STRING"],
                        "type": ["SPECIAL_HOURS", "STRING"],
                        "reason": ["CHRISTMAS_PERIOD", "STRING"],
                        "effective_time": ["2024-12-23", "DATE"],
                        "expiry_time": ["2024-12-25", "DATE"]
                    },
                    {
                        "closure_id": ["2", "STRING"],
                        "open_times": [[{
                            "from": [None, "STRING"],
                            "until": [None, "STRING"]
                        }], "RECORD"],
                        "description": ["Single day closure", "STRING"],
                        "channel": ["EAT_IN", "STRING"],
                        "type": ["SPECIAL_HOURS", "STRING"],
                        "reason": ["CHRISTMAS_PERIOD", "STRING"],
                        "effective_time": ["2024-01-01", "DATE"],
                        "expiry_time": ["2024-01-01", "DATE"]
                    }
                    ], "RECORD"]
                }
                ], "RECORD"]
            }
            ]
        expected_output = "ARRAY<STRUCT<`foo` STRING,`closures` ARRAY<STRUCT<`updated_time` TIMESTAMP,`value` ARRAY<STRUCT<`closure_id` STRING,`open_times` ARRAY<STRUCT<`from` STRING,`until` STRING>>,`description` STRING,`channel` STRING,`type` STRING,`reason` STRING,`effective_time` DATE,`expiry_time` DATE>>>>>>[(SAFE_CAST('bar' AS STRING),[(SAFE_CAST('2025-02-27 00:00:01.850000 UTC' AS TIMESTAMP),[(SAFE_CAST('1' AS STRING),[(SAFE_CAST(NULL AS STRING),SAFE_CAST(NULL AS STRING))],SAFE_CAST('Multi day closure' AS STRING),SAFE_CAST('EAT_IN' AS STRING),SAFE_CAST('SPECIAL_HOURS' AS STRING),SAFE_CAST('CHRISTMAS_PERIOD' AS STRING),SAFE_CAST('2024-12-23' AS DATE),SAFE_CAST('2024-12-25' AS DATE)), (SAFE_CAST('2' AS STRING),[(SAFE_CAST(NULL AS STRING),SAFE_CAST(NULL AS STRING))],SAFE_CAST('Single day closure' AS STRING),SAFE_CAST('EAT_IN' AS STRING),SAFE_CAST('SPECIAL_HOURS' AS STRING),SAFE_CAST('CHRISTMAS_PERIOD' AS STRING),SAFE_CAST('2024-01-01' AS DATE),SAFE_CAST('2024-01-01' AS DATE))])])]"
        self.maxDiff = None
        self.assertEqual(create_record_datatype(record), expected_output)


if __name__ == "__main__":
    unittest.main()
