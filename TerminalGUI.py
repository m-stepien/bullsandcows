import platform
import os


class TerminalGUI:
    def __init__(self):
        self.num = None
        self.stats = None
        self.l_word = None

    def set_guess_result(self, num, stats, l_word):
        self.num = num
        self.stats = stats
        self.l_word = l_word

    def clean_screen(func):
        def with_reload(self, *args):
            if os.getenv("PYCHARM_HOSTED"):
                pass
            else:
                if platform.system() == "Windows":
                    os.system("cls")
                else:
                    os.system("clear")
            if len(args) == 0:
                return func(self)
            else:
                return func(self, *args)

        return with_reload

    @clean_screen
    def show_result_of_guess(self):
        print(f"Try remind:\t{self.num}")
        print(self.stats)
        print(f"Dlugosc slowa {self.l_word}")

    def get_answer(self):
        return input()

    @clean_screen
    def get_file_name(self):
        print("Podaj nazwe pliku")
        return input()

    @clean_screen
    def showStartMenu(self):
        print("1. Nowa gra\n2. Zasady gry\n3. Ustawienia\n4. Zakoncz gre")
        response = input()
        return response

    @clean_screen
    def show_win_screen(self, is_win, word, num_try):
        self.create_result_of_game(is_win, word, num_try)
        print(self.game_result_str)
        print("Jesli chcesz zapisac wynik kliknij 1")
        want_save = True if input() == "1" else False
        return want_save

    def create_result_of_game(self, is_win, word, num_try):
        header = "Zwyciestwo" if is_win else "Przegrana"
        self.game_result_str = f"{header}\nSlowo:\t{word}\nLiczba prob:\t {num_try}"

    @clean_screen
    def show_configuration(self, config):
        print(config)
        gui = None
        diff_lvl = None
        num_try = None
        while True:
            print("1. Zmien poziom trudnosci\n2. Zmien liczbe prob\n3. Reset\n4.Wroc\n")
            choose = input()
            while choose not in ["1", "2", "3", "4", "5"]:
                print("Niestety nie ma takiej opcji")
                choose = input()
            if choose == "1":
                print("1. Easy")
                print("2. Medium")
                print("3. Hard")
                print("4. Wroc")
                diff_lvl = input()
                while diff_lvl not in ["1", "2", "3", "4"]:
                    print("Nie ma takiej opcji")
                    diff_lvl = input()
                if diff_lvl == "1":
                    diff_lvl = "easy"
                elif diff_lvl == "2":
                    diff_lvl = "medium"
                elif diff_lvl == "3":
                    diff_lvl = "hard"
                elif diff_lvl == "4":
                    diff_lvl = None
            elif choose == "2":
                print("Podaj liczbe calkowita z przedzialu od 1 do 20")
                while True:
                    num_try = input()
                    try:
                        num_try = int(num_try)
                    except ValueError:
                        print("Podano zla liczbe")
                    else:
                        if num_try < 1 or num_try > 20:
                            print("Podano zla liczbe")
                        else:
                            break
            elif choose == "3":
                return True
            elif choose == "4":
                break
        return diff_lvl, num_try

    @clean_screen
    def show_game_rule(self):
        print("""
Tekstowa gra w wktorej komputer (Host) losuje slowo, ktore jest izogramem (izogram jest to wyraz
w ktorym nie powtarzaja sie zadne litery) i informuje uzytkownika (Guesser) o ilosci liter
w slowie. Uzytkownik (Guesser) stara sie zgadnac co to za slowo. Komputer (Host) po kazdej probie
zwraca liczbe Cows & Bulls. Liczba przy slowie Cows oznacza litere wystepujaca w slowie lecz na zlej pozycji,
liczba przy slowie Bulls oznacza poprawna litere na poprawnej pozycji. Gra konczy sie kiedy
liczba przy Bulls bedzie taka sama jak dlugosc slowa wylosowanego przez komputer.
        """)
        input("Nacisinj Enter aby wrocic do menu")

    def no_such_option_mess(self):
        print("Niestety nie ma takiej opcji")

    def file_already_exist(self):
        print("Plik o takiej nazwie juz istnieje.\nJesli chcesz go nadpisac wcisniej 1")
        return True if input() == "1" else False
