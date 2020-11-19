import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox, Frame
from PIL import Image, ImageTk
import cv2
import os
import configparser
import sys





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

    for i in range(0, 1):
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
                self.btn.place(x=330, y=330, width=200, height=50)

                self.btn_quit = ttk.Button(window, text="QUIT", width=20, command=self.quit)
                self.btn_quit.place(x=60, y=330, width=200, height=50)

            '''
            validating username and password and if validated move to next page
            '''

            def validate(self):
                if (str(self.txtfld1.get()) in self.UID) and (str(self.txtfld2.get()) in self.PWD):

                    user_name = str(self.txtfld1.get())
                    window_user_login.destroy()

                    display(user_key=user_name)




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




    def display(user_key=str(0)):




        class Store_DATA_IN_INI():

            # OPTION SELECT POP UP CREATION

            def __init__(self, win):




                load = cv2.imread('Data/Images/Background/background.jpg', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                regx=tk.Tk()
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
                img.place(x=1115, y=0)


                self.b0 = tk.Button(win,
                bg='#f7421e',
                fg='#b7f731',
                relief='flat',
                width=20,command=self.quit)
                self.b0.place(x=0, y=0, width=70, height=70)

                self.b0b = tk.Button(win,
                                    bg='#33ff00',
                                    fg='#b7f731',
                                    relief='flat',
                                    width=20,command=self.settings)
                self.b0b.place(x=1300, y=700, width=70, height=70)



                self.b1 = ttk.Button(win, text='Class Environment', width=20,command=self.classs)
                self.b1.place(x=15, y=275, width=175, height=70)

                self.b2 = ttk.Button(win, text='Hostel Envionment', width=20,command=self.hostel)
                self.b2.place(x=90, y=490, width=250, height=70)

                self.b3 = ttk.Button(win, text='Online Assignment', width=20,command=self.exam)
                self.b3.place(x=300, y=660, width=250, height=70)

                self.b4 = ttk.Button(win, text='School Bus', width=20,command=self.bus)
                self.b4.place(x=1180, y=495, width=170, height=70)

                self.b5 = ttk.Button(win, text='Corridor Environment', width=20,command=self.corridor)
                self.b5.place(x=1050, y=380, width=200, height=70)

                self.b6 = ttk.Button(win, text='SETTINGS', width=20,command=self.settings)
                self.b6.place(x=1000, y=170, width=200, height=70)



                # button_over_ride = ttk.Button(win, height=1, width=1, bg='white', bd=0)
                # button_over_ride.place(x=0, y=1)

                regx.destroy()


            def settings(self):

                class TOKENS():

                    def __init__(self, tokens):



                        config = configparser.ConfigParser()
                        config.read('Data/Keys/config.ini')
                        config_token = config.items('TOKEN')
                        TOKEN = str(config_token[0][1])
                        UP_URL = str(config_token[1][1])


                        self.lbl = tk.Label(tokens, text="TOKEN", font=("Helvetica", 30, 'bold'), bg='white')
                        self.lbl.place(x=60, y=70)

                        self.txtfld1 = ttk.Combobox(tokens, values=TOKEN, font=("Helvetica", 30, 'bold'))
                        self.txtfld1.place(x=220, y=70, width=350)
                        self.txtfld1.set(TOKEN)

                        self.lb2 = tk.Label(tokens, text="BOT", font=("Helvetica", 30, 'bold'), bg='white')
                        self.lb2.place(x=60, y=170)

                        self.txtfld2 = ttk.Combobox(tokens, values=UP_URL, font=("Helvetica", 30, 'bold'))
                        self.txtfld2.place(x=220, y=170, width=350)
                        self.txtfld2.set(UP_URL)



                        self.btn = ttk.Button(tokens, text="SUBMIT", width=20, command=self.token_validate)
                        self.btn.place(x=340, y=250, width=230, height=50)

                        # self.btn_quit = ttk.Button(tokens, text="QUIT", command=self.quit)
                        # self.btn_quit.place(x=875, y=-1)

                    def token_validate(self):
                        if (str(self.txtfld1.get()) != "") and (str(self.txtfld2.get()) != ""):

                            config = configparser.ConfigParser()
                            config.write('Data/Keys/config.ini')

                            file = open('Data/Keys/config.ini', "w+")

                            config.add_section('TOKEN')
                            config.set('TOKEN', 'TOKEN', str(self.txtfld1.get()))
                            config.set('TOKEN', 'UP_URL', str(self.txtfld2.get()))


                            config.write(file)
                            file.close()

                            tk.messagebox.showinfo("Success", "Updated Successfully")

                            tokens_user_login.destroy()





                        else:
                            tk.messagebox.showerror("Error", "EMPTY VALUES")

                    def quit(self):
                        tokens_user_login.destroy()

                tokens_user_login = tk.Tk()
                tokens_user_login.config(background='white')
                tokens_user_login.attributes('-alpha', 0.9)

                user_login_tokens = TOKENS(tokens_user_login)
                tokens_user_login.iconbitmap(default='DATA/Images/icons/favicon.ico')
                tokens_user_login.title('TELEGRAM ADMIN ' + version)
                tokens_user_login.geometry("650x350")
                tokens_user_login.mainloop()

            def quit(self):
                window_user_login1.destroy()
                exit(0)

            def classs(self):
                window_user_login1.destroy()
                second(user_key=user_key,job="EXAM ENVIRONMENT")

            def hostel(self):
                window_user_login1.destroy()
                second(user_key=user_key,job="HOSTEL ENVIRONMENT")


            def bus(self):
                window_user_login1.destroy()
                second(user_key=user_key,job="BUS ENVIRONMENT")

            def exam(self):
                window_user_login1.destroy()
                second(user_key=user_key,job="EXAM ENVIRONMENT")

            def corridor(self):
                window_user_login1.destroy()
                second(user_key=user_key,job="CORRIDOR ENVIRONMENT")

            def start(self):
                window_user_login1.destroy()
                second(user_key=user_key,job="START ENVIRONMENT")







        window_user_login1 = tk.Tk()
        window_user_login1.config(background='#EFEFEF')
        window_user_login1.attributes('-fullscreen', True)

        user_login_window = Store_DATA_IN_INI(window_user_login1)
        window_user_login1.iconbitmap(default='DATA/Images/icons/favicon.ico')
        window_user_login1.title('INTELEGIX')
        window_user_login1.mainloop()






    def second(user_key=str(0),job=str(0)):

        class Store_DATA_IN_INI():

            # OPTION SELECT POP UP CREATION

            def __init__(self, win):
                head_title = job

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
                                    width=20,command=self.back)
                self.b0.place(x=0, y=0, width=70, height=70)

                self.b0r = tk.Button(win,
                                     bg='#f7421e',
                                     fg='#b7f731',
                                     relief='flat',
                                     width=20,command=self.quit)
                self.b0r.place(x=1300, y=0, width=70, height=70)

                if job == "HOSTEL ENVIRONMENT":
                    self.txtfld1 = ttk.Combobox(win, font=("Helvetica", 20), justify='center',
                                                state='readonly',value=[str("0"+str(x)+":00:00")[-8:] for x in range(0,24)])
                    self.txtfld1.place(x=800,y=225,height=50,width=200)
                    self.txtfld1.set("00:00:00")

                    self.txtfld2 = ttk.Combobox(win, font=("Helvetica", 20), justify='center', state='readonly',
                                                value=[str("0"+str(x)+":00:00")[-8:] for x in range(0, 24)])
                    self.txtfld2.place(x=1100, y=225,height=50,width=200)
                    self.txtfld2.set("00:00:00")

                if job == "CORRIDOR ENVIRONMENT":
                    self.txtfld1 = ttk.Combobox(win, font=("Helvetica", 20), justify='center',
                                                state='readonly',value=['man','woman'])
                    self.txtfld1.place(x=800,y=225,height=50,width=200)


                    # self.txtfld2 = ttk.Combobox(win, font=("Helvetica", 20), justify='center', state='readonly',
                    #                             value=[str("0"+str(x)+":00:00")[-8:] for x in range(0, 24)])
                    # self.txtfld2.place(x=1100, y=225,height=50,width=200)
                    # self.txtfld2.set("00:00:00")

                # self.b0b = tk.Button(win,
                #                      bg='#33ff00',
                #                      fg='#b7f731',
                #                      relief='flat',
                #                      width=20)
                # self.b0b.place(x=1300, y=700, width=70, height=70)

                self.b1 = ttk.Button(win, text='LIVE', width=20,command=self.run_live)
                self.b1.place(x=285, y=225, width=450, height=70)

                self.b2 = ttk.Button(win, text='UPLOAD', width=20,command=self.browse_file)
                self.b2.place(x=285, y=325, width=450, height=70)

                self.b3 = ttk.Button(win, text='SAVED DATA', width=20,command=self.check_saved)
                self.b3.place(x=285, y=425, width=450, height=70)

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

                self.h0 = ttk.Button(win, text=head_title, style='my.TButton', width=20)
                self.h0.place(x=70, y=-1, width=1232, height=72)

                regx.destroy()

            def check_saved(self):

                window_user_login2.destroy()
                photo_viewer(job)

            def browse_file(self):
                window_user_login2.filename = filedialog.askopenfilename(initialdir="/", title="Upload Video file",
                                                                filetypes=(
                                                                ("video files", "*.mp4"),("Video files", "*.mp4")))
                print(window_user_login2.filename)

                if job=="EXAM ENVIRONMENT":

                    from ENGINES.AI_ONLINE_EXAM_PROCTORING import AI_PROCTORING
                    AI_PROCTORING.AI_PROCTORING(str(window_user_login2.filename))

                if job=="BUS ENVIRONMENT":

                    from ENGINES.AI_DRIVER_MONITORING_SYSTEM import AI_DRIVER_MONITORING
                    AI_DRIVER_MONITORING.AI_DRIVER_MONITORING(str(window_user_login2.filename))

                if job=="HOSTEL ENVIRONMENT":

                    from ENGINES.AI_Hostel_Environment_Monitoring import AI_HOSTEL_ENVIRONMENT
                    AI_HOSTEL_ENVIRONMENT.hostel_enviornment(path=str(window_user_login2.filename),start=str(self.txtfld1.get()),end=str(self.txtfld2.get()))


                if job=="CORRIDOR ENVIRONMENT":

                    from ENGINES.AI_Washroom_Corridor_Environment_Monitoring import AI_Washroom_Corridor_ENVIRONMENT
                    AI_Washroom_Corridor_ENVIRONMENT.corridor_enviornment(path=str(window_user_login2.filename),gender=str(self.txtfld1.get()))

            def run_live(self):

                if job=="EXAM ENVIRONMENT":

                    from ENGINES.AI_ONLINE_EXAM_PROCTORING import AI_PROCTORING
                    AI_PROCTORING.AI_PROCTORING(0)

                if job=="BUS ENVIRONMENT":

                    from ENGINES.AI_DRIVER_MONITORING_SYSTEM import AI_DRIVER_MONITORING
                    AI_DRIVER_MONITORING.AI_DRIVER_MONITORING(0)

                if job=="HOSTEL ENVIRONMENT":

                    from ENGINES.AI_Hostel_Environment_Monitoring import AI_HOSTEL_ENVIRONMENT
                    AI_HOSTEL_ENVIRONMENT.hostel_enviornment(path=0,start=str(self.txtfld1.get()),end=str(self.txtfld2.get()))


                if job=="CORRIDOR ENVIRONMENT":

                    from ENGINES.AI_Washroom_Corridor_Environment_Monitoring import AI_Washroom_Corridor_ENVIRONMENT
                    AI_Washroom_Corridor_ENVIRONMENT.corridor_enviornment(path=0,gender=str(self.txtfld1.get()))



            def quit(self):
                window_user_login2.destroy()
                exit(0)

            def back(self):
                window_user_login2.destroy()
                display(user_key=user_key)

        window_user_login2 = tk.Tk()
        window_user_login2.config(background='#EFEFEF')
        window_user_login2.attributes('-fullscreen', True)

        user_login_window = Store_DATA_IN_INI(window_user_login2)
        window_user_login2.iconbitmap(default='DATA/Images/icons/favicon.ico')
        window_user_login2.title('INTELEGIX')
        window_user_login2.mainloop()

    def photo_viewer(pathx='NULL'):

        class Store_DATA_IN_INI():

            # OPTION SELECT POP UP CREATION

            def __init__(self, win):

                head_title = pathx

                print(head_title)

                listx = []

                iter = 0

                path='Data/Saved_Images/'+str(head_title).replace(" ","_")

                print(path)

                for dirname, _, filenames in os.walk(path):
                    for filename in filenames:
                        print(path + '/' + filename)
                        listx.append(str(path + '/' + filename))

                load = cv2.imread('Data/Images/Background/logo.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(70), int(70)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=0, y=700)

                img1 = tk.Label(image=render)
                img1.image = render

                img1.place(x=1296, y=700)

                print(listx)

                listx = sorted(listx, reverse=True)

                print(listx)


                def image_viewer(iter, key=0):

                    print("ft", iter)

                    if iter > len(listx) - 1:
                        iter = len(listx) - 1

                    if iter <= -1:
                        iter = 0

                    print(iter)

                    try:
                        img.destroy()
                    except:
                        pass

                    load = cv2.imread(listx[iter], 1)
                    cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                    load = Image.fromarray(cv2imagex1)
                    regx = tk.Tk()
                    load = load.resize((int(regx.winfo_screenwidth()) - 140, int(regx.winfo_screenheight()) - 70),
                                       Image.ANTIALIAS)

                    render = ImageTk.PhotoImage(load)
                    img = tk.Label(image=render)
                    img.image = render
                    img.place(x=70, y=70)

                    regx.destroy()

                    if key == 2:

                        try:
                            self.forward_right.destroy()
                            self.forward_right = ttk.Button(win, text=">", style='my.TButton', width=20,
                                                            command=lambda: image_viewer(iter + 1, key=2))
                            self.forward_right.place(x=1296, y=70, width=74, height=632)
                        except:
                            pass

                        try:
                            self.back_left.destroy()

                            self.back_left = ttk.Button(win, text="<", style='my.TButton', width=20,
                                                        command=lambda: image_viewer(iter - 1, key=1))
                            self.back_left.place(x=0, y=70, width=74, height=632)
                        except:
                            pass

                    if key == 1:
                        try:
                            self.back_left.destroy()

                            self.back_left = ttk.Button(win, text="<", style='my.TButton', width=20,
                                                        command=lambda: image_viewer(iter - 1, key=1))
                            self.back_left.place(x=0, y=70, width=74, height=632)
                        except:
                            pass

                        try:
                            self.forward_right.destroy()
                            self.forward_right = ttk.Button(win, text=">", style='my.TButton', width=20,
                                                            command=lambda: image_viewer(iter + 1, key=2))
                            self.forward_right.place(x=1296, y=70, width=74, height=632)
                        except:
                            pass

                    return iter

                image_viewer(iter)



                self.b0 = tk.Button(win,
                                    bg='#33ff00',
                                    fg='#b7f731',
                                    relief='flat',
                                    width=20,command=self.back)
                self.b0.place(x=0, y=0, width=70, height=70)

                self.b0r = tk.Button(win,
                                     bg='#f7421e',
                                     fg='#b7f731',
                                     relief='flat',
                                     width=20, command=self.quit)
                self.b0r.place(x=1296, y=0, width=70, height=70)

                s = ttk.Style()
                s.configure('my.TButton', font=('Aerial', 25, 'bold'))

                self.back_left = ttk.Button(win, text="<", style='my.TButton', width=20,
                                            command=lambda: image_viewer(iter - 1, key=1))
                self.back_left.place(x=0, y=70, width=74, height=632)

                self.forward_right = ttk.Button(win, text=">", style='my.TButton', width=20,
                                                command=lambda: image_viewer(iter + 1, key=2))
                self.forward_right.place(x=1296, y=70, width=74, height=632)

                self.h0 = ttk.Button(win, text=head_title, style='my.TButton', width=20)
                self.h0.place(x=70, y=-1, width=1226, height=72)



            def quit(self):
                window_user_login3.destroy()
                exit(0)

            def back(self):
                window_user_login3.destroy()
                display()



        window_user_login3 = tk.Tk()
        window_user_login3.config(background='#EFEFEF')
        window_user_login3.attributes('-fullscreen', True)

        user_login_window = Store_DATA_IN_INI(window_user_login3)
        window_user_login3.iconbitmap(default='DATA/Images/icons/favicon.ico')
        window_user_login3.title('INTELEGIX')
        window_user_login3.mainloop()





    user_login_over_ride()




if __name__ == '__main__':
    '''
    The main fuction that will loop the program from start to end 
    '''
    main()