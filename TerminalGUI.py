import platform
import os


class TerminalGUI:

    def show_try_remind(self, num):
        print(f"Try remind:\t{num}")

    def show_result(self, stats):
        print(stats)

    def get_answer(self):
        return input()

    def get_file_name(self):
        print("Podaj nazwe pliku")
        return input()

    def show_len_of_word(self, word):
        print(f"Dlugosc slowa {len(word)}")

    def showStartMenu(self):
        print("1. Nowa gra\n2. Zasady gry\n3. Ustawienia\n4. Zakoncz gre")
        response = input()
        self.reload()
        return response

    def show_win_screen(self, is_win, word, num_try):
        self.create_result_of_game(is_win, word, num_try)
        print(self.game_result_str)
        print("Jesli chcesz zapisac wynik kliknij 1")
        want_save = True if input() == "1" else False
        return want_save

    def create_result_of_game(self, is_win, word, num_try):
        header = "Zwyciestwo" if is_win else "Przegrana"
        self.game_result_str = f"{header}\nSlowo:\t{word}\nLiczba prob:\t {num_try}"

    def show_configuration(self, config):
        self.reload()
        print(config)
        gui = None
        diff_lvl = None
        num_try = None
        while True:
            print("1. Zmiana opcji gui\n2. Zmien poziom trudnosci\n3. Zmien liczbe prob\n4. Reset\n5. Wroc")
            choose = input()
            while choose not in ["1", "2", "3", "4", "5"]:
                print("Niestety nie ma takiej opcji")
                choose = input()
            if choose == "1":
                self.reload()
                print("1. Terminal")
                print("2. Window")
                print("3. Wroc")
                gui = input()
                while gui not in ["1", "2", "3"]:
                    print("Nie ma takiej opcji")
                    gui = input()
                self.reload()
                if gui == "1":
                    gui = "terminal"
                elif gui == "2":
                    gui = "window"
                elif gui == "3":
                    gui = None
            elif choose == "2":
                print("1. Easy")
                print("2. Medium")
                print("3. Hard")
                print("4. Wroc")
                diff_lvl = input()
                while diff_lvl not in ["1", "2", "3", "4"]:
                    print("Nie ma takiej opcji")
                    diff_lvl = input()
                self.reload()
                if diff_lvl == "1":
                    diff_lvl = "easy"
                elif diff_lvl == "2":
                    diff_lvl = "medium"
                elif diff_lvl == "3":
                    diff_lvl = "hard"
                elif diff_lvl == "4":
                    diff_lvl = None
            elif choose == "3":
                print("Podaj liczbe calkowita z przedzialu od 1 do 20")
                while True:
                    num_try = input()
                    try:
                        num_try = int(num_try)
                    except ValueError:
                        print("Podano zla liczbe")
                    else:
                        if (num_try < 1 or num_try > 20):
                            print("Podano zla liczbe2")
                        else:
                            break
                self.reload()
            elif choose == "4":
                return (True)
            elif choose == "5":
                break
        return (gui, diff_lvl, num_try)

    def show_game_rule(self):
        self.reload()
        print("""
        Tu bedzie
        opis zasad
        gry
        """)
        input("Nacisinj Enter aby wrocic do menu")

    def no_such_option_mess(self):
        print("Niestety nie ma takiej opcji")

    def file_already_exist(self):
        print("Plik o takiej nazwie juz istnieje.\nJesli chcesz go nadpisac wcisniej 1")
        return True if input() == "1" else False

    def reload(self):
        if os.getenv("PYCHARM_HOSTED"):
            pass
        else:
            if platform.system() == "Windows":
                os.system("cls")
            else:
                os.system("clear")
