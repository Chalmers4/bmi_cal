import unittest
from bmi_calculator import calculate_bmi, get_bmi_category


class TestBMICalculator(unittest.TestCase):
    def test_calculate_bmi(self):
        # Test cases for calculate_bmi function
        self.assertAlmostEqual(calculate_bmi(5, 0, 90), 17.6, places=1)  # Underweight
        self.assertAlmostEqual(calculate_bmi(5, 6, 140), 22.6, places=1)  # Normal weight
        self.assertAlmostEqual(calculate_bmi(5, 10, 200), 28.7, places=1)  # Overweight
        self.assertAlmostEqual(calculate_bmi(6, 0, 250), 33.9, places=1)  # Obese

    def test_get_bmi_category(self):
        # Test cases for get_bmi_category function
        self.assertEqual(get_bmi_category(17.5), "Underweight")  # Underweight
        self.assertEqual(get_bmi_category(18.5), "Normal weight")  # Normal weight (lower boundary)
        self.assertEqual(get_bmi_category(24.9), "Normal weight")  # Normal weight (upper boundary)
        self.assertEqual(get_bmi_category(25.0), "Overweight")  # Overweight (lower boundary)
        self.assertEqual(get_bmi_category(29.9), "Overweight")  # Overweight (upper boundary)
        self.assertEqual(get_bmi_category(30.0), "Obese")  # Obese (lower boundary)


if __name__ == "__main__":
    unittest.main()