import unittest

import Validator


class ValidatorTest(unittest.TestCase):
    def test_is_valid_1(self):
        self.assertTrue(Validator.Validator.is_valid(self,"kot"))

    def test_is_valid_2(self):
        self.assertFalse(Validator.Validator.is_valid(self,"mamalyga"))

    def test_is_valid_3(self):
        self.assertTrue(Validator.Validator.is_valid(self,"pterodakyl"))
    def test_is_word_1(self):
        self.assertTrue(Validator.Validator.is_word(self, "word"))
    def test_is_word_2(self):
        self.assertFalse(Validator.Validator.is_word(self, "many words"))
    def test_is_word_3(self):
        self.assertFalse(Validator.Validator.is_word(self, "many1words"))
    def test_is_word_4(self):
        self.assertFalse(Validator.Validator.is_word(self, "many$words"))





if __name__ == '__main__':
    unittest.main()