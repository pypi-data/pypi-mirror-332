import unittest
import json

from src.dataform_unit_testing.unit_test_extractor import get_model_to_test

COMPILATION_RESULT = "projects/preview-dataform-52eca37e/locations/europe-west2/repositories/nandos-data-transformations/compilationResults/59c243b9-97b8-4677-b9e3-cedaed5618b9"

class TestGetModelToTest(unittest.TestCase):
    def test_model_exists(self):
        """Test for 'Model Exists'"""
        with open("sample_unit_tests/test_sample_unit_test_1.json") as f:
            contents = f.read()
            to_json = json.loads(contents)

        model_exists, model_to_test = get_model_to_test(to_json, COMPILATION_RESULT)
        self.assertTrue(model_exists)

    
    def test_model_not_exists(self):
        """Test for 'Model Doesn't Exist'"""
        with open("sample_unit_tests/test_sample_unit_test_missing_model.json") as f:
            contents = f.read()
            to_json = json.loads(contents)

        model_exists, model_to_test = get_model_to_test(to_json, COMPILATION_RESULT)
        self.assertFalse(model_exists)


if __name__ == "__main__":
    unittest.main()
