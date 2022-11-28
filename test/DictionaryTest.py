import pytest
from Dictionary import Dictionary


@pytest.mark.parametrize("diff_lvl,output_list", [("easy", ["a", "aa", "aaa", "aaaa"]), ("medium", ["aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa"]), ("hard", ["aaaaaaaaa", "aaaaaaaaaa"])])
def test_get_filter_word_list(diff_lvl, output_list):
    dict = Dictionary(diff_lvl)
    # zmiana listy w taki sposob aby uniezaleznic test od funkcji read_from_file
    dict.word_list = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    assert dict.get_filter_word_list() == output_list
