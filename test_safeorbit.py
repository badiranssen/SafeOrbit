# test_safeorbit.py
"""
Tests for SafeOrbit module.
"""

import unittest
from safeorbit import SafeOrbit

class TestSafeOrbit(unittest.TestCase):
    """Test cases for SafeOrbit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SafeOrbit()
        self.assertIsInstance(instance, SafeOrbit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SafeOrbit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
