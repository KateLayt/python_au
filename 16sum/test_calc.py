import unittest
from calc import HexNumber


class TestHexNumber(unittest.TestCase):

    def test_is_correct_string_low(self):
        self.assertEqual("", str(HexNumber("abc")))

    def test_is_correct_string_symbols(self):
        self.assertEqual("", str(HexNumber("JKL")))

    def test_is_correct_string(self):
        self.assertEqual("ABC", str(HexNumber("ABC")))

    def test_add_common(self):
        num1 = HexNumber("123")
        num2 = HexNumber("210")
        expect = "333"
        result = str(num1.add(num2))
        self.assertEqual(expect, result)

    def test_add_complicated(self):
        num1 = HexNumber("A56")
        num2 = HexNumber("711")
        expect = "1167"
        result = str(num1.add(num2))
        self.assertEqual(expect, result)

    def test_add_different_len(self):
        num1 = HexNumber("12")
        num2 = HexNumber("11111")
        expect = "11123"
        result = str(num1.add(num2))
        self.assertEqual(expect, result)

    def test_add_nothing(self):
        num1 = HexNumber("1111")
        num2 = HexNumber("")
        expect = "1111"
        result = str(num1.add(num2))
        self.assertEqual(expect, result)

    def test_add_none(self):
        num1 = HexNumber("1111")
        num2 = None
        expect = None
        result = num1.add(num2)
        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()
