import platform
import os


class TerminalGUI:
    def __init__(self):
        self.num = None
        self.stats = None
        self.l_word = None
        self.name = "terminal"

    def set_guess_result(self, num, stats, l_word):
        self.num = num
        self.stats = stats
        self.l_word = l_word

    def game_screen(self, num, word, stats, not_valid):

        self.set_guess_result(num, stats, len(word))
        self.show_result_of_guess()
        if not_valid:
            print("Niepoprawna odpowiedz sprobuj jeszcze raz")
        return input()

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
        print(f"Dlugosc slowa {self.l_word}")
        print(self.stats)

    @clean_screen
    def show_start_menu(self):
        print("1. Nowa gra\n2. Zasady gry\n3. Ustawienia\n4. Zakoncz gre")
        response = input()
        return response

    @clean_screen
    def show_end_screen(self, is_win, word, num_try):
        self.create_result_of_game(is_win, word, num_try)
        print(self.game_result_str)
        print("Jesli chcesz zapisac wynik kliknij 1")
        want_save = True if input() == "1" else False
        if want_save:
            print("Podaj nazwe pliku")
            return input()

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
            print("1. Zmiana opcji gui\n2. Zmien poziom trudnosci\n3. Zmien liczbe prob\n4. Reset\n5. Wroc")
            choose = input()
            while choose not in ["1", "2", "3", "4", "5"]:
                print("Niestety nie ma takiej opcji")
                choose = input()
            if choose == "1":
                print("1. Terminal")
                print("2. Window")
                print("3. Wroc")
                gui = input()
                while gui not in ["1", "2", "3"]:
                    print("Nie ma takiej opcji")
                    gui = input()
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
                        if num_try < 1 or num_try > 20:
                            print("Podano zla liczbe2")
                        else:
                            break
            elif choose == "4":
                return True
            elif choose == "5":
                break
        return gui, diff_lvl, num_try

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
