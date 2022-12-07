import re


class Validator:
    def __init__(self, l_word, answer=None):
        self.answer = answer
        self.l_word = l_word

    def full_word_validation(self, answer):
        self.answer = answer.upper()
        return self.is_word() and self.is_valid() and self.is_same_len()

    def is_valid(self):
        for char in self.answer:
            if self.answer.count(char) > 1:
                return False
        return True

    def is_word(self):
        pattern = "^[A-Za-z]+$"
        result = re.search(pattern, self.answer)
        if result is None:
            return False
        else:
            return True

    def is_same_len(self):
        try:
            len_answer = len(self.answer)
            return self.l_word == len_answer
        except TypeError:
            raise TypeError
