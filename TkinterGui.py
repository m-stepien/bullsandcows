from tkinter import *
from tkinter.ttk import *


class TkinterGui:
    def __init__(self):
        self.root = Tk()
        self.root.title("Bulls and Cows")
        self.root.geometry("400x200")
        self.root.iconbitmap("resource/icon.ico")
        self.opt = None

    def go_to_next(self, value):
        print(value)
        char = value.widget.get()
        if value.keycode == 13:
            print("Sending")
        if len(char) > 1:
            char = char[-1]
            value.widget.delete(0, END)
            value.widget.insert(0, char)
        if value.keycode != 9:
            value.widget.tk_focusNext().focus()

    def choose_option(self, opt):
        self.opt = opt
        self.root.quit()

    def stay_active(self):
        self.root.mainloop()

    def game_screen(self, try_remind, word, result):

        fr_button = Frame(self.root, width=25, height=15)
        photo = PhotoImage(file="resource/back_arr.png")
        photoimage = photo.subsample(30, 30)
        button_back = Button(fr_button, command=lambda: self.get_back_to_menu(word_fr,frame_try_rem,label_try_rem,frame_result,label_result, frame_button,button_send,fr_button,button_back),
                             image=photoimage)
        fr_button.pack(side=TOP, anchor=NW)
        button_back.pack()
        frame_try_rem = Frame(self.root, width=20, height=2)
        label_try_rem = Label(frame_try_rem, text=f"Try remind:\t {try_remind}")
        frame_try_rem.pack(side=TOP, anchor=NW)
        label_try_rem.pack()
        frame_result = Frame(self.root, width=20,height=2)
        label_result = Label(frame_result, text=result)
        frame_result.pack(side=TOP, anchor=NW)
        label_result.pack()
        word_fr = self.show_len_of_word("abct")
        frame_button = Frame(self.root)
        button_send = Button(frame_button, command=self.send, text="Wyslij")
        frame_button.pack(side=RIGHT, anchor=SE, padx=5,pady=5)
        button_send.pack()

        self.stay_active()
    def send(self):
        pass
    def show_game_rule(self):
        GAME_RULE = 'Tu beda zapisane zasady gry\nCiekawe czy \\ndziala'
        fr_info = Frame(self.root, width=400, height=185)
        info = Label(fr_info, text=GAME_RULE, justify=CENTER, anchor=CENTER)
        fr_button = Frame(self.root, width=25, height=15)
        photo = PhotoImage(file="resource/back_arr.png")
        photoimage = photo.subsample(30, 30)
        button_back = Button(fr_button, command=lambda: self.get_back_to_menu(fr_info, info, fr_button, button_back),
                             image=photoimage)
        fr_button.pack(side=TOP, anchor=NW)
        button_back.pack()
        fr_info.pack(fill=BOTH, expand=True)
        info.pack(fill=BOTH, expand=True)
        self.stay_active()

    def show_len_of_word(self, word):
        word_frame = Frame(self.root, height=20)
        char_frame = []
        char_label = []
        for ch in range(len(word)):
            fr = Frame(word_frame)
            char_frame.append(fr)
            fr.pack(side=LEFT, fill=BOTH, expand=True)
            ent = Entry(fr, text="_", font=("Arial", 25), width=1, textvariable=f"side{ch}")
            char_label.append(ent)
            ent.pack()
            ent.bind("<KeyRelease>", self.go_to_next)

        word_frame.pack(fill=X, expand=True)

        return word_frame

    def get_back_to_menu(self, *args):
        self.opt = None
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
