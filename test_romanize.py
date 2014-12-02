import unittest

from romanize import get_roman_equivalent

class TestRomanize(unittest.TestCase):

    def setUp(self):
        pass

    def test_2345(self):
        self.assertEqual('MMCCCXLV', get_roman_equivalent(2345))

    def test_589(self):
        self.assertEqual('DLXXXIX', get_roman_equivalent(589))

    def test_641(self):
        self.assertEqual('DCXLI', get_roman_equivalent(641))

    def test_23(self):
        self.assertEqual('XXIII', get_roman_equivalent(23))

    def test_4(self):
        self.assertEqual('IV', get_roman_equivalent(4))

    def test_0(self):
        self.assertEqual('', get_roman_equivalent(0))

    def test_4000(self):
        self.assertEqual('None', get_roman_equivalent(4000)) # The method returns a string None

if __name__ == '__main__':
    unittest.main()
