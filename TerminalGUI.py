class TerminalGUI:
    def __init__(self):
        self.cows = 0
        self.bulls = 0

    def show_result(self):
        print(f"Bulls: {self.bulls}")
        print(f"Cows: {self.cows}")

    def get_input(self):
        return input()

    def show_len_of_word(self, word):
        print(f"Dlugosc slowa {len(word)}")

    def showStartMenu(self):
        print("1. Nowa gra\n2. Zasady gry\n3. Ustawienia\4. Zakoncz gre")

    def showEndGameResult(self):
        pass

    def show_configuration_option(self):
        pass

    def show_game_rule(self):
        pass

    def update_game_display(self):
        pass
