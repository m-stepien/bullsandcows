import xml.etree.ElementTree as ET

class ConfigManager:
    def __init__(self, config_path):
        self.config_path = config_path
    def read_config(self):
        tree = ET.parse(self.config_path)
        root = tree.getroot()
        configs_list = root.findall("configuration")
        for config in configs_list:
            if config.get(version)=="current":
                return config
        try:
            for config in configs_list:
                if config.get(version) == "default":
                    return config
        # NWM
        except FileExistsError:
            print("Plik konfiguracyjny jest uszkodzony")
            exit(1)




