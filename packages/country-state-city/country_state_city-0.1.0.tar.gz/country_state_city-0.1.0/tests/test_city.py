"""
Tests for the City module.
"""

import unittest
from country_state_city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        # Set up test cases
        self.country_codes = ["US", "IN", "GB"]
        self.state_combinations = [
            {"country": "US", "state": "CA"},  # California, USA
            {"country": "US", "state": "NY"},  # New York, USA
            {"country": "IN", "state": "MH"},  # Maharashtra, India
            {"country": "GB", "state": "ENG"},  # England, UK
        ]
        self.invalid_combinations = [
            {"country": "US", "state": "XX"},  # Invalid state
            {"country": "XX", "state": "CA"},  # Invalid country
            {"country": "", "state": ""},      # Empty codes
            {"country": None, "state": None},  # None codes
        ]
    
    def test_get_cities(self):
        """Test retrieving all cities."""
        cities = City.get_cities()
        self.assertIsNotNone(cities)
        self.assertIsInstance(cities, list)
        self.assertGreater(len(cities), 0)
        
        # Test that returned objects are City instances
        for city in cities[:5]:
            self.assertIsInstance(city, City)
            self.assertTrue(hasattr(city, 'name'))
            self.assertTrue(hasattr(city, 'country_code'))
            self.assertTrue(hasattr(city, 'state_code'))
    
    def test_get_cities_of_state(self):
        """Test retrieving cities by country and state code."""
        for combo in self.state_combinations:
            cities = City.get_cities_of_state(combo["country"], combo["state"])
            self.assertIsNotNone(cities)
            self.assertIsInstance(cities, list)
            self.assertGreater(len(cities), 0)
            
            # Verify all cities belong to the specified country and state
            for city in cities:
                self.assertEqual(city.country_code, combo["country"])
                self.assertEqual(city.state_code, combo["state"])
                self.assertTrue(hasattr(city, 'name'))
                self.assertTrue(hasattr(city, 'latitude'))
                self.assertTrue(hasattr(city, 'longitude'))
    
    def test_get_cities_of_country(self):
        """Test retrieving cities by country code."""
        for code in self.country_codes:
            cities = City.get_cities_of_country(code)
            self.assertIsNotNone(cities)
            self.assertIsInstance(cities, list)
            self.assertGreater(len(cities), 0)
            
            # Verify all cities belong to the specified country
            for city in cities[:5]:
                self.assertEqual(city.country_code, code)
                self.assertTrue(hasattr(city, 'name'))
                self.assertTrue(hasattr(city, 'state_code'))
    
    def test_invalid_city_queries(self):
        """Test behavior with invalid query parameters."""
        for combo in self.invalid_combinations:
            cities = City.get_cities_of_state(combo["country"], combo["state"])
            self.assertEqual(cities, [])
            
        for code in ["", None, "XX"]:
            cities = City.get_cities_of_country(code)
            self.assertEqual(cities, [])
    
    def test_city_sorting(self):
        """Test that cities are sorted alphabetically."""
        for combo in self.state_combinations:
            cities = City.get_cities_of_state(combo["country"], combo["state"])
            if len(cities) > 1:
                # Check first few cities are in alphabetical order
                for i in range(min(5, len(cities) - 1)):
                    self.assertLessEqual(cities[i].name, cities[i+1].name)
                    
        for code in self.country_codes:
            cities = City.get_cities_of_country(code)
            if len(cities) > 1:
                # Check first few cities are in alphabetical order
                for i in range(min(5, len(cities) - 1)):
                    self.assertLessEqual(cities[i].name, cities[i+1].name)
    
    def test_to_dict(self):
        """Test conversion to dictionary."""
        cities = City.get_cities_of_state('US', 'CA')
        if cities:
            city = cities[0]
            city_dict = city.to_dict()
            
            self.assertIsInstance(city_dict, dict)
            self.assertEqual(city_dict['countryCode'], "US")
            self.assertEqual(city_dict['stateCode'], "CA")
            self.assertEqual(city_dict['name'], city.name)
            self.assertIn('latitude', city_dict)
            self.assertIn('longitude', city_dict)


if __name__ == '__main__':
    unittest.main()