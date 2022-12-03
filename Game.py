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
        result = Stats.Stats(0, 0)
        while i < self.number_of_try:
            self.gui.set_guess_result(self.number_of_try - i, result, len(self.engine.word))
            self.gui.show_result_of_guess()
            answer = self.gui.get_answer()
            if not self.validator.full_word_validation(answer):
                print("Bledna odpowiedz")
                continue
            i += 1
            result = self.engine.round(answer)

            if self.engine.is_win(result.bulls):
                break

        want_save = self.gui.show_win_screen(self.engine.is_win(result.bulls), self.engine.word, i)
        if want_save:
            file_name = self.gui.get_file_name()
            file_writer = FileWriter.FileWriter(file_name)
            if file_writer.check_is_file():
                want_override = self.gui.file_already_exist()
                if not want_override:
                    return
            file_writer.write(self.gui.game_result_str)
