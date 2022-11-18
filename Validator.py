import re


class Validator:

    def is_valid(self, word):
        for char in word:
            if word.count(char) > 1:
                return False
        return True

    def is_word(self, word):
        word = word.upper()
        pattern = "^[A-Z]+$"
        result = re.search(pattern, word)
        if result is None:
            return False
        else:
            return True
