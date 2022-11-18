class TerminalGUI(Gui):
    def __init__(self):
        self.left_guest_num = left_guest_num
        self.word = word
        self.cows = 0
        self.bulls = 0

    def show_game_screen(self):
        print("Guest left {}", self.left_guest_num)
        print("Bulls: {}", self.bulls)
        print("Cows: {}", self.cows)
        print("\t\t\t{}", word)
        print("_ " * len(word))

    def showStartMenu(self):
        print("1. Nowa gra\n2. Zasady gry\n3. Ustawienia\4. Zakoncz gre")

    def showEngGameResult(self):
        pass

    def show_configuration_option(self):
        pass

    def show_game_rule(self):
        pass

    def update_game_display(self)
