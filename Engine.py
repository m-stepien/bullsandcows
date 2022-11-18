from Stats import Stats


class Engine:
    def __init__(self, word, num_of_remaind_try):
        self.word = word
        self.index_to_skip = []
        self._num_of_remaind_try = num_of_remaind_try

    def end_of_game(self):
        return self._num_of_remaind_try == 0

    def round(self, player_answer):
        bulls = count_match_char_in_place(player_answer)
        cows = count_match_char_wrong_place(player_answer)
        result = Stats(bulls, cows)
        self.num_of_remaind_try -= 1
        return result

    def count_match_char_in_place(self, player_answer):
        # assum player_answer word sa tej samej dlugosci
        counter = 0
        for e, char in enumerate(self.word):
            if char == player_answer[e]:
                counter += 1
                self.index_to_skip.append(e)
        return counter

    def count_match_char_wrong_place(self, player_answer):
        counter = 0
        for char in player_answer:
            if char in self.word:
                counter += 1
        return counter

    def get_num_of_remaind_try(self):
        return self.num_of_remaind_try
