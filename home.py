import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, Frame
from PIL import Image, ImageTk
import cv2
import sys



class quitButton(ttk.Button):
    def __init__(self, parent):
        ttk.Button.__init__(self, parent)
        self['text'] = 'Good Bye'
        # Command to close the window (the destory method)
        self['command'] = parent.destroy
        self.pack(side='bottom')


class CreateToolTip(object):
    """
    create a tooltip for a given widget of delete button
    """

    def __init__(self, widget, text='widget info'):
        self.waittime = 500  # miliseconds
        self.wraplength = 180  # pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                         background="#ffffff", relief='solid', borderwidth=1,
                         wraplength=self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()


'''
The main fuction that will loop the program from start to end 
'''

version='1.0.1'

def main():


    regwindowx = tk.Tk()
    screen_widthx = regwindowx.winfo_screenwidth()
    # screen_heightx = regwindowx.winfo_screenheight()
    regwindowx.destroy()


    def loading():
        rootx = tk.Tk()
        rootx.iconbitmap(default='Data/Images/icons/favicon.ico')
        # The image must be stored to Tk or it will be garbage collected.
        rootx.image = tk.PhotoImage(file='Data/Images/Background/load.gif')
        labelx = tk.Label(rootx, image=rootx.image, bg='white')
        rootx.overrideredirect(True)
        rootx.geometry("+270+10")
        # root.lift()
        rootx.wm_attributes("-topmost", True)
        rootx.wm_attributes("-disabled", True)
        rootx.wm_attributes("-transparentcolor", "white")
        labelx.pack()
        labelx.after(500, lambda: labelx.destroy())
        rootx.after(500, lambda: rootx.destroy())  # Destroy the widget after 0.5 seconds
        labelx.mainloop()

    for i in range(0, 3):
        loading()

    def user_login_over_ride():



        class User_Login():

            """
            The login window that ask user for password and id , and validates then to move to the second page
            """

            def __init__(self, window):

                self.UID = []
                self.PWD = []

                '''read username and password from text file stored in DATA/PRIVATE/passkey.txt'''
                with open('DATA/Keys/passkey.txt', 'r') as fh:
                    all_lines = fh.readlines()
                    for each in all_lines:
                        x, y = list(map(str, each.split(",")))
                        x = str(x).replace("\n", "")
                        y = str(y).replace("\n", "")
                        self.UID.append(x)
                        self.PWD.append(y)

                self.lbl = tk.Label(window, text="User", font=("Helvetica", 20), bg='#EFEFEF')
                self.lbl.place(x=60, y=90)

                self.txtfld1 = ttk.Entry(window, text="Enter UID", font=("Helvetica", 20))
                self.txtfld1.place(x=220, y=90)

                self.lb2 = tk.Label(window, text="Password", font=("Helvetica", 20), bg='#EFEFEF')
                self.lb2.place(x=60, y=220)

                self.txtfld2 = ttk.Entry(window, text="Enter Password", show="*", font=("Helvetica", 20))
                self.txtfld2.place(x=220, y=220)

                self.btn = ttk.Button(window, text="LOGIN", width=20, command=self.validate)
                self.btn.place(x=60, y=330, width=200, height=50)

                self.btn_quit = ttk.Button(window, text="QUIT", width=20, command=self.quit)
                self.btn_quit.place(x=330, y=330, width=200, height=50)

            '''
            validating username and password and if validated move to next page
            '''

            def validate(self):
                if (str(self.txtfld1.get()) in self.UID) and (str(self.txtfld2.get()) in self.PWD):

                    user_name = str(self.txtfld1.get())
                    window_user_login.destroy()

                    display()




                else:
                    messagebox.showerror("Error", "INVALID CREDENTIALS")

            def quit(self):
                window_user_login.destroy()
                exit(0)

        window_user_login = tk.Tk()
        window_user_login.config(background='#EFEFEF')
        window_user_login.attributes('-alpha', 0.97)

        user_login_window = User_Login(window_user_login)
        window_user_login.iconbitmap(default='DATA/Images/icons/favicon.ico')
        window_user_login.title('Admin Login')
        window_user_login.geometry("600x450")

        def exitx():
            exit(0)

        window_user_login.protocol('WM_DELETE_WINDOW', exitx)
        window_user_login.mainloop()




    def display():




        class Store_DATA_IN_INI():

            # OPTION SELECT POP UP CREATION

            def __init__(self, win):
                load = cv2.imread('Data/Images/Background/background.jpg', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                regx=tk.Tk()
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





    user_login_over_ride()




if __name__ == '__main__':
    '''
    The main fuction that will loop the program from start to end 
    '''
    main()