class TerminalGUI:
    def __init__(self, left_guest_num, word):
        self.left_guest_num = left_guest_num
        self.word = word
        self.cows = 0
        self.bulls = 0

    def show_game_screen(self):
        print(f"Guest left {self.left_guest_num}")
        print(f"Bulls: {self.bulls}")
        print(f"Cows: {self.cows}")
        print(f"{self.word}")
        print(len(self.word))
        print("_ " * len(self.word))
        self.left_guest_num -= 1

    def showStartMenu(self):
        print("1. Nowa gra\n2. Zasady gry\n3. Ustawienia\4. Zakoncz gre")

    def showEngGameResult(self):
        pass

    def show_configuration_option(self):
        pass

    def show_game_rule(self):
        pass

    def update_game_display(self):
        pass
