from ConfigManager import ConfigManager
from Dictionary import Dictionary
from Engine import Engine
from TerminalGUI import TerminalGUI
from Stats import Stats
from Config import Config
from Validator import Validator
from Game import Game
import tkinter

if __name__ == '__main__':
    config_manager = ConfigManager(r"config.xml")
    config_manager.read_config()
    config = config_manager.config
    dictionary = Dictionary("resource/dictionary.txt")
    gui = TerminalGUI()
    validator = Validator()
    engine = Engine(None)
    game = Game(validator, gui, engine, dictionary, config.number_of_try)
    game.gameplay()
