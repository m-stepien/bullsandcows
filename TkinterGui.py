from tkinter import *
from tkinter.ttk import *


class TkinterGui:
    def __init__(self):
        self.root = Tk()
        self.name = "window"
        self.root.title("Bulls and Cows")
        self.root.geometry("400x320")
        self.root.iconbitmap("resource/icon.ico")
        self.opt = None
        self.answer = None
        self.fr_valid = None
        self.is_game_screen = False
        self.want_save_option = False
        self.IGNORE_KEY = (27, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123,
                           44, 46, 8, 16, 37, 38, 39, 40, 17, 18, 91, 20, 9)

    def create_result_of_game(self, is_win, word, i):
        header = "Zwyciestwo" if is_win else "Przegrana"
        self.game_result_str = f"{header}\nSlowo:\t{word}\nLiczba prob:\t {i}"

    def show_end_screen(self, is_win, word, i):
        self.is_game_screen = False
        fr_button = Frame(self.root, width=25, height=15)
        photo = PhotoImage(file="resource/back_arr.png")
        photoimage = photo.subsample(30, 30)
        x = lambda: self.destroy_elems(fr_button, button_back, fr_end_result, label_end_result,
                                       entry_file_name, label_info_save, button_save, frame_to_save)
        button_back = Button(fr_button, command=lambda: self.get_back_to_menu(x),
                             image=photoimage)
        fr_button.pack(side=TOP, anchor=NW)
        button_back.pack()
        self.create_result_of_game(is_win, word, i)
        fr_end_result = Frame(self.root)
        label_end_result = Label(fr_end_result, text=self.game_result_str, justify=CENTER)
        fr_end_result.pack(fill=BOTH, expand=True, pady=20)
        label_end_result.pack()
        frame_to_save = Frame(self.root)
        label_info_save = Label(frame_to_save, text="Jesli chcesz zapisac wynik\npodaj nazwe pliku i kliknij zapisz")
        entry_file_name = Entry(frame_to_save, font=("Arial", 15), justify=CENTER)
        button_save = Button(frame_to_save, text="Zapisz", command=lambda: self.ret_file_name(x, entry_file_name))
        label_info_save.pack(side=TOP)
        entry_file_name.pack(side=LEFT, pady=10, padx=5)
        button_save.pack(side=LEFT, pady=10, padx=5)
        frame_to_save.pack(side=BOTTOM)
        self.file_name = entry_file_name.get()
        self.stay_active()
        return self.file_name

    def ret_file_name(self, exp, ent):
        self.file_name = ent.get()
        exp()

    def enter_handler(self, event):
        if self.is_game_screen:
            x = lambda: self.destroy_elems(*self.root.winfo_children())
            self.send(x)

    def go_to_next(self, value):
        char = value.char
        value.widget.delete(0, END)
        value.widget.insert(0, char)
        if value.keycode not in self.IGNORE_KEY:
            value.widget.tk_focusNext().focus()

    def choose_option(self, opt):
        self.opt = opt
        self.root.quit()

    def stay_active(self):
        self.root.mainloop()

    def game_screen(self, try_remind, word, result, not_valid):
        self.is_game_screen = True
        fr_button = Frame(self.root, width=25, height=15)
        photo = PhotoImage(file="resource/back_arr.png")
        photoimage = photo.subsample(30, 30)
        x = lambda: self.destroy_elems(word_fr, frame_try_rem, label_try_rem, frame_result, label_result, frame_button,
                                       button_send, fr_button, button_back)
        button_back = Button(fr_button, command=lambda: self.get_back_to_menu(x), image=photoimage)
        fr_button.pack(side=TOP, anchor=NW)
        button_back.pack()
        frame_try_rem = Frame(self.root, width=20, height=2)
        label_try_rem = Label(frame_try_rem, text=f"Try remind:\t {try_remind}")
        frame_try_rem.pack(side=TOP, anchor=NW)
        label_try_rem.pack()
        frame_result = Frame(self.root, width=20, height=2)
        label_result = Label(frame_result, text=result)
        frame_result.pack(side=TOP, anchor=NW)
        label_result.pack()

        if not_valid:
            self.fr_valid = Frame(self.root)
            self.lb_valid = Label(self.fr_valid, text="Nie mozna udzielic takiej odpowiedzi")
            self.fr_valid.pack(side=TOP)
            self.lb_valid.pack()

        word_fr = self.show_len_of_word(word)
        frame_button = Frame(self.root)
        button_send = Button(frame_button, command=lambda: self.send(x), text="Wyslij")
        frame_button.pack(side=RIGHT, anchor=SE, padx=5, pady=5)
        button_send.pack()
        self.root.bind("<Return>", self.enter_handler)
        self.stay_active()
        return self.answer

    def send(self, exp):
        answer = ""
        for entry in self.char_entry:
            answer += entry.get()

        exp()
        self.answer = answer

    def show_game_rule(self):
        GAME_RULE = """
        Tekstowa gra w wktorej komputer (Host)
        losuje slowo, ktore jest izogramem (izogram
        jest to wyraz w ktorym nie powtarzaja sie
        zadne litery) i informuje uzytkownika 
        (Guesser) o ilosci liter w slowie. 
        Uzytkownik (Guesser) stara sie zgadnac co 
        to za slowo. Komputer (Host) po kazdej 
        probie zwraca liczbe Cows & Bulls. Liczba
        przy slowie Cows oznacza litere wystepujaca
        w slowie lecz na zlej pozycji, liczba przy
        slowie Bulls oznacza poprawna litere na 
        poprawnej pozycji. Gra konczy sie kiedy 
        liczba przy Bulls bedzie taka sama jak 
        dlugosc slowa wylosowanego przez komputer.
        """
        fr_info = Frame(self.root)
        info = Label(fr_info, text=GAME_RULE, font=("Arial", 12), justify=CENTER, anchor=CENTER)
        fr_button = Frame(self.root, width=25, height=15)
        photo = PhotoImage(file="resource/back_arr.png")
        photoimage = photo.subsample(30, 30)
        x = lambda: self.destroy_elems(fr_info, info, fr_button, button_back)
        button_back = Button(fr_button, command=lambda: self.get_back_to_menu(x),
                             image=photoimage)
        fr_button.pack(side=TOP, anchor=NW)
        button_back.pack()
        fr_info.pack(fill=BOTH, expand=True)
        info.pack(fill=BOTH, expand=True)
        self.stay_active()

    def show_len_of_word(self, word):
        word_frame = Frame(self.root, height=20)
        char_frame = []
        self.char_entry = []
        for ch in range(len(word)):
            fr = Frame(word_frame)
            char_frame.append(fr)
            fr.pack(side=LEFT, fill=BOTH, expand=True)
            ent = Entry(fr, font=("Arial", 25), width=1, justify=CENTER)
            self.char_entry.append(ent)
            ent.pack(ipadx=5, ipady=3)
            ent.bind("<KeyRelease>", self.go_to_next)

        word_frame.pack(fill=X, expand=True)

        return word_frame

    def destroy_elems(self, *args):
        for arg in args:
            arg.destroy()
        self.root.quit()

    def get_back_to_menu(self, exp):
        self.opt = None
        if self.fr_valid:
            self.fr_valid.destroy()
            self.lb_valid.destroy()
        exp()

    def show_start_menu(self):
        self.is_game_screen = False
        fr_bt1 = Frame(self.root, width=400, height=50)
        fr_bt2 = Frame(self.root, width=400, height=50)
        fr_bt3 = Frame(self.root, width=400, height=50)
        fr_bt4 = Frame(self.root, width=400, height=50)

        bt1 = Button(fr_bt1, text="Nowa gra", command=lambda: self.choose_option("1"))
        bt2 = Button(fr_bt2, text="Zasady gry", command=lambda: self.choose_option("2"))
        bt3 = Button(fr_bt3, text="Ustawienia", command=lambda: self.choose_option("3"))
        bt4 = Button(fr_bt4, text="Zakoncz gre", command=lambda: self.choose_option("4"))
        fr_bt1.pack(fill=BOTH, expand=True)
        fr_bt2.pack(fill=BOTH, expand=True)
        fr_bt3.pack(fill=BOTH, expand=True)
        fr_bt4.pack(fill=BOTH, expand=True)

        bt1.pack(fill=BOTH, expand=True)
        bt2.pack(fill=BOTH, expand=True)
        bt3.pack(fill=BOTH, expand=True)
        bt4.pack(fill=BOTH, expand=True)
        self.stay_active()
        bt1.destroy()
        bt2.destroy()
        bt3.destroy()
        bt4.destroy()
        fr_bt1.destroy()
        fr_bt2.destroy()
        fr_bt3.destroy()
        fr_bt4.destroy()
        self.root.update_idletasks()
        self.root.update()
        return self.opt

    def send_option(self, func):
        self.want_save_option = True
        func()

    def show_configuration(self, config):
        self.want_save_option = False
        fr_button = Frame(self.root, width=25, height=15)
        photo = PhotoImage(file="resource/back_arr.png")
        photoimage = photo.subsample(30, 30)
        x = lambda: self.destroy_elems(button_back, fr_button, fr_current_config, fr_config_option)
        button_back = Button(fr_button, command=lambda: self.get_back_to_menu(x),
                             image=photoimage)
        fr_button.pack(side=TOP, anchor=NW)
        button_back.pack()
        fr_current_config = Frame(self.root)
        label_title = Label(fr_current_config, text="KONFIGURACJA", font=("Arial", 13))
        label_gui = Label(fr_current_config, text="Rodzaj GUI {}".format(config.gui))
        label_diff_level = Label(fr_current_config, text="Poziom trudnosci {}".format(config.difficulty_level))
        label_num_try = Label(fr_current_config, text="Liczba prob {}".format(config.number_of_try))
        fr_current_config.pack()
        label_title.pack()
        label_gui.pack()
        label_diff_level.pack()
        label_num_try.pack()
        fr_config_option = Frame(self.root)
        self.new_gui_conf = StringVar()
        gui_choose = Combobox(fr_config_option, textvariable=self.new_gui_conf)
        gui_choose['values'] = ("terminal", "window")
        gui_choose.current(1)
        fr_config_option.pack()
        gui_choose.pack()
        self.new_diff_lvl = StringVar()
        diff_lvl_choose = Combobox(fr_config_option, textvariable=self.new_diff_lvl)
        diff_lvl_choose['values'] = ("easy", "medium", "hard")
        diff_lvl_choose.current(0)
        diff_lvl_choose.pack()
        self.new_num_try = StringVar()
        num_try_choose = Combobox(fr_config_option, textvariable=self.new_num_try)
        num_try_choose['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                                    "14", "15", "16", "17", "18", "19", "20")
        num_try_choose.current(0)
        num_try_choose.pack()
        button_send = Button(fr_config_option, text="Zapisz", command=lambda: self.send_option(x))
        button_send.pack(side=RIGHT)
        self.stay_active()
        if self.want_save_option:
            return self.new_gui_conf.get(), self.new_diff_lvl.get(), self.new_num_try.get()
