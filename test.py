import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, Frame
from PIL import Image, ImageTk
import cv2
import sys




def second():


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
            load = load.resize((int(250), int(160)), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(image=render)
            img.image = render
            img.place(x=0, y=610)






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
                                width=20)
            self.b0r.place(x=1300, y=0, width=70, height=70)

            # self.b0b = tk.Button(win,
            #                      bg='#33ff00',
            #                      fg='#b7f731',
            #                      relief='flat',
            #                      width=20)
            # self.b0b.place(x=1300, y=700, width=70, height=70)

            self.b1 = ttk.Button(win, text='LIVE', width=20)
            self.b1.place(x=385, y=225, width=250, height=70)

            self.b2 = ttk.Button(win, text='UPLOAD', width=20)
            self.b2.place(x=385, y=325, width=250, height=70)

            self.b3 = ttk.Button(win, text='BROWSE', width=20)
            self.b3.place(x=385, y=425, width=250, height=70)

            # self.b4 = ttk.Button(win, text='School Bus', width=20)
            # self.b4.place(x=1180, y=495, width=170, height=70)
            #
            # self.b5 = ttk.Button(win, text='Corridor Enviroment', width=20)
            # self.b5.place(x=1050, y=380, width=200, height=70)
            #
            # self.b6 = ttk.Button(win, text='START', width=20)
            # self.b6.place(x=1000, y=170, width=200, height=70)

            # button_over_ride = ttk.Button(win, height=1, width=1, bg='white', bd=0)
            # button_over_ride.place(x=0, y=1)

            s = ttk.Style()
            s.configure('my.TButton', font=('Aerial', 25, 'bold'))

            self.h0 = ttk.Button(win, text=head_title,style='my.TButton', width=20)
            self.h0.place(x=70, y=-1, width=1232, height=72)

            regx.destroy()

    window_user_login1 = tk.Tk()
    window_user_login1.config(background='#EFEFEF')
    window_user_login1.attributes('-fullscreen', True)

    user_login_window = Store_DATA_IN_INI(window_user_login1)
    window_user_login1.iconbitmap(default='DATA/Images/icons/favicon.ico')
    window_user_login1.title('INTELEGIX')
    window_user_login1.mainloop()

second()