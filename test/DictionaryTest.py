import pytest
from Dictionary import Dictionary


class TestDictionary:
    @pytest.fixture
    def dictionary(self):
        return Dictionary(None, "../resource/dictionary.txt")

    # Test ma za zadanie upewnic sie ze filtrowanie slownika po poziomie trudnosci dziala prawidlowo
    @pytest.mark.parametrize("diff_lvl,output_list", [("easy", ["a", "aa", "aaa", "aaaa"]),
                                                      ("medium", ["aaaaa", "aaaaaa", "aaaaaaa"]),
                                                      ("hard", ["aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"])])
    def test_get_filter_word_list(self, dictionary, diff_lvl, output_list):
        dictionary.difficulty_level = diff_lvl
        # zmiana listy w taki sposob aby uniezaleznic test od funkcji read_from_file
        dictionary.word_list = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa",
                                "aaaaaaaaaa"]
        assert dictionary.get_filter_word_list() == output_list

    # dodatkowy test sprawdzajacy czy slowo wylosowane jest z prawidlowego zakresu dlugosci
    @pytest.mark.parametrize("diff_lvl,down,up", [("easy", 1, 4),
                                                  ("medium", 5, 7),
                                                  ("hard", 7, 25)])
    def test_is_word_good_len(self, dictionary, diff_lvl, down, up):
        dictionary.difficulty_level = diff_lvl
        assert down <= len(dictionary.choose_random_word()) <= up
