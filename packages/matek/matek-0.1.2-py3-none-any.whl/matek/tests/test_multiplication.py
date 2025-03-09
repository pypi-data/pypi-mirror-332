import unittest

from szorzas import generate_number

class TestMultiplication(unittest.TestCase):
    def test_generate_number(self):
        for digit in range(1, 10):
            with self.subTest(digit=digit):
                number = generate_number(digit)
                self.assertTrue(10 ** (digit-1) <= number <= 10**digit - 1)
                self.assertEqual(len(str(number)), digit)
