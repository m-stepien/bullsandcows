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
        response = int(input())
        self.reload()
        return response

    def show_end_screen(self, is_win, word, num_try):
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

    def reload(self):
        if os.getenv("PYCHARM_HOSTED"):
            pass
        else:
            if platform.system() == "Windows":
                os.system("cls")
            else:
                os.system("clear")
