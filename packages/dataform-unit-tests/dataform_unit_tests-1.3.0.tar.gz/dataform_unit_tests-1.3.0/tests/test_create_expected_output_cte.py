import unittest

from src.dataform_unit_testing.sql_unit_test_builder import create_expected_output_cte

class TestCreateExpectedOutputCTE(unittest.TestCase):
    def test_build_single_row(self):
        """Test for 'Build Single Row'"""
        test = {
            "expected_output": [
                {
                    "submission_id": ["NKHWN-SHTJ", "STRING"],
                    "version": ["1", "STRING"],
                    "status": ["COMPLETED", "STRING"]
                }
            ]
        }
        expected_output = "expected_output AS (\nSELECT\n\tSAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`\n),"
        self.assertEqual(create_expected_output_cte(test), expected_output)

    
    def test_build_multiple_rows(self):
        """Test for 'Build Multiple Rows'"""
        test = {
            "expected_output": [
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
        }
        expected_output = "expected_output AS (\nSELECT\n\tSAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`\nUNION ALL\nSELECT\n\tSAFE_CAST('NKHWN-SHTK' AS STRING) AS `submission_id`,\n\tSAFE_CAST('2' AS STRING) AS `version`,\n\tSAFE_CAST('DRAFT' AS STRING) AS `status`\n),"
        self.assertEqual(create_expected_output_cte(test), expected_output)

    
    def test_build_single_row_with_record(self):
        """Test for 'Build Single Row with Record'"""
        test = {
            "expected_output": [
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
        }
        expected_output = "expected_output AS (\nSELECT\n\tSAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`,\n\tARRAY<STRUCT<`injury` STRING,`injured_age` STRING>>[(SAFE_CAST('Broken arm' AS STRING),SAFE_CAST('24' AS STRING))] AS `injured`\n),"
        self.assertEqual(create_expected_output_cte(test), expected_output)

    
    def test_build_single_row_with_nested_records(self):
        """Test for 'Build Single Row with Nested Records'"""
        test = {
            "expected_output": [
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
        }
        expected_output = "expected_output AS (\nSELECT\n\tSAFE_CAST('NKHWN-SHTJ' AS STRING) AS `submission_id`,\n\tSAFE_CAST('1' AS STRING) AS `version`,\n\tSAFE_CAST('COMPLETED' AS STRING) AS `status`,\n\tARRAY<STRUCT<`injury` STRING,`injured_age` STRING,`injured` ARRAY<STRUCT<`injury_type` STRING,`injury_location` STRING>>>>[(SAFE_CAST('Broken arm' AS STRING),SAFE_CAST('24' AS STRING),[(SAFE_CAST('Nandoca' AS STRING),SAFE_CAST('Kitchen' AS STRING))])] AS `injured`\n),"
        self.assertEqual(create_expected_output_cte(test), expected_output)


if __name__ == "__main__":
    unittest.main()
