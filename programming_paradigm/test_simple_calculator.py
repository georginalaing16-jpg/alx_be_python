import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(7, 3), 10)

    def test_subtract(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(4, 8), -4)

    def test_multiply(self):
        """Test the multiplication method"""
        self.assertEqual(self.calc.multiply(2, 1), 2)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        """Test the multiplication method"""
        self.assertEqual(self.calc.divide(2, 1), 2)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(6, 2), 3)
        
        self.assertIsNone(self.calc.divide(9, 0), "Error: Diving by zero")

if __name__ == "__main__":
    unittest.main()
