import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, Frame
from PIL import Image, ImageTk
import cv2
import sys




def photo_viewer():


    class Store_DATA_IN_INI():

        # OPTION SELECT POP UP CREATION

        def __init__(self, win):


            head_title="CLASS ENVIRONMENT"

            load = cv2.imread('Data/Images/Background/background1.png', 1)
            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            load = Image.fromarray(cv2imagex1)
            regx = tk.Tk()
            load = load.resize((int(regx.winfo_screenwidth()), int(regx.winfo_screenheight())), Image.ANTIALIAS)

            render = ImageTk.PhotoImage(load)
            img = tk.Label(image=render)
            img.image = render
            img.place(x=-1, y=0)


            load = cv2.imread('Data/Images/Background/logo.png', 1)
            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            load = Image.fromarray(cv2imagex1)
            load = load.resize((int(70), int(70)), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(image=render)
            img.image = render
            img.place(x=0, y=700)








            self.b0 = tk.Button(win,
                                bg='#33ff00',
                                fg='#b7f731',
                                relief='flat',
                                width=20)
            self.b0.place(x=0, y=0, width=70, height=70)

            self.b0r = tk.Button(win,
                                bg='#f7421e',
                                fg='#b7f731',
                                relief='flat',
                                width=20,command=self.quit)
            self.b0r.place(x=1300, y=0, width=70, height=70)



            s = ttk.Style()
            s.configure('my.TButton', font=('Aerial', 25, 'bold'))

            self.h0 = ttk.Button(win, text=head_title,style='my.TButton', width=20)
            self.h0.place(x=70, y=-1, width=1232, height=72)



            regx.destroy()

        def quit(self):
            window_user_login3.destroy()
            exit(0)

    window_user_login3 = tk.Tk()
    window_user_login3.config(background='#EFEFEF')
    window_user_login3.attributes('-fullscreen', True)

    user_login_window = Store_DATA_IN_INI(window_user_login3)
    window_user_login3.iconbitmap(default='DATA/Images/icons/favicon.ico')
    window_user_login3.title('INTELEGIX')
    window_user_login3.mainloop()

photo_viewer()