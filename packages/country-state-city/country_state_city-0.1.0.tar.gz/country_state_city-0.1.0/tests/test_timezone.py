"""
Tests for the Timezone module.
"""

import unittest
from country_state_city import Country, Timezone


class TestTimezone(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        # Get a country with timezones
        self.usa = Country.get_country_by_code('US')
        
        # Sample timezone data for testing from_dict and to_dict
        self.sample_timezone_data = {
            'zoneName': 'America/New_York',
            'gmtOffset': -18000,
            'gmtOffsetName': 'UTC-05:00',
            'abbreviation': 'EST',
            'tzName': 'Eastern Standard Time'
        }
    
    def test_country_timezones(self):
        """Test that country timezones are properly loaded."""
        self.assertIsNotNone(self.usa)
        self.assertGreater(len(self.usa.timezones), 0)
        
        # Test timezone attributes
        for timezone in self.usa.timezones[:5]:
            self.assertIsInstance(timezone, Timezone)
            self.assertTrue(hasattr(timezone, 'name'))
            self.assertTrue(hasattr(timezone, 'gmt_offset'))
            self.assertTrue(hasattr(timezone, 'gmt_offset_name'))
            self.assertTrue(hasattr(timezone, 'abbreviation'))
            self.assertTrue(hasattr(timezone, 'tz_name'))
    
    def test_from_dict(self):
        """Test creating a Timezone from a dictionary."""
        timezone = Timezone.from_dict(self.sample_timezone_data)
        
        self.assertEqual(timezone.name, 'America/New_York')
        self.assertEqual(timezone.gmt_offset, -18000)
        self.assertEqual(timezone.gmt_offset_name, 'UTC-05:00')
        self.assertEqual(timezone.abbreviation, 'EST')
        self.assertEqual(timezone.tz_name, 'Eastern Standard Time')
    
    def test_to_dict(self):
        """Test converting a Timezone to a dictionary."""
        timezone = Timezone.from_dict(self.sample_timezone_data)
        result_dict = timezone.to_dict()
        
        self.assertEqual(result_dict['zoneName'], 'America/New_York')
        self.assertEqual(result_dict['gmtOffset'], -18000)
        self.assertEqual(result_dict['gmtOffsetName'], 'UTC-05:00')
        self.assertEqual(result_dict['abbreviation'], 'EST')
        self.assertEqual(result_dict['tzName'], 'Eastern Standard Time')
        
        # Test that the result matches the original data
        for key, value in self.sample_timezone_data.items():
            self.assertEqual(result_dict[key], value)
    
    def test_repr(self):
        """Test the string representation of a Timezone."""
        timezone = Timezone.from_dict(self.sample_timezone_data)
        repr_str = repr(timezone)
        
        self.assertIn('Timezone', repr_str)
        self.assertIn(timezone.name, repr_str)
    
    def test_from_dict_with_missing_fields(self):
        """Test creating a Timezone with missing fields."""
        incomplete_data = {
            'zoneName': 'America/Chicago'
            # Missing other fields
        }
        
        timezone = Timezone.from_dict(incomplete_data)
        self.assertEqual(timezone.name, 'America/Chicago')
        self.assertEqual(timezone.gmt_offset, 0)  # Default value
        self.assertEqual(timezone.gmt_offset_name, '')  # Default value
        self.assertEqual(timezone.abbreviation, '')  # Default value
        self.assertEqual(timezone.tz_name, '')  # Default value


if __name__ == '__main__':
    unittest.main()