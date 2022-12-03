from ConfigManager import ConfigManager
from Dictionary import Dictionary
from Engine import Engine
from TerminalGUI import TerminalGUI
from Game import Game
from Config import Config

if __name__ == '__main__':
    config_manager = ConfigManager(r"config.xml")
    config_manager.read_config()
    gui = TerminalGUI()
    while True:
        config = config_manager.config
        dictionary = Dictionary(config.difficulty_level,"resource/dictionary.txt")
        option = gui.showStartMenu()
        if option == "1":
            engine = Engine(None)
            game = Game(gui, engine, dictionary, config.number_of_try)
            game.gameplay()
        elif option == "2":
            gui.show_game_rule()
        elif option == "3":
            result = gui.show_configuration(config)
            if result:
                if type(result) == bool:
                    config_manager.reset_config()
                else:
                    diff_lvl = result[0]
                    num_try = result[1]
                    if diff_lvl is None and num_try is None:
                        continue
                    else:
                        new_conf = Config()
                        new_conf.set_from_values(diff_lvl, num_try)
                        config_manager.write_config(new_conf)

        elif option == "4":
            exit(0)
        else:
            gui.no_such_option_mess()
