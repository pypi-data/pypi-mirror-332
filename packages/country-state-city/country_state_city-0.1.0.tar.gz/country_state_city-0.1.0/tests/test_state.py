"""
Tests for the State module.
"""

import unittest
from country_state_city import State


class TestState(unittest.TestCase):
    def setUp(self):
        # Set up test cases
        self.country_codes = ["US", "IN", "CA"]
        self.state_combinations = [
            {"country": "US", "state": "CA"},  # California, USA
            {"country": "US", "state": "NY"},  # New York, USA
            {"country": "IN", "state": "MH"},  # Maharashtra, India
            {"country": "CA", "state": "ON"},  # Ontario, Canada
        ]
        self.invalid_combinations = [
            {"country": "US", "state": "XX"},  # Invalid state
            {"country": "XX", "state": "CA"},  # Invalid country
            {"country": "", "state": ""},      # Empty codes
            {"country": None, "state": None},  # None codes
        ]
    
    def test_get_states(self):
        """Test retrieving all states."""
        states = State.get_states()
        self.assertIsNotNone(states)
        self.assertIsInstance(states, list)
        self.assertGreater(len(states), 0)
        
        # Test that returned objects are State instances
        for state in states[:5]:
            self.assertIsInstance(state, State)
            self.assertTrue(hasattr(state, 'name'))
            self.assertTrue(hasattr(state, 'country_code'))
            self.assertTrue(hasattr(state, 'iso_code'))
    
    def test_get_states_of_country(self):
        """Test retrieving states by country code."""
        for code in self.country_codes:
            states = State.get_states_of_country(code)
            self.assertIsNotNone(states)
            self.assertIsInstance(states, list)
            self.assertGreater(len(states), 0)
            
            # Verify all states belong to the specified country
            for state in states:
                self.assertEqual(state.country_code, code)
                self.assertTrue(hasattr(state, 'name'))
                self.assertTrue(hasattr(state, 'iso_code'))
    
    def test_get_state_by_code(self):
        """Test retrieving a state by country and state code."""
        for combo in self.state_combinations:
            state = State.get_state_by_code(combo["country"], combo["state"])
            self.assertIsNotNone(state)
            self.assertIsInstance(state, State)
            self.assertEqual(state.country_code, combo["country"])
            self.assertEqual(state.iso_code, combo["state"])
            
            # Test basic state properties
            self.assertTrue(hasattr(state, 'name'))
            self.assertTrue(hasattr(state, 'latitude'))
            self.assertTrue(hasattr(state, 'longitude'))
    
    def test_invalid_state_codes(self):
        """Test behavior with invalid state codes."""
        for combo in self.invalid_combinations:
            state = State.get_state_by_code(combo["country"], combo["state"])
            self.assertIsNone(state)
    
    def test_california_properties(self):
        """Test specific properties of California."""
        california = State.get_state_by_code('US', 'CA')
        self.assertEqual(california.name, "California")
        self.assertEqual(california.country_code, "US")
        self.assertEqual(california.iso_code, "CA")
        
        # Check that latitude and longitude are present
        self.assertIsNotNone(california.latitude)
        self.assertIsNotNone(california.longitude)
    
    def test_to_dict(self):
        """Test conversion to dictionary."""
        california = State.get_state_by_code('US', 'CA')
        state_dict = california.to_dict()
        
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['name'], "California")
        self.assertEqual(state_dict['countryCode'], "US")
        self.assertEqual(state_dict['isoCode'], "CA")
        self.assertIn('latitude', state_dict)
        self.assertIn('longitude', state_dict)


if __name__ == '__main__':
    unittest.main()