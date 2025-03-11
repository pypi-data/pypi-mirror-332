import unittest

from src.dataform_unit_testing.sql_unit_test_builder import handle_geography_datatype

class TestHandleJGeographyDatatype(unittest.TestCase):
    def test_point_string(self):
        """Test for 'POINT String'"""
        geo_value = "POINT(-0.349498 51.48198)"
        expected_output = "ST_GEOGFROMTEXT('POINT(-0.349498 51.48198)')"
        self.assertEqual(handle_geography_datatype(geo_value), expected_output)


    def test_linestring_string(self):
        """Test for 'LineString String'"""
        geo_value = "LINESTRING(-0.349498 51.48198, -0.359498 51.48198)"
        expected_output = "ST_GEOGFROMTEXT('LINESTRING(-0.349498 51.48198, -0.359498 51.48198)')"
        self.assertEqual(handle_geography_datatype(geo_value), expected_output)

    
    def test_polygon_string(self):
        """Test for 'Polygon String'"""
        geo_value = "POLYGON((0 0, 2 2, 2 0, 0 0), (2 2, 3 4, 2 4, 2 2))"
        expected_output = "ST_GEOGFROMTEXT('POLYGON((0 0, 2 2, 2 0, 0 0), (2 2, 3 4, 2 4, 2 2))')"
        self.assertEqual(handle_geography_datatype(geo_value), expected_output)
    

    def test_multipoint_string(self):
        """Test for 'MultiPoint String'"""
        geo_value = "MULTIPOINT(0 32, 123 9, 48 67)"
        expected_output = "ST_GEOGFROMTEXT('MULTIPOINT(0 32, 123 9, 48 67)')"
        self.assertEqual(handle_geography_datatype(geo_value), expected_output)
    

    def test_multilinestring_string(self):
        """Test for 'MultiLineString String'"""
        geo_value = "MULTILINESTRING((2 2, 3 4), (5 6, 7 7))"
        expected_output = "ST_GEOGFROMTEXT('MULTILINESTRING((2 2, 3 4), (5 6, 7 7))')"
        self.assertEqual(handle_geography_datatype(geo_value), expected_output)
    

    def test_multipolygon_string(self):
        """Test for 'MultiPolygon String'"""
        geo_value = "MULTIPOLYGON(((0 -1, 1 0, 1 1, 0 -1)), ((0 0, 2 2, 3 0, 0 0), (2 2, 3 4, 2 4, 1 9)))"
        expected_output = "ST_GEOGFROMTEXT('MULTIPOLYGON(((0 -1, 1 0, 1 1, 0 -1)), ((0 0, 2 2, 3 0, 0 0), (2 2, 3 4, 2 4, 1 9)))')"
        self.assertEqual(handle_geography_datatype(geo_value), expected_output)
    

    def test_geometrycollection_string(self):
        """Test for 'GeometryCollection String'"""
        geo_value = "GEOMETRYCOLLECTION(MULTIPOINT(-1 2, 0 12), LINESTRING(-2 4, 0 6))"
        expected_output = "ST_GEOGFROMTEXT('GEOMETRYCOLLECTION(MULTIPOINT(-1 2, 0 12), LINESTRING(-2 4, 0 6))')"
        self.assertEqual(handle_geography_datatype(geo_value), expected_output)
    

    def test_non_geo_string(self):
        """Test for 'Non Geo String'"""
        geo_value = "Random String"
        self.assertRaises(Exception, handle_geography_datatype, geo_value)
    

    def test_badpoint_string(self):
        """Test for 'Bad POINT String'"""
        geo_value = "POINTPOINT(-0.349498 51.48198)"
        self.assertRaises(Exception, handle_geography_datatype, geo_value)
    

    def test_badpolygon_string(self):
        """Test for 'Bad POLYGON String'"""
        geo_value = "POLYGON POINT((0 0, 2 2, 2 0, 0 0), (2 2, 3 4, 2 4, 2 2))"
        self.assertRaises(Exception, handle_geography_datatype, geo_value)

    
if __name__ == "__main__":
    unittest.main()
