import unittest

from Engine import Engine


class ValidatorTest(unittest.TestCase):
    def test_count_match_char_in_place_1(self):
        word = "word"
        engine = Engine(word, None)
        self.assertTrue(engine.count_match_char_in_place(word) == len(word))

    def test_count_match_char_in_place_2(self):
        word = "word"
        word2 = "must"
        engine = Engine(word, None)
        self.assertTrue(engine.count_match_char_in_place(word2) == 0)

    def test_count_match_char_in_place_3(self):
        word = "word"
        word2 = "drow"
        engine = Engine(word, None)
        self.assertTrue(engine.count_match_char_in_place(word2) == 0)

    def test_count_match_char_in_place_4(self):
        word = "word"
        word2 = "mpsd"
        engine = Engine(word, None)
        self.assertTrue(engine.count_match_char_in_place(word2) == 1)

    def test_count_match_char_in_place_5(self):
        word = "word"
        word2 = "mpod"
        engine = Engine(word, None)
        self.assertTrue(engine.count_match_char_in_place(word2) == 1)

    def test_count_match_char_in_place_skip_index_1(self):
        word = "word"
        word2 = "wozt"
        engine = Engine(word, None)
        engine.count_match_char_in_place(word2) == 1
        self.assertTrue(engine.index_to_skip.sort() == [0, 1].sort())

    def test_count_match_char_in_place_skip_index_2(self):
        word = "word"
        word2 = "wprt"
        engine = Engine(word, None)
        engine.count_match_char_in_place(word2) == 1
        self.assertTrue(engine.index_to_skip.sort() == [0, 2].sort())

    def test_count_match_char_wrong_place_1(self):
        word = "qwerty"
        engine = Engine(word, None)
        engine.index_to_skip = [x for x in range(0, len(word))]
        self.assertTrue(engine.count_match_char_wrong_place(word) == 0)

    def test_count_match_char_wrong_place_1(self):
        word = "qwerty"
        word2 = "ytrewq"
        engine = Engine(word, None)
        self.assertTrue(engine.count_match_char_wrong_place(word2) == len(word))

    def test_count_match_char_wrong_place_1(self):
        word = "qwerty"
        word2 = "qpreay"
        engine = Engine(word, None)
        engine.index_to_skip = [0, len(word2) - 1]
        self.assertTrue(engine.count_match_char_wrong_place(word2) == 2)

    def test_end_of_game_1(self):
        engine = Engine(None, 0)
        self.assertTrue(engine.end_of_game(None))

    def test_end_of_game_1(self):
        engine = Engine(None, None)
        word = "word"
        engine.word = word
        self.assertTrue(engine.end_of_game(len(word)))

    def test_end_of_game_1(self):
        engine = Engine(None, 4)
        word = "word"
        engine.word = word
        self.assertFalse(engine.end_of_game(len(word) - 2))

