import xml.etree.ElementTree as ET


class Config:
    def __init__(self):
        self.difficulty_level = None
        self.number_of_try = None

    def set_from_xml(self, config_xml):
        self.difficulty_level = config_xml.find("difficulty_level").text
        self.number_of_try = config_xml.find("number_of_try").text

    def set_from_values(self, diff_lvl, n_of_try):
        self.difficulty_level = diff_lvl
        self.number_of_try = n_of_try

    def __str__(self):
        return f"KONFIGURACJA\nPoziom trudnosci:\t{self.difficulty_level}\n" \
               f"Liczba prob:\t{self.number_of_try}"
