"""
Tests for the Country module.
"""

import unittest
from country_state_city import Country


class TestCountry(unittest.TestCase):
    def setUp(self):
        # Set up test cases
        self.country_codes = ["US", "GB", "IN", "AU", "CA"]
        self.invalid_codes = ["XX", "", None]
    
    def test_get_countries(self):
        """Test retrieving all countries."""
        countries = Country.get_countries()
        self.assertIsNotNone(countries)
        self.assertIsInstance(countries, list)
        self.assertGreater(len(countries), 0)
        
        # Test that returned objects are Country instances
        for country in countries[:5]:
            self.assertIsInstance(country, Country)
            self.assertTrue(hasattr(country, 'name'))
            self.assertTrue(hasattr(country, 'iso2'))
            self.assertTrue(hasattr(country, 'flag'))
    
    def test_get_country_by_code(self):
        """Test retrieving countries by their ISO code."""
        for code in self.country_codes:
            country = Country.get_country_by_code(code)
            self.assertIsNotNone(country)
            self.assertIsInstance(country, Country)
            self.assertEqual(country.iso2, code)
            
            # Test basic country properties
            self.assertTrue(hasattr(country, 'name'))
            self.assertTrue(hasattr(country, 'iso2'))
            self.assertTrue(hasattr(country, 'flag'))
            self.assertTrue(hasattr(country, 'phone_code'))
            self.assertTrue(hasattr(country, 'currency'))
    
    def test_invalid_country_code(self):
        """Test behavior with invalid country codes."""
        for code in self.invalid_codes:
            country = Country.get_country_by_code(code)
            self.assertIsNone(country)
    
    def test_usa_properties(self):
        """Test specific properties of USA."""
        usa = Country.get_country_by_code('US')
        self.assertEqual(usa.name, "United States")
        self.assertEqual(usa.iso2, "US")
        self.assertEqual(usa.flag, "🇺🇸")
        self.assertEqual(usa.currency, "USD")
        
        # Test timezones
        self.assertGreater(len(usa.timezones), 0)
        for tz in usa.timezones:
            self.assertTrue(hasattr(tz, 'name'))
            self.assertTrue(hasattr(tz, 'gmt_offset'))
            self.assertTrue(hasattr(tz, 'gmt_offset_name'))
    
    def test_to_dict(self):
        """Test conversion to dictionary."""
        usa = Country.get_country_by_code('US')
        country_dict = usa.to_dict()
        
        self.assertIsInstance(country_dict, dict)
        self.assertEqual(country_dict['name'], "United States")
        self.assertEqual(country_dict['isoCode'], "US")
        self.assertEqual(country_dict['flag'], "🇺🇸")
        
        # Check timezones in dictionary
        self.assertIsInstance(country_dict['timezones'], list)
        if country_dict['timezones']:
            self.assertIsInstance(country_dict['timezones'][0], dict)
            self.assertTrue('zoneName' in country_dict['timezones'][0])


if __name__ == '__main__':
    unittest.main()