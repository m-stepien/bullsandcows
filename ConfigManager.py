import xml.etree.ElementTree as ET
import platform
from Config import Config


class ConfigManager:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = None

    def write_config(self, config):
        # TODO nadpisuje default poniewaz referencja wciaz na nia wskazuje trzeba zmienic tworzenie nowego konfiga
        #  zeby uzywal xml.Element()
        tree = ET.parse(self.config_path)
        root = tree.getroot()
        new_config = ET.Element("configuration")
        new_config.attrib["version"] = "current"
        gui_ET = ET.Element("gui")
        gui_ET.text = config.gui
        new_config.append(gui_ET)
        diff_ET = ET.Element("difficulty_level")
        diff_ET.text = config.difficulty_level
        new_config.append(diff_ET)
        num_ET = ET.Element("number_of_try")
        num_ET.text = str(config.number_of_try)
        new_config.append(num_ET)
        conf_curr = self.__find_config__(root.findall("configuration"), "current")
        if conf_curr is not None:
            print(conf_curr.get("version"))
            root.remove(conf_curr)
        root.append(new_config)
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
