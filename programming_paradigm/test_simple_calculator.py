import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
    # #     """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.    
    def test_subtraction(self):
        # result= self.calc.subtract(5,3)
        self.assertEqual(self.calc.subtract(5,3),2)
        # self.assertEqual(self.calc.subtract(5,"as"),2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5,3),15)
        self.assertEqual(self.calc.multiply(5,4),20)
        self.assertEqual(self.calc.multiply(5,0),0)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(15,3),5)
        self.assertEqual(self.calc.divide(15,0),None)
