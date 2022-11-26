from tkinter import *
from tkinter.ttk import *


class TkinterGui:
    def __init__(self):
        self.root = Tk()
        self.root.title("Bulls and Cows")
        self.root.geometry("400x200")
        self.root.iconbitmap("resource/icon.ico")
        self.opt = None

    def choose_option(self, opt):
        self.opt = opt
        self.root.quit()

    def stay_active(self):
        self.root.mainloop()

    def show_game_rule(self):
        print("Ja tu jestem")
        GAME_RULE = 'Tu beda zapisane zasady gry\nCiekawe czy \\ndziala'
        fr_info = Frame(self.root, width=400, height=185)
        info = Label(fr_info, text=GAME_RULE, justify=CENTER, anchor=CENTER)
        fr_button = Frame(self.root, width=25, height=15)
        photo = PhotoImage(file="resource/back_arr.png")
        photoimage = photo.subsample(30, 30)
        button_back = Button(fr_button, command=lambda: self.get_back_to_menu(fr_info,info,fr_button,button_back), image=photoimage)
        fr_button.pack(side=TOP, anchor=NW)
        button_back.pack()
        fr_info.pack(fill=BOTH, expand=True)
        info.pack(fill=BOTH, expand=True)
        self.root.mainloop()


    def get_back_to_menu(self, *args):
        self.opt=None
        for arg in args:
            arg.destroy()
        self.root.quit()

    def showStartMenu(self):
        fr_bt1 = Frame(self.root, width=400, height=50)
        fr_bt2 = Frame(self.root, width=400, height=50)
        fr_bt3 = Frame(self.root, width=400, height=50)
        fr_bt4 = Frame(self.root, width=400, height=50)

        bt1 = Button(fr_bt1, text="Nowa gra", command=lambda: self.choose_option(1))
        bt2 = Button(fr_bt2, text="Zasady gry", command=lambda: self.choose_option(2))
        bt3 = Button(fr_bt3, text="Ustawienia", command=lambda: self.choose_option(3))
        bt4 = Button(fr_bt4, text="Zakoncz gre", command=lambda: self.choose_option(4))
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
