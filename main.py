from ConfigManager import ConfigManager
from Dictionary import Dictionary
from Engine import Engine
from TerminalGUI import TerminalGUI
from Stats import Stats
from Config import Config
import tkinter

if __name__ == '__main__':
    config_manager = ConfigManager(r"config.xml")
    config_manager.read_config()
    config = config_manager.config
    config = Config()
    config.set_from_values("gui", "hard", 60)
    config_manager.write_config(config)

    # dictionary = Dictionary("resource/dictionary.txt")
    # dictionary.read_from_file()
    # word = dictionary.choose_random_word()
    # engine = Engine(word, config.number_of_try)
    # gui = TerminalGUI(config.number_of_try, word)
    # gui.show_game_screen()
    # answer = input()
    # stat = engine.round(answer)
    # print(engine.end_of_game(stat.get_bulls()))
    # gui.cows = stat._cows
    # gui.bulls = stat._bulls
    # gui.show_game_screen()
