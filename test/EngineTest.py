import pytest
from Engine import Engine


class TestEngine:
    @pytest.fixture
    def engine(self):
        return Engine("word")
    #Test sprawdzajacy czy prawidlowo sa liczone litery na wlasciwych miejscach
    @pytest.mark.parametrize("answer,result",
                             [("word", 4), ("asgf", 0), ("womp", 2), ("wara", 2), ("drow", 0), ("wrod", 2)])
    def test_count_match_char_in_place(self, engine, answer, result):
        assert engine.count_match_char_in_place(answer) == result

    #Test sprawdzajacy czy prawidlowo sa dodawane indeksy do pominiecia
    @pytest.mark.parametrize("answer,skip_list",
                             [("word", [0, 1, 2, 3]), ("asgf", []), ("womp", [0, 1]), ("wara", [0, 2]), ("drow", []),
                              ("wrod", [0, 3])])
    def test_count_match_char_in_place_skip_index(self, engine, answer, skip_list):
        engine.count_match_char_in_place(answer)
        assert engine.index_to_skip.sort() == skip_list.sort()

    #Test sprawdzajacy czy prawidlowo sa liczone litery prawidlowe ktore sa na niewlasciwym miejscu
    @pytest.mark.parametrize("answer,skip_list,result",
                             [("word", [0, 1, 2, 3], 0), ("wodm", [0, 1], 1), ("drow", [], 4), ("dapw", [], 2)])
    def test_count_match_wrong_place(self, engine, answer, skip_list, result):
        engine.index_to_skip = skip_list
        assert engine.count_match_char_wrong_place(answer) == result
