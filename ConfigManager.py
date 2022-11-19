import xml.etree.ElementTree as ET
import platform

#TODO wyciagnac sprawdzanie istnienia config current do osobnej metody

class ConfigManager:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = None

    def write_config(self):
        #TODO istnieje mozliwosc zapisania wielu config current powinien zawszy byc 1 lub 0
        sys = platform.uname()[0]
        gui = "Gui"
        diff_lvl = "Hard"
        try_number = 20
        new_conf = self.config
        new_conf.attrib["version"] = "current"
        new_conf.find("system").text = sys
        new_conf.find("gui").text = gui
        new_conf.find("difficulty_level").text = diff_lvl
        new_conf.find("number_of_try").text = str(try_number)
        tree = ET.parse(self.config_path)
        root = tree.getroot()
        root.append(new_conf)
        tree.write(self.config_path)

    def read_config(self):
        tree = ET.parse(self.config_path)
        root = tree.getroot()
        configs_list = root.findall("configuration")
        for config in configs_list:
            if config.get("version") == "current":
                self.config = config
        if self.config is None:
            try:
                for config in configs_list:
                    if config.get("version") == "default":
                        self.config = config
            # NWM
            except FileExistsError:
                print("Plik konfiguracyjny jest uszkodzony")
                exit(1)

    def get_current_system(self):
        return self.config.find("system").text

    def get_current_gui(self):
        return self.config.find("gui").text

    def get_current_difficulty_level(self):
        return self.config.find("difficulty_level").text

    def get_number_of_try(self):
        return int(self.config.find("number_of_try").text)


    def check_system(self):
        return platform.uname()[0]
