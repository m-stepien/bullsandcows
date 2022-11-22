class Game:
    def __init__(self, validator, gui, engine, dictionary, number_of_try):
        self.validator = validator
        self.gui = gui
        self.engine = engine
        self.dictionary = dictionary
        self.number_of_try = int(number_of_try)

    def gameplay(self):
        i = 0
        bulls = None
        word = self.dictionary.choose_random_word()
        self.engine.word = word
        while i < self.number_of_try:
            self.gui.show_len_of_word(word)
            answer = self.gui.get_input()
            if not self.validator.is_word(answer) or not self.validator.is_valid(answer):
                print("Bledna odpowiedz")
                continue
            result = self.engine.round(answer)
            self.gui.bulls = result.get_bulls()
            self.gui.cows = result.get_cows()
            self.gui.show_result()
            if self.engine.is_win(bulls):
                break
            i += 1

        if self.engine.is_win(bulls):
            print("Wygralem")
        else:
            print("Przegralem")