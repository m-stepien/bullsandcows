from Stats import Stats


class Engine:
    def __init__(self, word):
        self.word = word
        self.index_to_skip = []

    def is_win(self, bulls):
        print(bulls)
        print(self.word)
        return bulls == len(self.word)

    def round(self, player_answer):
        self.index_to_skip = []
        bulls = self.count_match_char_in_place(player_answer)
        cows = self.count_match_char_wrong_place(player_answer)
        result = Stats(bulls, cows)
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
        for e, char in enumerate(player_answer):
            if char in self.word and e not in self.index_to_skip:
                counter += 1
        return counter

    def get_num_of_remaind_try(self):
        return self.num_of_remaind_try
