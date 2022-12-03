import xml.etree.ElementTree as Et
from Config import Config


class ConfigManager:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = None

    def write_config(self, config):
        tree = Et.parse(self.config_path)
        root = tree.getroot()
        new_config = Et.Element("configuration")
        new_config.attrib["version"] = "current"
        gui_et = Et.Element("gui")
        if config.gui is not None:
            print(config.gui)
            gui_et.text = config.gui
        else:
            gui_et.text = self.config.gui
        new_config.append(gui_et)
        diff_et = Et.Element("difficulty_level")
        if config.difficulty_level is not None:
            diff_et.text = config.difficulty_level
        else:
            diff_et.text = self.config.difficulty_level
        new_config.append(diff_et)
        num_et = Et.Element("number_of_try")
        if config.number_of_try is not None:
            num_et.text = str(config.number_of_try)
        else:
            num_et.text = str(self.config.number_of_try)
        new_config.append(num_et)
        conf_curr = self.__find_config__(root.findall("configuration"), "current")
        if conf_curr is not None:
            root.remove(conf_curr)
        root.append(new_config)
        tree.write(self.config_path)
        self.read_config()

    def read_config(self):
        try:
            tree = Et.parse(self.config_path)
            root = tree.getroot()
            configs_list = root.findall("configuration")
            config_xml = self.__find_config__(configs_list, "current")
            if config_xml is None:
                config_xml = self.__find_config__(configs_list, "default")
                if config_xml is None:
                    raise Et.ParseError
            # NWM
        except (FileExistsError, Et.ParseError) as error:
            print("Plik konfiguracyjny jest uszkodzony")
            exit(1)
        self.config = Config()
        self.config.set_from_xml(config_xml)

    def __find_config__(self, config_list, version):
        for config in config_list:
            if config.get("version") == version:
                return config
        return None

    def reset_config(self):
        tree = Et.parse(self.config_path)
        root = tree.getroot()
        conf_curr = self.__find_config__(root.findall("configuration"), "current")
        if conf_curr is not None:
            root.remove(conf_curr)
        tree.write(self.config_path)
        self.read_config()
