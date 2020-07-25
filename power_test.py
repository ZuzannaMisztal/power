import unittest

from power import power, ToHardEquationError


class PowerTest(unittest.TestCase):
    def test_pow_1_1_is_1(self):
        self.assertEqual(power(1, 1), 1)

    def test_pow_100_1_is_100(self):
        self.assertEqual(power(100, 1), 100)

    def test_pow_2_0_is_1(self):
        self.assertEqual(power(2, 0), 1)

    def test_pow_0_0_is_1(self):
        self.assertEqual(power(0, 0), 1)

    def test_pow_0_2_is_0(self):
        self.assertEqual(power(0, 2), 0)

    def test_random_numbers(self):
        self.assertEqual(power(5, 3), 5**3)

    def test_negative_base(self):
        self.assertEqual(power(-2, 3), -8)

    def test_negative_exponent(self):
        self.assertEqual(power(4, -2), 4**-2)

    def test_floating_base(self):
        self.assertEqual(power(0.5, 2), 0.25)

    def test_floating_exponent(self):
        with self.assertRaises(ToHardEquationError):
            power(4, 0.5)

    def test_both_are_negative(self):
        self.assertEqual(power(-2, -2), (-2)**-2)

    def test_both_floating(self):
        with self.assertRaises(ToHardEquationError):
            power(1/8, 1/3)

    def test_0_to_negative_raises_exception(self):
        with self.assertRaises(ZeroDivisionError):
            power(0, -2)

