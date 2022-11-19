from Stats import Stats


class Engine:
    def __init__(self, word, num_of_remaind_try):
        self.word = word
        self.index_to_skip = []
        self._num_of_remaind_try = num_of_remaind_try


    def end_of_game(self, bulls):
        if self._num_of_remaind_try == 0 or bulls == len(self.word):
            return True
        else:
            return False

    def round(self, player_answer):
        self.index_to_skip = []
        bulls = self.count_match_char_in_place(player_answer)
        cows = self.count_match_char_wrong_place(player_answer)
        result = Stats(bulls, cows)
        self._num_of_remaind_try -= 1
        return result

    def count_match_char_in_place(self, player_answer):
        # assum player_answer word sa tej samej dlugosci
        counter = 0
        for e, char in enumerate(self.word):
            if char == player_answer[e]:
                counter += 1
                self.index_to_skip.append(e)
        return counter

    #TODO do przemyslenia czy potrzebne usuwanie znalezionych znakow z powyzszej metody czy spowoduje powtorzenia
    def count_match_char_wrong_place(self, player_answer):
        counter = 0
        for e, char in enumerate(player_answer):
            if char in self.word and e not in self.index_to_skip:
                counter += 1
        return counter

    def get_num_of_remaind_try(self):
        return self.num_of_remaind_try
