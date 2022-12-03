import pytest
from Dictionary import Dictionary


class TestDictionary:
    @pytest.fixture
    def dictionary(self):
        return Dictionary(None, "../resource/dictionary.txt")

    @pytest.mark.parametrize("diff_lvl,output_list", [("easy", ["a", "aa", "aaa", "aaaa"]),
                                                      ("medium", ["aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa"]),
                                                      ("hard", ["aaaaaaaaa", "aaaaaaaaaa"])])
    def test_get_filter_word_list(self, dictionary, diff_lvl, output_list):
        dictionary.difficulty_level = diff_lvl
        # zmiana listy w taki sposob aby uniezaleznic test od funkcji read_from_file
        dictionary.word_list = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa",
                                "aaaaaaaaaa"]
        assert dictionary.get_filter_word_list() == output_list
