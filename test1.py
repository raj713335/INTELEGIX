import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, Frame
from PIL import Image, ImageTk
import cv2
import sys



def display():
    class Store_DATA_IN_INI():

        # OPTION SELECT POP UP CREATION

        def __init__(self, win):
            load = cv2.imread('Data/Images/Background/background.jpg', 1)
            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            load = Image.fromarray(cv2imagex1)
            regx = tk.Tk()
            load = load.resize(((regx.winfo_screenwidth()), int(regx.winfo_screenheight())), Image.ANTIALIAS)
            regx.destroy()
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
            img.place(x=1115, y=0)

            self.b3 = ttk.Button(win, text='START', width=20)
            self.b3.place(x=15, y=200, width=200, height=50)

            # button_over_ride = ttk.Button(win, height=1, width=1, bg='white', bd=0)
            # button_over_ride.place(x=0, y=1)

    window_user_login1 = tk.Tk()
    window_user_login1.config(background='#EFEFEF')
    window_user_login1.attributes('-fullscreen', True)

    user_login_window = Store_DATA_IN_INI(window_user_login1)
    window_user_login1.iconbitmap(default='DATA/Images/icons/favicon.ico')
    window_user_login1.title('INTELEGIX')


display()