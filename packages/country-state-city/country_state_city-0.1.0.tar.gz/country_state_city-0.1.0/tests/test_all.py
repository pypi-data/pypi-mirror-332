"""
Main test runner for the country_state_city library.
"""

import unittest

# Import all test modules
from tests.test_country import TestCountry
from tests.test_state import TestState
from tests.test_city import TestCity
from tests.test_timezone import TestTimezone


if __name__ == '__main__':
    # Create a test suite with all tests
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestCountry))
    test_suite.addTest(unittest.makeSuite(TestState))
    test_suite.addTest(unittest.makeSuite(TestCity))
    test_suite.addTest(unittest.makeSuite(TestTimezone))
    
    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)