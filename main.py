from ConfigManager import ConfigManager
from Dictionary import Dictionary
from Engine import Engine
from TerminalGUI import TerminalGUI
from Validator import Validator
from Game import Game
import tkinter

if __name__ == '__main__':
    config_manager = ConfigManager(r"config.xml")
    config_manager.read_config()
    config = config_manager.config
    dictionary = Dictionary("resource/dictionary.txt")
    gui = TerminalGUI()
    while True:
        option = gui.showStartMenu()
        if option == 1:
            validator = Validator()
            engine = Engine(None)
            game = Game(validator, gui, engine, dictionary, config.number_of_try)
            game.gameplay()
        elif option == 2:
            gui.show_game_rule()
        elif option == 3:
            gui.show_configuration(config)
        elif option == 4:
            exit(0)
        else:
            gui.no_such_option_mess()
