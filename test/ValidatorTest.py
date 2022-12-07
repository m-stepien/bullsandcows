import pytest
from Validator import Validator


class TestValidator:
    @pytest.fixture
    def validator(self):
        return Validator(8)

    # Test sprawdzajacy czy odpowiedz uzytkownika ma odpowiednia dlugosc
    @pytest.mark.parametrize("answer,result", [("a" * 8, True), ("a" * 7, False), ("a" * 30, False)])
    def test_validator_len_of_word(self, validator, answer, result):
        validator.answer = answer
        assert validator.is_same_len() == result

    # Test upewniajacy ze w przypadku niewlasciwej dlugosci odpowiedni blad zostanie rzucony
    def test_validator_len_of_word_excep(self, validator):
        with pytest.raises(TypeError) as err:
            assert err == validator.is_same_len(8)

    # Test sprawdzajacy czy slowo sklada sie tylko z liter
    @pytest.mark.parametrize("word,result", [("slowa", True), ("slowa" * 2, True), ("SLOWO", True), ("   ", False),
                                             ("dwa slowa", False), ("123", False), ("sl0wa", False), ("", False)])
    def test_validator_is_word(self, validator, word, result):
        validator.answer = word
        assert validator.is_word() == result

    # Test sprawdzajacy czy slowo jest izogramem
    @pytest.mark.parametrize("answer,result", [("duzo", True), ("slowo", False), ("DUZO", True), ("SLOWO", False)])
    def test_validator_is_valid(self, validator, answer, result):
        validator.answer = answer
        assert validator.is_valid() == result
