import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox, Frame
from PIL import Image, ImageTk
import cv2
import sys
import configparser

def KAIZALA():

    class TOKENS():

        def __init__(self, tokens):
            # Static user Name and Password



            config = configparser.ConfigParser()
            config.read('Data/Keys/config.ini')
            config_token = config.items('TOKEN')

            TOKEN = str(config_token[0][1])
            CHAT_ID = str(config_token[1][1])



            self.lbl = tk.Label(tokens, text="TOKEN", font=("Helvetica", 25, 'bold'), bg='white')
            self.lbl.place(x=60, y=70)

            self.txtfld1 = ttk.Entry(tokens, text='TOKEN', font=("Helvetica", 25, 'bold'))
            self.txtfld1.place(x=220, y=70, width=300)
            self.txtfld1.insert(0,TOKEN)

            self.lb2 = tk.Label(tokens, text="CHAT ID", font=("Helvetica", 25, 'bold'), bg='white')
            self.lb2.place(x=60, y=170)

            self.txtfld2 = ttk.Entry(tokens, text='CHAT_ID', font=("Helvetica", 25, 'bold'))
            self.txtfld2.place(x=220, y=170, width=300)
            self.txtfld2.insert(0,CHAT_ID)



            self.btn = ttk.Button(tokens, text="SUBMIT", width=20, command=self.token_validate)
            self.btn.place(x=270, y=250, width=250, height=60)



        def token_validate(self):
            if (str(self.txtfld1.get()) != "") and (str(self.txtfld2.get()) != ""):
                config = configparser.ConfigParser()
                config.write(r'Data/Keys/config.ini')

                file = open('../Data/Keys/config.ini', "w+")

                config.add_section('TOKEN')
                config.set('TOKEN', 'TOKEN', str(self.txtfld1.get()))
                config.set('TOKEN', 'UP_URL', str(self.txtfld2.get()))


                config.write(file)
                file.close()

                messagebox.showinfo("Success", "API Token Update Succesful")
                tokens_user_login.destroy()




            else:
                tk.messagebox.showerror("Error", "WRONG VALUES")



    tokens_user_login = tk.Tk()
    tokens_user_login.config(background='white')
    tokens_user_login.attributes('-alpha', 0.9)

    user_login_tokens = TOKENS(tokens_user_login)
    tokens_user_login.iconbitmap(default='Data/Images/icons/favicon.ico')
    tokens_user_login.title('TELEGRAM API TOKEN ADMIN')
    tokens_user_login.geometry("600x350")
    tokens_user_login.mainloop()

KAIZALA()