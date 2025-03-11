import unittest

from src.dataform_unit_testing.sql_unit_test_builder import handle_json_datatype

class TestHandleJSONDatatype(unittest.TestCase):
    def test_simple_json_string(self):
        """Test for 'Simple JSON String'"""
        json_string = "{'key1': 'value1'}"
        expected_output = "JSON_OBJECT('key1', 'value1')"
        self.assertEqual(handle_json_datatype(json_string), expected_output)

    
    def test_two_key_json_string(self):
        """Test for 'Two Key JSON String'"""
        json_string = "{'key1': 'value1', 'key2': 'value2'}"
        expected_output = "JSON_OBJECT('key1', 'value1', 'key2', 'value2')"
        self.assertEqual(handle_json_datatype(json_string), expected_output)

    
    def test_three_key_json_string(self):
        """Test for 'Three Key JSON String'"""
        json_string = "{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}"
        expected_output = "JSON_OBJECT('key1', 'value1', 'key2', 'value2', 'key3', 'value3')"
        self.assertEqual(handle_json_datatype(json_string), expected_output)

    
    def test_nested_json(self):
        """Test for 'Nested JSON String'"""
        json_string = "{'key1': 'value1', 'key2': 'value2', 'key3': {'key4': 'value4'}}"
        expected_output = "JSON_OBJECT('key1', 'value1', 'key2', 'value2', 'key3', JSON_OBJECT('key4', 'value4'))"
        self.assertEqual(handle_json_datatype(json_string), expected_output)

    
    def test_nested_json_with_nested_json(self):
        """Test for 'Nested JSON with Nested JSON String'"""
        json_string = "{'key1': 'value1', 'key2': 'value2', 'key3': {'key4': 'value4', 'key5': {'key6': 'value6'}}}"
        expected_output = "JSON_OBJECT('key1', 'value1', 'key2', 'value2', 'key3', JSON_OBJECT('key4', 'value4', 'key5', JSON_OBJECT('key6', 'value6')))"
        self.assertEqual(handle_json_datatype(json_string), expected_output)

    
    def test_json_with_text_values_using_single_quotes(self):
        """Test for 'JSON with Text Values using Single Quotes"""
        json_string = "{'key1': 'It\'s great!', 'key2': 'value2', 'key3': {'key4': 'value4', 'key5': {'key6': 'value6'}}}"
        expected_output = "JSON_OBJECT('key1', 'It\\\'s great!', 'key2', 'value2', 'key3', JSON_OBJECT('key4', 'value4', 'key5', JSON_OBJECT('key6', 'value6')))"
        self.assertEqual(handle_json_datatype(json_string), expected_output)
    

    def test_json_with_two_text_values_using_single_quotes(self):
        """Test for 'JSON with Two Text Values using Single Quotes"""
        json_string = "{'key1': 'It\'s great!', 'key2': 'value2', 'key3': {'key4': 'value4', 'key5': {'key6': 'Wasn\'t great'}}}"
        expected_output = "JSON_OBJECT('key1', 'It\\\'s great!', 'key2', 'value2', 'key3', JSON_OBJECT('key4', 'value4', 'key5', JSON_OBJECT('key6', 'Wasn\\\'t great')))"
        self.assertEqual(handle_json_datatype(json_string), expected_output)

    
    def test_json_with_double_quotes(self):
        """Test for 'JSON with Double Quotes"""
        json_string = "{\"key1\": \"It's great!\", \"key2\": \"value2\", \"key3\": {\"key4\": \"value4\", \"key5\": {\"key6\": \"Wasn't great\"}}}"
        expected_output = "JSON_OBJECT('key1', 'It\\\'s great!', 'key2', 'value2', 'key3', JSON_OBJECT('key4', 'value4', 'key5', JSON_OBJECT('key6', 'Wasn\\\'t great')))"
        self.assertEqual(handle_json_datatype(json_string), expected_output)

    
    def test_json_with_array(self):
        """Test for 'JSON with Array"""
        json_string = "{'key1': 'value1', 'key2': 'value2', 'key3': ['1', '2', '3']}"
        expected_output = "JSON_OBJECT('key1', 'value1', 'key2', 'value2', 'key3', ['1', '2', '3'])"
        self.assertEqual(handle_json_datatype(json_string), expected_output)

    
    def test_json_with_int_array(self):
        """Test for 'JSON with Integer Array"""
        json_string = "{'key1': 'value1', 'key2': 'value2', 'key3': [1, 2, 3]}"
        expected_output = "JSON_OBJECT('key1', 'value1', 'key2', 'value2', 'key3', [1, 2, 3])"
        self.assertEqual(handle_json_datatype(json_string), expected_output)

    
    def test_json_with_non_string_value(self):
        """Test for 'JSON with Non String Value"""
        json_string = "{'key1': 1, 'key2': 'value2', 'key3': [1, 2, 3]}"
        expected_output = "JSON_OBJECT('key1', 1, 'key2', 'value2', 'key3', [1, 2, 3])"
        self.assertEqual(handle_json_datatype(json_string), expected_output)

    
    def test_json_as_array(self):
        """Test for 'JSON that is an Array"""
        json_string = "[{\"displayName\":\"Coconut Gelado\",\"fulfilmentTypes\":[\"COLLECTION\",\"EAT_IN\",\"AT_TABLE\"],\"id\":\"coconut-gelado:desserts\"}]"
        expected_output = "JSON_ARRAY(JSON_OBJECT('displayName', 'Coconut Gelado', 'fulfilmentTypes', ['COLLECTION', 'EAT_IN', 'AT_TABLE'], 'id', 'coconut-gelado:desserts'))"
        self.assertEqual(handle_json_datatype(json_string), expected_output)
    

    def test_json_as_array_two_items(self):
        """Test for 'JSON that is an Array with Two Items"""
        json_string = "[{\"displayName\":\"Nando's x Fanta Wings\", \"fulfilmentTypes\":[\"DELIVERY\",\"COLLECTION\",\"EAT_IN\",\"AT_TABLE\"],\"id\":\"fanta-wings:pe-ri-pe-ri-chicken\"},{\"displayName\":\"Chicken Butterfly\", \"fulfilmentTypes\":[\"DELIVERY\",\"COLLECTION\",\"EAT_IN\",\"AT_TABLE\"],\"id\":\"chicken-butterfly:pe-ri-pe-ri-chicken\"}]"
        expected_output = "JSON_ARRAY(JSON_OBJECT('displayName', 'Nando\\\'s x Fanta Wings', 'fulfilmentTypes', ['DELIVERY', 'COLLECTION', 'EAT_IN', 'AT_TABLE'], 'id', 'fanta-wings:pe-ri-pe-ri-chicken'), JSON_OBJECT('displayName', 'Chicken Butterfly', 'fulfilmentTypes', ['DELIVERY', 'COLLECTION', 'EAT_IN', 'AT_TABLE'], 'id', 'chicken-butterfly:pe-ri-pe-ri-chicken'))"
        self.assertEqual(handle_json_datatype(json_string), expected_output)

    
if __name__ == "__main__":
    unittest.main()
