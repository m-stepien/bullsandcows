from ConfigManager import ConfigManager
from Dictionary import Dictionary
from Config import Config
from Engine import Engine
from TerminalGUI import TerminalGUI
from Game import Game
from TkinterGui import TkinterGui
import os

was_change = False
if __name__ == '__main__':
    config_manager = ConfigManager(r"config.xml")
    config_manager.read_config()
    config = config_manager.config
    if config.gui == "terminal":
        gui = TerminalGUI()
    else:
        gui = TkinterGui()
    while True:
        config = config_manager.config

        dictionary = Dictionary(config.difficulty_level, "resource/dictionary.txt")
        option = gui.show_start_menu()
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
                    gui_conf = result[0]
                    diff_lvl = result[1]
                    num_try = result[2]
                    if gui_conf is None and diff_lvl is None and num_try is None:
                        continue
                    else:
                        new_conf = Config()
                        new_conf.set_from_values(gui_conf, diff_lvl, num_try)
                        config_manager.write_config(new_conf)
                        print(config.gui)
                        if config.gui == "terminal":
                            os.system("python main.py")
                            del gui
                            os._exit(0)
                        else:
                            gui.root.quit()
                            gui.root.destroy()
                            del gui
                            os.system("python main.py")
                            os._exit(0)


        elif option == "4":
            exit(0)
        else:
            gui.no_such_option_mess()
