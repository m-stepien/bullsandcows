import FileWriter
import Stats
from Validator import Validator


class Game:
    def __init__(self, gui, engine, dictionary, number_of_try):
        self.gui = gui
        self.engine = engine
        self.dictionary = dictionary
        self.engine.word = self.dictionary.choose_random_word()
        self.validator = Validator(len(self.engine.word))
        self.number_of_try = int(number_of_try)

    def gameplay(self):
        i = 0
        word = self.dictionary.choose_random_word()
        self.engine.word = word
        result = Stats.Stats(0, 0)
        valid_fail = False
        while i < self.number_of_try:
            answer = self.gui.game_screen(self.number_of_try - i, word, result, valid_fail)
            if self.gui.opt is None:
                break
            if valid_fail:
                self.gui.destroy_elems(self.gui.fr_valid, self.gui.lb_valid)
            valid_fail = False
            if not self.validator.full_word_validation(answer):
                valid_fail = True
                continue
            i += 1
            result = self.engine.round(answer)
            if self.engine.is_win(result.bulls):
                break
        if self.gui.opt:
            want_save = self.gui.show_end_screen(self.engine.is_win(result.bulls), word, i)
            if want_save:
                file_writer = FileWriter.FileWriter(self.gui.file_name)
                file_writer.write(self.gui.game_result_str)
