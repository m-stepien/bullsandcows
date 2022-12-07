class Config:
    def __init__(self):
        self.gui = None
        self.difficulty_level = None
        self.number_of_try = None

    def set_from_xml(self, config_xml):
        self.gui = config_xml.find("gui").text
        self.difficulty_level = config_xml.find("difficulty_level").text
        self.number_of_try = config_xml.find("number_of_try").text

    def set_from_values(self, gui, diff_lvl, n_of_try):
        self.gui = gui
        self.difficulty_level = diff_lvl
        self.number_of_try = n_of_try

    def __str__(self):
        return f"KONFIGURACJA\nGui:\t{self.gui}\nPoziom trudnosci:\t{self.difficulty_level}\n" \
               f"Liczba prob:\t{self.number_of_try}"
