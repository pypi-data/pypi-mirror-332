import unittest

from src.dataform_unit_testing.sql_unit_test_builder import check_all_tables_mocked

class TestCheckAllTablesMocked(unittest.TestCase):
    def test_single_table_input(self):
        """Test for 'Single Table Input'"""
        model_to_check = "SELECT * FROM `test-project.sources.aims_events`"
        self.assertRaises(Exception, check_all_tables_mocked, model_to_check)

    
    def test_single_table_input_mocked(self):
        """Test for 'Single Table Input Mocked'"""
        model_to_check = "SELECT * FROM sources_aims_events"
        self.assertTrue(check_all_tables_mocked(model_to_check))

    
    def test_two_table_input_one_mocked(self):
        """Test for 'Two Table Input with One Mocked'"""
        model_to_check = "SELECT * FROM sources_aims_events INNER JOIN `project-id.reporting.customer` USING (customer_id)"
        self.assertRaises(Exception, check_all_tables_mocked, model_to_check)

    
    def test_two_table_input_none_mocked(self):
        """Test for 'Two Table Input with None Mocked'"""
        model_to_check = "SELECT * FROM `project-id.sources.aims_events` INNER JOIN `project-id.reporting.customer` USING (customer_id)"
        self.assertRaises(Exception, check_all_tables_mocked, model_to_check)
    

    def test_two_table_input_both_mocked(self):
        """Test for 'Two Table Input with Both Mocked'"""
        model_to_check = "SELECT * FROM sources_aims_events INNER JOIN reporting_customer USING (customer_id)"
        self.assertTrue(check_all_tables_mocked(model_to_check))


if __name__ == "__main__":
    unittest.main()
