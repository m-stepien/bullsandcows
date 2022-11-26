import FileWriter
import Stats


class Game:
    def __init__(self, validator, gui, engine, dictionary, number_of_try):
        self.validator = validator
        self.gui = gui
        self.engine = engine
        self.dictionary = dictionary
        self.number_of_try = int(number_of_try)
        self.answer = None

    def gameplay(self):
        i = 0
        word = self.dictionary.choose_random_word()
        self.engine.word = word
        result = Stats.Stats(0, 0)
        valid_fail=False
        while i < self.number_of_try:
            # self.gui.reload()
            answer = self.gui.game_screen(self.number_of_try - i, word,result, valid_fail)
            # self.gui.show_len_of_word(word)
            # answer = self.gui.get_answer()
            if self.gui.opt is None:
                break
            if valid_fail:
                self.gui.destroy_elems(self.gui.fr_valid, self.gui.lb_valid)
            valid_fail = False
            if not self.validator.is_word(answer) or not self.validator.is_valid(answer):
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

