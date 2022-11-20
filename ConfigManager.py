import xml.etree.ElementTree as ET
import platform
from Config import Config


class ConfigManager:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = None

    def write_config(self, config):
        #TODO nadpisuje default poniewaz referencja wciaz na nia wskazuje trzeba zmienic tworzenie nowego konfiga zeby uzywal xml.Element()
        tree = ET.parse(self.config_path)
        root = tree.getroot()
        root.append(self.__find_config__(root.findall("configuration"), "default"))
        new_conf = self.__find_config__(root.findall("configuration"), "default")
        tree.write(self.config_path)
        new_conf.attrib["version"] = "current"
        new_conf.find("gui").text = config.gui
        new_conf.find("difficulty_level").text = config.difficulty_level
        new_conf.find("number_of_try").text = config.number_of_try
        conf_curr = self.__find_config__(root.findall("configuration"), "current")
        if conf_curr is not None:
            print(conf_curr.get("version"))
            root.remove(conf_curr)
            print("dajkda")
        root.append(new_conf)
        tree.write(self.config_path)

    def read_config(self):
        tree = ET.parse(self.config_path)
        root = tree.getroot()
        configs_list = root.findall("configuration")
        config_xml = self.__find_config__(configs_list, "current")
        if config_xml is None:
            try:
                config_xml = self.__find_config__(configs_list, "default")
            # NWM
            except FileExistsError:
                print("Plik konfiguracyjny jest uszkodzony")
                exit(1)
        self.config = Config()
        self.config.set_from_xml(config_xml)

    def check_system(self):
        return platform.uname()[0]

    def __find_config__(self, config_list, version):
        for config in config_list:
            if config.get("version") == version:
                return config
        return None

    def reset_config(self):
        tree = ET.parse(self.config_path)
        root = tree.getroot()
        conf_curr = self.__find_config__(root.findall("configuration"), "current")
        if conf_curr is not None:
            root.remove(conf_curr)
        tree.write(self.config_path)
        self.read_config()

