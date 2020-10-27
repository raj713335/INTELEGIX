from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import tkinter.ttk as ttk
from datetime import date
from tkinter import messagebox
import csv
import os









def user_add_kc():
    # CLASS FOR ADDING STATION

    class user_add_kc():

        def __init__(self, window):

            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()

            """shop_floor_canvax = tk.Canvas(window, width=screen_width, height=screen_height, background='white')
            shop_floor_canvax.grid(row=0, column=0)
            shop_floor_canvax.create_line((screen_width // 1.5), 0, (screen_width // 1.5), 750, fill='grey', width=3)
            shop_floor_canvax.create_line(-1, 71, screen_width, 71, fill='grey', width=3)"""

            shop_floor_canvax = tk.Canvas(window, width=screen_width, height=screen_height, background='white')
            shop_floor_canvax.grid(row=0, column=0)
            shop_floor_canvax.create_line(0, 120, 1920, 120, fill='grey', width=2)
            #shop_floor_canvax.create_line(-1, 71, screen_width, 71, fill='grey', width=3)


            # load = cv2.imread('IMAGES/header.png', 1)
            # cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            # load = Image.fromarray(cv2imagex1)
            # load = load.resize((int(1920), int(70)), Image.ANTIALIAS)
            # render = ImageTk.PhotoImage(load)
            # img = tk.Label(image=render)
            # img.image = render
            # img.place(x=-1, y=0)

            self.lb_title = Label(window, text="JDPS Engine", fg='#34943a',
                                  font=("Ariel", 20, 'bold'),bg='white')
            self.lb_title.place(x=10, y=80)

            self.lb_dept = Label(window, text="Dept No.", fg='#34943a',font=("Ariel", 13), bg='white')
            self.lb_dept.place(x=60, y=140)

            self.lb_operator = Label(window, text="Operator Name", fg='#34943a', font=("Ariel", 13), bg='white')
            self.lb_operator.place(x=680, y=140)

            self.lb_station = Label(window, text="Station No.", fg='#34943a', font=("Ariel", 13), bg='white')
            self.lb_station.place(x=1300, y=140)

            self.lb_engine = Label(window, text="Engine Model", fg='#34943a', font=("Ariel", 13), bg='white')
            self.lb_engine.place(x=60, y=240)

            self.lb_Date = Label(window, text="Date", fg='#34943a', font=("Ariel", 13), bg='white')
            self.lb_Date.place(x=680, y=240)

            self.lb_QE_Name = Label(window, text="QE Name", fg='#34943a', font=("Ariel", 13), bg='white')
            self.lb_QE_Name.place(x=1300, y=240)



            self.dept_name = ttk.Combobox(window, text="dept_name",values=["566","570","564","569"],font=("Ariel", 25), width=30)
            self.dept_name.place(x=60, y=170)
            self.dept_name.set("")



            self.operator_name = ttk.Entry(window, text="operator_name", font=("Ariel", 25), width=31)
            self.operator_name.place(x=680, y=170)


            self.station_no = ttk.Entry(window, text="station_no", font=("Ariel", 25), width=31)
            self.station_no.place(x=1300, y=170)


            self.engine_model = ttk.Entry(window, text="engine_model", font=("Ariel", 25), width=31)
            self.engine_model.place(x=60, y=270)


            self.date = ttk.Entry(window, text="date", font=("Ariel", 25), width=31)
            self.date.place(x=680, y=270)

            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            self.date.insert(0,d1)
            self.date.configure(state=DISABLED)


            self.QE_name = ttk.Entry(window, text="QE_name", font=("Ariel", 25), width=31)
            self.QE_name.place(x=1300, y=270)






















            self.l1 = Label(window, text="""Training and Certification""",font=("Ariel", 18),fg='#34943a',bg='white', borderwidth=5, relief="groove")
            self.l1.place(x=60,y=435,height=35,width=565)

            self.l1_data1=Label(window, text="""Training content and certification for the station""",font=("Ariel", 15),fg='#34943a',bg='white', borderwidth=3, relief="groove")
            self.l1_data1.place(x=625, y=435, height=35, width=565)

            def l1_data1_bool1_fun(value):
                if self.l1_data1_bool1_data.get()=="YES":
                    self.l1_data1_bool1 = Label(window, text="""""",
                                          font=("Ariel", 15), fg='#34943a', bg='green', borderwidth=3, relief="groove")
                    self.l1_data1_bool1.place(x=1191, y=435, height=35, width=90)
                    self.l1_data1_comment.delete(0,END)
                    self.l1_data1_comment.configure(state=DISABLED)
                else:
                    self.l1_data1_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='red', borderwidth=3,
                                                relief="groove")
                    self.l1_data1_bool1.place(x=1191, y=435, height=35, width=90)
                    self.l1_data1_comment.configure(state=ACTIVE)




            self.l1_data1_bool1_data = Combobox(window, text="""""",state='readonly',
                                        font=("Ariel", 25),values=["YES","NO"],justify='center')
            self.l1_data1_bool1_data.place(x=1191, y=435, height=35, width=107)

            self.l1_data1_bool1_data.bind("<<ComboboxSelected>>", l1_data1_bool1_fun)

            self.l1_data1_comment = ttk.Entry(window, text="l1_data1", font=("Ariel", 15), width=31)
            self.l1_data1_comment.place(x=1300, y=435, height=35, width=565)






























            self.l2 = Label(window, text="""Assembly Process""", font=("Ariel", 20), fg='#34943a', bg='white',
                            borderwidth=5, relief="groove")
            self.l2.place(x=60, y=470, height=70, width=565)

            self.l2_data1 = Label(window, text="""SOE""",
                                  font=("Ariel", 15), fg='#34943a', bg='white', borderwidth=3, relief="groove")
            self.l2_data1.place(x=625, y=470, height=35, width=565)

            def l2_data1_bool1_fun(value):
                if self.l2_data1_bool1_data.get() == "YES":
                    self.l2_data1_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='green', borderwidth=3,
                                                relief="groove")
                    self.l2_data1_bool1.place(x=1191, y=470, height=35, width=90)
                    self.l2_data1_comment.delete(0, END)
                    self.l2_data1_comment.configure(state=DISABLED)
                else:
                    self.l2_data1_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='red', borderwidth=3,
                                                relief="groove")
                    self.l2_data1_bool1.place(x=1191, y=470, height=35, width=90)
                    self.l2_data1_comment.configure(state=ACTIVE)

            self.l2_data1_bool1_data = Combobox(window, text="""""",state='readonly',
                                                font=("Ariel", 25), values=["YES", "NO"], justify='center')
            self.l2_data1_bool1_data.place(x=1191, y=470, height=35, width=107)

            self.l2_data1_bool1_data.bind("<<ComboboxSelected>>", l2_data1_bool1_fun)

            self.l2_data1_comment = ttk.Entry(window, text="l2_data1", font=("Ariel", 15), width=31)
            self.l2_data1_comment.place(x=1300, y=470, height=35, width=565)



            self.l2_data2 = Label(window, text="""pFMEA""",
                                  font=("Ariel", 15), fg='#34943a', bg='white', borderwidth=3, relief="groove")
            self.l2_data2.place(x=625, y=505, height=35, width=565)

            def l2_data2_bool1_fun(value):
                if self.l2_data2_bool1_data.get() == "YES":
                    self.l2_data2_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='green', borderwidth=3,
                                                relief="groove")
                    self.l2_data2_bool1.place(x=1191, y=505, height=35, width=90)
                    self.l2_data2_comment.delete(0, END)
                    self.l2_data2_comment.configure(state=DISABLED)
                else:
                    self.l2_data2_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='red', borderwidth=3,
                                                relief="groove")
                    self.l2_data2_bool1.place(x=1191, y=505, height=35, width=90)
                    self.l2_data2_comment.configure(state=ACTIVE)

            self.l2_data2_bool1_data = Combobox(window, text="""""",state='readonly',
                                                font=("Ariel", 25), values=["YES", "NO"], justify='center')
            self.l2_data2_bool1_data.place(x=1191, y=505, height=35, width=107)

            self.l2_data2_bool1_data.bind("<<ComboboxSelected>>", l2_data2_bool1_fun)

            self.l2_data2_comment = ttk.Entry(window, text="l2_data2", font=("Ariel", 15), width=31)
            self.l2_data2_comment.place(x=1300, y=505, height=35, width=565)



























            self.l3 = Label(window, text="""WI/Tooling/Gauging""", font=("Ariel", 20), fg='#34943a', bg='white',
                            borderwidth=5, relief="groove")
            self.l3.place(x=60, y=540, height=105, width=565)

            self.l3_data1 = Label(window, text="""Quantity of errors in visual aids (Work Instructions)""",
                                  font=("Ariel", 15), fg='#34943a', bg='white', borderwidth=3, relief="groove")
            self.l3_data1.place(x=625, y=540, height=35, width=565)

            def l3_data1_bool1_fun(value):
                if self.l3_data1_bool1_data.get() == "YES":
                    self.l3_data1_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='green', borderwidth=3,
                                                relief="groove")
                    self.l3_data1_bool1.place(x=1191, y=540, height=35, width=90)
                    self.l3_data1_comment.delete(0,END)
                    self.l3_data1_comment.configure(state=DISABLED)
                else:
                    self.l3_data1_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='red', borderwidth=3,
                                                relief="groove")
                    self.l3_data1_bool1.place(x=1191, y=540, height=35, width=90)
                    self.l3_data1_comment.configure(state=ACTIVE)

            self.l3_data1_bool1_data = Combobox(window, text="""""",state='readonly',
                                                font=("Ariel", 25), values=["YES", "NO"], justify='center')
            self.l3_data1_bool1_data.place(x=1191, y=540, height=35, width=107)

            self.l3_data1_bool1_data.bind("<<ComboboxSelected>>", l3_data1_bool1_fun)

            self.l3_data1_comment = ttk.Entry(window, text="l3_data1", font=("Ariel", 15), width=31)
            self.l3_data1_comment.place(x=1300, y=540, height=35, width=565)



            self.l3_data2 = Label(window, text="Tool Types",
                                  font=("Ariel", 15), fg='#34943a', bg='white', borderwidth=3, relief="groove")
            self.l3_data2.place(x=625, y=575, height=35, width=565)

            def l3_data2_bool1_fun(value):
                if self.l3_data2_bool1_data.get() == "YES":
                    self.l3_data2_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='green', borderwidth=3,
                                                relief="groove")
                    self.l3_data2_bool1.place(x=1191, y=575, height=35, width=90)
                    self.l3_data2_comment.delete(0,END)
                    self.l3_data2_comment.configure(state=DISABLED)
                else:
                    self.l3_data2_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='red', borderwidth=3,
                                                relief="groove")
                    self.l3_data2_bool1.place(x=1191, y=575, height=35, width=90)
                    self.l3_data2_comment.configure(state=ACTIVE)

            self.l3_data2_bool1_data = Combobox(window, text="""""",state='readonly',
                                                font=("Ariel", 25), values=["YES", "NO"], justify='center')
            self.l3_data2_bool1_data.place(x=1191, y=575, height=35, width=107)

            self.l3_data2_bool1_data.bind("<<ComboboxSelected>>", l3_data2_bool1_fun)

            self.l3_data2_comment = ttk.Entry(window, text="l3_data2", font=("Ariel", 15), width=31)
            self.l3_data2_comment.place(x=1300, y=575, height=35, width=565)



            self.l3_data3 = Label(window, text="Calibration validity period",
                                  font=("Ariel", 15), fg='#34943a', bg='white', borderwidth=3, relief="groove")
            self.l3_data3.place(x=625, y=610, height=35, width=565)

            def l3_data3_bool1_fun(value):
                if self.l3_data3_bool1_data.get() == "YES":
                    self.l3_data3_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='green', borderwidth=3,
                                                relief="groove")
                    self.l3_data3_bool1.place(x=1191, y=610, height=35, width=90)
                    self.l3_data3_comment.delete(0, END)
                    self.l3_data3_comment.configure(state=DISABLED)
                else:
                    self.l3_data3_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='red', borderwidth=3,
                                                relief="groove")
                    self.l3_data3_bool1.place(x=1191, y=610, height=35, width=90)
                    self.l3_data3_comment.configure(state=ACTIVE)

            self.l3_data3_bool1_data = Combobox(window, text="""""", state='readonly',
                                                font=("Ariel", 25), values=["YES", "NO"], justify='center')
            self.l3_data3_bool1_data.place(x=1191, y=610, height=35, width=107)

            self.l3_data3_bool1_data.bind("<<ComboboxSelected>>", l3_data3_bool1_fun)

            self.l3_data3_comment = ttk.Entry(window, text="l3_data3", font=("Ariel", 15), width=31)
            self.l3_data3_comment.place(x=1300, y=610, height=35, width=565)















            self.l4 = Label(window, text="""Cleanliness""", font=("Ariel", 18), fg='#34943a', bg='white',
                            borderwidth=5, relief="groove")
            self.l4.place(x=60, y=645, height=35, width=565)

            self.l4_data1 = Label(window, text="""Station complies with John Deere Special Process Audit for (Hydraulic) Cleanliness
Note: Refers to the evaluation of cleanliness for all components in assembly operation - not restricted to hydraulic components""",
                                  font=("Ariel", 7), fg='#34943a', bg='white', borderwidth=3, relief="groove")
            self.l4_data1.place(x=625, y=645, height=35, width=565)

            def l4_data1_bool1_fun(value):
                if self.l4_data1_bool1_data.get() == "YES":
                    self.l4_data1_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='green', borderwidth=3,
                                                relief="groove")
                    self.l4_data1_bool1.place(x=1191, y=645, height=35, width=90)
                    self.l4_data1_comment.delete(0, END)
                    self.l4_data1_comment.configure(state=DISABLED)
                else:
                    self.l4_data1_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='red', borderwidth=3,
                                                relief="groove")
                    self.l4_data1_bool1.place(x=1191, y=645, height=35, width=90)
                    self.l4_data1_comment.configure(state=ACTIVE)

            self.l4_data1_bool1_data = Combobox(window, text="""""", state='readonly',
                                                font=("Ariel", 25), values=["YES", "NO"], justify='center')
            self.l4_data1_bool1_data.place(x=1191, y=645, height=35, width=107)

            self.l4_data1_bool1_data.bind("<<ComboboxSelected>>", l4_data1_bool1_fun)

            self.l4_data1_comment = ttk.Entry(window, text="l4_data1", font=("Ariel", 15), width=31)
            self.l4_data1_comment.place(x=1300, y=645, height=35, width=565)














            self.l5 = Label(window, text="""Short Audit Only""", font=("Ariel", 20), fg='#34943a', bg='white',
                            borderwidth=5, relief="groove")
            self.l5.place(x=60, y=680, height=210, width=565)

            self.l5_data1 = Label(window, text="""Non conformance materail""",
                                  font=("Ariel", 15), fg='#34943a', bg='white', borderwidth=3, relief="groove")
            self.l5_data1.place(x=625, y=680, height=35, width=565)

            def l5_data1_bool1_fun(value):
                if self.l5_data1_bool1_data.get() == "YES":
                    self.l5_data1_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='green', borderwidth=3,
                                                relief="groove")
                    self.l5_data1_bool1.place(x=1191, y=680, height=35, width=90)
                    self.l5_data1_comment.delete(0, END)
                    self.l5_data1_comment.configure(state=DISABLED)
                else:
                    self.l5_data1_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='red', borderwidth=3,
                                                relief="groove")
                    self.l5_data1_bool1.place(x=1191, y=680, height=35, width=90)
                    self.l5_data1_comment.configure(state=ACTIVE)

            self.l5_data1_bool1_data = Combobox(window, text="""""", state='readonly',
                                                font=("Ariel", 25), values=["YES", "NO"], justify='center')
            self.l5_data1_bool1_data.place(x=1191, y=680, height=35, width=107)

            self.l5_data1_bool1_data.bind("<<ComboboxSelected>>", l5_data1_bool1_fun)

            self.l5_data1_comment = ttk.Entry(window, text="l5_data1", font=("Ariel", 15), width=31)
            self.l5_data1_comment.place(x=1300, y=680, height=35, width=565)










            self.l5_data2 = Label(window, text="Safety",
                                  font=("Ariel", 15), fg='#34943a', bg='white', borderwidth=3, relief="groove")
            self.l5_data2.place(x=625, y=715, height=35, width=565)

            def l5_data2_bool1_fun(value):
                if self.l5_data2_bool1_data.get() == "YES":
                    self.l5_data2_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='green', borderwidth=3,
                                                relief="groove")
                    self.l5_data2_bool1.place(x=1191, y=715, height=35, width=90)
                    self.l5_data2_comment.delete(0, END)
                    self.l5_data2_comment.configure(state=DISABLED)
                else:
                    self.l5_data2_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='red', borderwidth=3,
                                                relief="groove")
                    self.l5_data2_bool1.place(x=1191, y=715, height=35, width=90)
                    self.l5_data2_comment.configure(state=ACTIVE)

            self.l5_data2_bool1_data = Combobox(window, text="""""", state='readonly',
                                                font=("Ariel", 25), values=["YES", "NO"], justify='center')
            self.l5_data2_bool1_data.place(x=1191, y=715, height=35, width=107)

            self.l5_data2_bool1_data.bind("<<ComboboxSelected>>", l5_data2_bool1_fun)

            self.l5_data2_comment = ttk.Entry(window, text="l5_data2", font=("Ariel", 15), width=31)
            self.l5_data2_comment.place(x=1300, y=715, height=35, width=565)




            self.l5_data3 = Label(window, text="Devices to transport materail",
                                  font=("Ariel", 15), fg='#34943a', bg='white', borderwidth=3, relief="groove")
            self.l5_data3.place(x=625, y=750, height=35, width=565)

            def l5_data3_bool1_fun(value):
                if self.l5_data3_bool1_data.get() == "YES":
                    self.l5_data3_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='green', borderwidth=3,
                                                relief="groove")
                    self.l5_data3_bool1.place(x=1191, y=750, height=35, width=90)
                    self.l5_data3_comment.delete(0, END)
                    self.l5_data3_comment.configure(state=DISABLED)
                else:
                    self.l5_data3_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='red', borderwidth=3,
                                                relief="groove")
                    self.l5_data3_bool1.place(x=1191, y=750, height=35, width=90)
                    self.l5_data3_comment.configure(state=ACTIVE)

            self.l5_data3_bool1_data = Combobox(window, text="""""", state='readonly',
                                                font=("Ariel", 25), values=["YES", "NO"], justify='center')
            self.l5_data3_bool1_data.place(x=1191, y=750, height=35, width=107)

            self.l5_data3_bool1_data.bind("<<ComboboxSelected>>", l5_data3_bool1_fun)

            self.l5_data3_comment = ttk.Entry(window, text="l5_data3", font=("Ariel", 15), width=31)
            self.l5_data3_comment.place(x=1300, y=750, height=35, width=565)










            self.l5_data4 = Label(window, text="TQC",
                                  font=("Ariel", 15), fg='#34943a', bg='white', borderwidth=3, relief="groove")
            self.l5_data4.place(x=625, y=785, height=35, width=565)

            def l5_data4_bool1_fun(value):
                if self.l5_data4_bool1_data.get() == "YES":
                    self.l5_data4_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='green', borderwidth=3,
                                                relief="groove")
                    self.l5_data4_bool1.place(x=1191, y=785, height=35, width=90)
                    self.l5_data4_comment.delete(0, END)
                    self.l5_data4_comment.configure(state=DISABLED)
                else:
                    self.l5_data4_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='red', borderwidth=3,
                                                relief="groove")
                    self.l5_data4_bool1.place(x=1191, y=785, height=35, width=90)
                    self.l5_data4_comment.configure(state=ACTIVE)

            self.l5_data4_bool1_data = Combobox(window, text="""""", state='readonly',
                                                font=("Ariel", 25), values=["YES", "NO"], justify='center')
            self.l5_data4_bool1_data.place(x=1191, y=785, height=35, width=107)

            self.l5_data4_bool1_data.bind("<<ComboboxSelected>>", l5_data4_bool1_fun)

            self.l5_data4_comment = ttk.Entry(window, text="l5_data4", font=("Ariel", 15), width=31)
            self.l5_data4_comment.place(x=1300, y=785, height=35, width=565)







            self.l5_data5 = Label(window, text="OPM (Operator preventive maintence)",
                                  font=("Ariel", 15), fg='#34943a', bg='white', borderwidth=3, relief="groove")
            self.l5_data5.place(x=625, y=820, height=35, width=565)

            def l5_data5_bool1_fun(value):
                if self.l5_data5_bool1_data.get() == "YES":
                    self.l5_data5_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='green', borderwidth=3,
                                                relief="groove")
                    self.l5_data5_bool1.place(x=1191, y=820, height=35, width=90)
                    self.l5_data5_comment.delete(0, END)
                    self.l5_data5_comment.configure(state=DISABLED)
                else:
                    self.l5_data5_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='red', borderwidth=3,
                                                relief="groove")
                    self.l5_data5_bool1.place(x=1191, y=820, height=35, width=90)
                    self.l5_data5_comment.configure(state=ACTIVE)

            self.l5_data5_bool1_data = Combobox(window, text="""""", state='readonly',
                                                font=("Ariel", 25), values=["YES", "NO"], justify='center')
            self.l5_data5_bool1_data.place(x=1191, y=820, height=35, width=107)

            self.l5_data5_bool1_data.bind("<<ComboboxSelected>>", l5_data5_bool1_fun)

            self.l5_data5_comment = ttk.Entry(window, text="l5_data5", font=("Ariel", 15), width=31)
            self.l5_data5_comment.place(x=1300, y=820, height=35, width=565)






            self.l5_data6 = Label(window, text="Quality alerts",
                                  font=("Ariel", 15), fg='#34943a', bg='white', borderwidth=3, relief="groove")
            self.l5_data6.place(x=625, y=855, height=35, width=565)

            def l5_data6_bool1_fun(value):
                if self.l5_data6_bool1_data.get() == "YES":
                    self.l5_data6_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='green', borderwidth=3,
                                                relief="groove")
                    self.l5_data6_bool1.place(x=1191, y=855, height=35, width=90)
                    self.l5_data6_comment.delete(0, END)
                    self.l5_data6_comment.configure(state=DISABLED)
                else:
                    self.l5_data6_bool1 = Label(window, text="""""",
                                                font=("Ariel", 15), fg='#34943a', bg='red', borderwidth=3,
                                                relief="groove")
                    self.l5_data6_bool1.place(x=1191, y=855, height=35, width=90)
                    self.l5_data6_comment.configure(state=ACTIVE)

            self.l5_data6_bool1_data = Combobox(window, text="""""", state='readonly',
                                                font=("Ariel", 25), values=["YES", "NO"], justify='center')
            self.l5_data6_bool1_data.place(x=1191, y=855, height=35, width=107)

            self.l5_data6_bool1_data.bind("<<ComboboxSelected>>", l5_data6_bool1_fun)

            self.l5_data6_comment = ttk.Entry(window, text="l5_data6", font=("Ariel", 15), width=31)
            self.l5_data6_comment.place(x=1300, y=855, height=35, width=565)

            """
            self.btn0 = ttk.Button(user_add, text="DASHBOARD", width=20)
            self.btn0.place(x=0, y=70, width=230, height=70)
            self.btn1 = ttk.Button(user_add, text="MASTER", width=20)
            self.btn1.place(x=230, y=70, width=230, height=70)
            self.btn3 = ttk.Button(user_add, text="R&R", width=20)
            self.btn3.place(x=460, y=70, width=230, height=70)
            self.btn4 = ttk.Button(user_add, text="CAPABILITY", width=20)
            self.btn4.place(x=690, y=70, width=230, height=70)
            self.btn5 = ttk.Button(user_add, text="GROUP_KC", width=20)
            self.btn5.place(x=920, y=70, width=230, height=70)
            """

            def adding_data_to_csv():
                Dept=self.dept_name.get()
                Opertor=self.operator_name.get()
                Station=self.station_no.get()
                Engine=self.engine_model.get()
                Date=self.date.get()
                QE=self.QE_name.get()

                if Dept!="" and Opertor!="" and Station!="" and Engine!="" and Date!="" and QE!="":
                    print("HELLO")

                    dir_path = os.getcwd()
                    #dir_path = dir_path.replace("\\", "/")
                    path = dir_path + '\DATA _FORMAT\Zero_Error.csv'


                    DATA_EDIT=[['Dept. No.', 'Operator Name', 'Station No.', 'Engine Model', 'Date', 'QE Name']]


                    iter=0
                    with open(path, 'r') as file:
                        csv_reader = csv.reader(file)

                        for each in csv_reader:
                            if iter>0:
                                DATA_EDIT.append(each)
                            iter+=1




                    DATA_EDIT[1][0]=Dept
                    DATA_EDIT[1][1] = Opertor
                    DATA_EDIT[1][2] = Station
                    DATA_EDIT[1][3] = Engine
                    DATA_EDIT[1][4] = Date
                    DATA_EDIT[1][5] = QE




                    DATA_EDIT[4][4]=str(self.l1_data1_bool1_data.get())
                    DATA_EDIT[4][5]=str(self.l1_data1_comment.get())


                    DATA_EDIT[5][4] = str(self.l2_data1_bool1_data.get())
                    DATA_EDIT[5][5] = str(self.l2_data1_comment.get())

                    DATA_EDIT[6][0]=DATA_EDIT[5][0]
                    DATA_EDIT[6][4] = str(self.l2_data2_bool1_data.get())
                    DATA_EDIT[6][5] = str(self.l2_data2_comment.get())



                    DATA_EDIT[7][4] = str(self.l3_data1_bool1_data.get())
                    DATA_EDIT[7][5] = str(self.l3_data1_comment.get())

                    DATA_EDIT[8][0] = DATA_EDIT[7][0]
                    DATA_EDIT[8][4] = str(self.l3_data2_bool1_data.get())
                    DATA_EDIT[8][5] = str(self.l3_data2_comment.get())

                    DATA_EDIT[9][0] = DATA_EDIT[7][0]
                    DATA_EDIT[9][4] = str(self.l3_data3_bool1_data.get())
                    DATA_EDIT[9][5] = str(self.l3_data3_comment.get())

                    DATA_EDIT[10][4] = str(self.l4_data1_bool1_data.get())
                    DATA_EDIT[10][5] = str(self.l4_data1_comment.get())


                    DATA_EDIT[11][4] = str(self.l5_data1_bool1_data.get())
                    DATA_EDIT[11][5] = str(self.l5_data1_comment.get())

                    DATA_EDIT[12][0] = DATA_EDIT[11][0]
                    DATA_EDIT[12][4] = str(self.l5_data2_bool1_data.get())
                    DATA_EDIT[12][5] = str(self.l5_data2_comment.get())

                    DATA_EDIT[13][0] = DATA_EDIT[11][0]
                    DATA_EDIT[13][4] = str(self.l5_data3_bool1_data.get())
                    DATA_EDIT[13][5] = str(self.l5_data3_comment.get())

                    DATA_EDIT[14][0] = DATA_EDIT[11][0]
                    DATA_EDIT[14][4] = str(self.l5_data4_bool1_data.get())
                    DATA_EDIT[14][5] = str(self.l5_data4_comment.get())

                    DATA_EDIT[15][0] = DATA_EDIT[11][0]
                    DATA_EDIT[15][4] = str(self.l5_data5_bool1_data.get())
                    DATA_EDIT[15][5] = str(self.l5_data5_comment.get())

                    DATA_EDIT[16][0] = DATA_EDIT[11][0]
                    DATA_EDIT[16][4] = str(self.l5_data6_bool1_data.get())
                    DATA_EDIT[16][5] = str(self.l5_data6_comment.get())



                    path = dir_path + '\DATA _FORMAT\STORED_DATA\DATA'+str(Opertor)+'.csv'




                    with open(path, 'w') as file:
                        wr = csv.writer(file)
                        for each in DATA_EDIT:
                            wr.writerow(each)


                    if self.l1_data1_bool1_data.get()!="" \
                            and self.l2_data1_bool1_data.get()!="" and self.l2_data2_bool1_data.get()!="" \
                            and self.l3_data1_bool1_data.get() != "" and self.l3_data2_bool1_data.get()!="" and self.l3_data3_bool1_data.get()!="" \
                            and self.l4_data1_bool1_data.get() != "" \
                            and self.l5_data1_bool1_data.get()!="" and self.l5_data2_bool1_data.get()!="" and self.l5_data3_bool1_data.get()!="" \
                            and self.l5_data4_bool1_data.get() != "" and self.l5_data5_bool1_data.get()!="" and self.l5_data6_bool1_data.get()!="":


                        print(self.l1_data1_bool1_data.get()!="",
                            self.l2_data1_bool1_data.get()!="",self.l2_data2_bool1_data.get()!="",
                            self.l3_data1_bool1_data.get() != "",self.l3_data2_bool1_data.get()!="",self.l3_data3_bool1_data.get()!="",
                            self.l4_data1_bool1_data.get() != "",
                            self.l5_data1_bool1_data.get()!="",self.l5_data2_bool1_data.get()!="",self.l5_data3_bool1_data.get()!="",
                              self.l5_data4_bool1_data.get() != "", self.l5_data5_bool1_data.get() != "",
                              self.l5_data6_bool1_data.get() != "")











                else:
                    messagebox.showwarning("Error", "Enter Values")




            self.btn = ttk.Button(window, text="Import.CSV File", width=20,command=adding_data_to_csv)
            self.btn.place(x=625, y=915, width=565, height=70)







        def quit(self):
            user_add.destroy()

    user_add = tk.Tk()
    user_login_window = user_add_kc(user_add)
    user_add.config(background='white')
    user_add.attributes('-alpha', 1)
    #user_add.iconbitmap(default='IMAGES/favicon.ico')
    user_add.title('Zero Error Short Audit')
    user_add.geometry("1920x1080")
    user_add.mainloop()


if __name__ == "__main__":
    user_add_kc()