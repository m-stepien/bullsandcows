import FileWriter
import Stats


class Game:
    def __init__(self, validator, gui, engine, dictionary, number_of_try):
        self.validator = validator
        self.gui = gui
        self.engine = engine
        self.dictionary = dictionary
        self.number_of_try = int(number_of_try)

    def gameplay(self):
        i = 0
        word = self.dictionary.choose_random_word()
        self.engine.word = word
        result = Stats.Stats(0,0)
        while i < self.number_of_try:
            # self.gui.reload()
            self.gui.game_screen(self.number_of_try - i, word,result)
            # self.gui.show_len_of_word(word)
            # answer = self.gui.get_answer()
            answer = "a"
            if not self.validator.is_word(answer) or not self.validator.is_valid(answer):
                print("Bledna odpowiedz")
                continue
            i += 1
            # result = self.engine.round(answer)
            # self.gui.show_result(result)
            if self.gui.opt is None:
                break
            if self.engine.is_win(result.bulls):
                break

        # want_save = self.gui.show_win_screen(self.engine.is_win(result.bulls),word, i)
        # if want_save:
        #     file_name = self.gui.get_file_name()
        #     file_writer = FileWriter.FileWriter(file_name)
        #     file_writer.write(self.gui.game_result_str)

