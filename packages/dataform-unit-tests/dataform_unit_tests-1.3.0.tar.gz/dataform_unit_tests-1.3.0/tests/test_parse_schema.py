import unittest

from src.dataform_unit_testing.unit_test_parser import parse_schema

class TestParseSchema(unittest.TestCase):
    def test_simple_schema(self):
        """Test for 'Simple Schema'"""
        schema = [{'name': 'submission_id', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'version', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'status', 'type': 'STRING', 'mode': 'NULLABLE'}]
        expected_output = {"submission_id": "STRING", "version": "STRING", "status": "STRING"}
        self.assertEqual(parse_schema(schema), expected_output)

    
    def test_schema_with_arrays(self):
        """Test for 'Schemas with Arrays'"""
        schema = [{'name': 'submission_id', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'version', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'status', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'injury_type', 'type': 'STRING', 'mode': 'REPEATED'}]
        expected_output = {"submission_id": "STRING", "version": "STRING", "status": "STRING", "injury_type": "ARRAY<STRING>"}
        self.assertEqual(parse_schema(schema), expected_output)

    
    def test_schema_with_records(self):
        """Test for 'Schemas with Records'"""
        schema = [
            {'name': 'submission_id', 'type': 'STRING', 'mode': 'NULLABLE'}, 
            {'name': 'version', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'status', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'injured', 'type': 'RECORD', 'mode': 'REPEATED', "fields": [
                {'name': 'injured_individual', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'injured_status', 'type': 'BOOLEAN', 'mode': 'NULLABLE'}
            ]}
        ]
        expected_output = {"submission_id": "STRING", "version": "STRING", "status": "STRING", "injured": "RECORD", "injured.injured_individual": "STRING", "injured.injured_status": "BOOLEAN"}
        self.assertEqual(parse_schema(schema), expected_output)

    
    def test_schema_with_nested_records(self):
        """Test for 'Schemas with Nested Records'"""
        schema = [
            {'name': 'submission_id', 'type': 'STRING', 'mode': 'NULLABLE'}, 
            {'name': 'version', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'status', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'injured', 'type': 'RECORD', 'mode': 'REPEATED', "fields": [
                {'name': 'injured_individual', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'injured_status', 'type': 'BOOLEAN', 'mode': 'NULLABLE'},
                {'name': 'injuries', 'type': 'RECORD', 'mode': 'REPEATED', "fields": [
                    {'name': 'injury_1', 'type': 'STRING', 'mode': 'NULLABLE'},
                    {'name': 'injury_2', 'type': 'STRING', 'mode': 'NULLABLE'}
                ]}
            ]}
        ]
        expected_output = {
            "submission_id": "STRING",
            "version": "STRING",
            "status": "STRING",
            "injured": "RECORD",
            "injured.injured_individual": "STRING",
            "injured.injured_status": "BOOLEAN",
            "injured.injuries": "RECORD",
            "injured.injuries.injury_1": "STRING",
            "injured.injuries.injury_2": "STRING"
        }
        self.assertEqual(parse_schema(schema), expected_output)

    
    def test_schema_with_array_and_nested_records(self):
        """Test for 'Schemas with an Array and Nested Records'"""
        schema = [
            {'name': 'submission_id', 'type': 'STRING', 'mode': 'NULLABLE'}, 
            {'name': 'version', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'status', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'injured', 'type': 'RECORD', 'mode': 'REPEATED', "fields": [
                {'name': 'injured_individual', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'injured_status', 'type': 'BOOLEAN', 'mode': 'NULLABLE'},
                {'name': 'injuries', 'type': 'RECORD', 'mode': 'REPEATED', "fields": [
                    {'name': 'injury_1', 'type': 'STRING', 'mode': 'NULLABLE'},
                    {'name': 'injury_2', 'type': 'STRING', 'mode': 'NULLABLE'}
                ]}
            ]},
            {'name': 'contributing_factors', 'type': 'STRING', 'mode': 'REPEATED'}
        ]
        expected_output = {
            "submission_id": "STRING",
            "version": "STRING",
            "status": "STRING",
            "injured": "RECORD",
            "injured.injured_individual": "STRING",
            "injured.injured_status": "BOOLEAN",
            "injured.injuries": "RECORD",
            "injured.injuries.injury_1": "STRING",
            "injured.injuries.injury_2": "STRING",
            "contributing_factors": "ARRAY<STRING>"
        }
        self.assertEqual(parse_schema(schema), expected_output)
    

    def test_schema_with_nested_records_and_float(self):
        """Test for 'Schemas with Nested Records and Float Datatype'"""
        schema = [
            {'name': 'submission_id', 'type': 'STRING', 'mode': 'NULLABLE'}, 
            {'name': 'version', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'status', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'injured', 'type': 'RECORD', 'mode': 'REPEATED', "fields": [
                {'name': 'injured_individual', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'injured_status', 'type': 'BOOLEAN', 'mode': 'NULLABLE'},
                {'name': 'injuries', 'type': 'RECORD', 'mode': 'REPEATED', "fields": [
                    {'name': 'injury_1', 'type': 'STRING', 'mode': 'NULLABLE'},
                    {'name': 'injury_2', 'type': 'STRING', 'mode': 'NULLABLE'},
                    {'name': 'injury_factor', 'type': 'FLOAT', 'mode': 'NULLABLE'}
                ]}
            ]}
        ]
        expected_output = {
            "submission_id": "STRING",
            "version": "STRING",
            "status": "STRING",
            "injured": "RECORD",
            "injured.injured_individual": "STRING",
            "injured.injured_status": "BOOLEAN",
            "injured.injuries": "RECORD",
            "injured.injuries.injury_1": "STRING",
            "injured.injuries.injury_2": "STRING",
            "injured.injuries.injury_factor": "FLOAT64"
        }
        self.assertEqual(parse_schema(schema), expected_output)


if __name__ == "__main__":
    unittest.main()
