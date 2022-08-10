import unittest
import pytest
from calc import SimpleCalc


class Caltests(unittest.TestCase):
    calc_obj = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc_obj.add(2,2), 4)

    def test_add_float(self):
        self.assertEqual(self.calc_obj.add(2.2, 4.6), 6.8)

    def test_multiply(self):
        self.assertEqual(self.calc_obj.multiply(4,3), 12)

    def test_multiply_float(self):
        self.assertEqual(self.calc_obj.multiply(5,3.5), 17.5)

    def test_divide(self):
        self.assertEqual(self.calc_obj.divide(8,4), 2)

    def test_divide_float(self):
        self.assertEqual(self.calc_obj.divide(10,2.5), 4)

    def test_divide_zero(self):
        self.assertEqual(self.calc_obj.divide(8,0), "division by zero is not allowed")

    def test_subtract(self):
        self.assertEqual(self.calc_obj.subtract(3,4), -1)

    def test_percentage(self):
        self.assertEqual(self.calc_obj.percentage(1,10), "10.0%")

    def test_percentage_neg(self):
        self.assertEqual(self.calc_obj.percentage(-5,15), "-33.3%")

    def test_percentage_zero(self):
        self.assertEqual(self.calc_obj.percentage(10,0), "division by zero is not allowed")

    def test_dob(self):
        self.assertEqual(self.calc_obj.dob(31,10), "31/10")

    def test_dob_outofrange(self):
        self.assertEqual(self.calc_obj.dob(-1,10), "Date is out of bounds")

    def test_dob_feb_31(self):
        self.assertEqual(self.calc_obj.dob(31,2), "Date is out of bounds")

    def test_cm_to_m(self):
        self.assertEqual(self.calc_obj.cm_m(100), 1.00)

