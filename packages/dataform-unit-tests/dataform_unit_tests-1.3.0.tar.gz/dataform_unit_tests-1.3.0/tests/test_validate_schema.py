import unittest
import json

from src.dataform_unit_testing.unit_test_parser import validate_schema

class TestValidateSchema(unittest.TestCase):
    def test_simple_unit_test(self):
        """Test for 'Simple Unit Test'"""
        with open("sample_unit_tests/test_sample_unit_test_1.json") as f:
            contents = f.read()
            to_json = json.loads(contents)

        self.assertTrue(validate_schema(to_json))
    

    def test_complex_unit_test(self):
        """Test for 'Complex Unit Test'"""
        with open("sample_unit_tests/test_sample_unit_test_2.json") as f:
            contents = f.read()
            to_json = json.loads(contents)

        self.assertTrue(validate_schema(to_json))
    

    def test_unit_test_missing_input_data_key(self):
        """Test for 'Unit Test Missing Input Data Key'"""
        with open("sample_unit_tests/test_sample_invalid_unit_test_1.json") as f:
            contents = f.read()
            to_json = json.loads(contents)

        self.assertFalse(validate_schema(to_json))
    

    def test_unit_test_invalid_input_data_format(self):
        """Test for 'Unit Test with Invalid Input Data Format'"""
        with open("sample_unit_tests/test_sample_invalid_unit_test_2.json") as f:
            contents = f.read()
            to_json = json.loads(contents)

        self.assertFalse(validate_schema(to_json))
    

    def test_unit_test_with_description_field(self):
        """Test for 'Unit Test with Description'"""
        with open("sample_unit_tests/test_sample_unit_test_3.json") as f:
            contents = f.read()
            to_json = json.loads(contents)

        self.assertTrue(validate_schema(to_json))
    

    def test_unit_test_with_description_field_missing_required_field(self):
        """Test for 'Unit Test with Description but Missing Required Field'"""
        with open("sample_unit_tests/test_sample_invalid_unit_test_3.json") as f:
            contents = f.read()
            to_json = json.loads(contents)

        self.assertFalse(validate_schema(to_json))

    
    def test_blank_table_mocked(self):
        """Test for "Unit Test with Blank Mocked Table"""
        test = {
            "name": "Test with Blank Mocked Table",
            "model_to_test": "random.model",
            "input_data": {
                "sources.injuries": [
                    {
                        "submission_id": "q4ah4e9w3/l5WQZ7cjxcJA=="
                    }
                ],
                "sources.events": None
            },
            "expected_output": [
                {
                    "submission_id": "q4ah4e9w3/l5WQZ7cjxcJA==",
                    "version": "1",
                    "affected_restaurants": "[14002, 14004, 14010, 14017]"
                }
            ]
        }

        self.assertTrue(validate_schema(test))


if __name__ == "__main__":
    unittest.main()
