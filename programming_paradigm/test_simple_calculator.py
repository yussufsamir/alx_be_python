import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        
        self.calc = SimpleCalculator()

    def test_addition(self):
        
        self.assertEqual(self.calc.add(10, 3), 13)
        self.assertEqual(self.calc.add(-4, 4), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        
        self.assertEqual(self.calc.subtract(13, 3), 10)
        self.assertEqual(self.calc.subtract(0, 4), -4)
        self.assertEqual(self.calc.subtract(-3, -3), 0)

    def test_multiplication(self):
        
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(-2, -5), 10)
        self.assertEqual(self.calc.multiply(0, 200), 0)

    def test_division(self):
        
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertIsNone(self.calc.divide(5, 0))  

if __name__ == "__main__":
    unittest.main()
