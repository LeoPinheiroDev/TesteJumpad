import unittest
from lib.numbers import Number, Numbers

class TestNumber(unittest.TestCase):
    def test_is_even(self):
        num = Number(4)
        self.assertTrue(num.is_even())

        num = Number(5)
        self.assertFalse(num.is_even())

    def test_is_positive(self):
        num = Number(10)
        self.assertTrue(num.is_positive())

        num = Number(-1)
        self.assertFalse(num.is_positive())

        num = Number(0)
        self.assertFalse(num.is_positive())


class TestNumbers(unittest.TestCase):
    def test_sum(self):
        numbers = Numbers([1, 2, 3, 4, 5])
        self.assertEqual(numbers.sum(), 15)

        numbers = Numbers([])
        self.assertEqual(numbers.sum(), 0)

    def test_average(self):
        numbers = Numbers([1, 2, 3, 4, 5])
        self.assertEqual(numbers.average(), 3.0)

        numbers = Numbers([])
        with self.assertRaises(ValueError):
            numbers.average()


if __name__ == '__main__':
    unittest.main()