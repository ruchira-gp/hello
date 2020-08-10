from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from tkcalendar import DateEntry
from tkinter import *

import sqlite3
conn=sqlite3.connect('mydata.db')
c=conn.cursor()
c.execute('''CREATE TABLE complainant modify column cname varchar(20) not null, modify column cage int not null, modify column  cgender varchar(10) not null, modify column cid varchar(10) unique not null, modify column area varchar(20) not null, modify column city varchar(20) not null, modify column firno varchar(10) not null,   FOREIGN KEY (firno) REFERENCES complaint(firno)''')
#c.execute('''CREATE TABLE complainant modify cname varchar(20) not null,cage int not null, cgender varchar(10) not null,cid varchar(10) unique not null,area varchar(20) not null,city varchar(20) not null,firno varchar(10) not null, FOREIGN KEY (firno) REFERENCES complaint(firno)''')
#c.execute('''CREATE TABLE convict modify coname varchar(20) not null ,coheight int not null ,cogen varchar(20) not null ,coph int(12) not null ,coid varchar(20) unique not null ,coiden varchar(25) not null ,firno varchar(10) not null , FOREIGN KEY (firno) REFERENCES complaint(firno)''')
#c.execute('''CREATE TABLE officer modify offname varchar(20) not null ,offtype varchar(20) not null ,offid varchar(20) unique not null ,firno varchar(10) not null , FOREIGN KEY (firno) REFERENCES complaint(firno)''')
#c.execute('''CREATE TABLE court modify courtda varchar(20) not null ,courtpp varchar(20) not null ,courtno varchar(20) not null ,courtjud varchar(20) not null ,courttype varchar(20) not null ,firno varchar(10)  not null ,FOREIGN KEY (firno) REFERENCES complaint(firno)''')
root=Tk()
root.configure(background='#A9A9A9')
root.title("CRIMINAL DATABASE")
root.iconbitmap('C:\\Users\\ruchi\\PycharmProjects\\namaskara\\img3.ico')
filename = PhotoImage(file = "C:\\Users\\ruchi\\PycharmProjects\\namaskara\\img2.png")
background_label = Label(root,image=filename)
label_0 = Label(root, text="W E L C O M E", font=("bold", 20),bg='#FF4500')
background_label.pack()
def query():


    '''q_root=Tk()
    q_root.iconbitmap('C:\\Users\\ruchi\\PycharmProjects\\namaskara\\img3.ico')
    q_root.geometry('700x700')
    submit_but1 = Button(q_root, text=" QUERY 1", padx=45, relief=RAISED, command=q1submit)
    submit_but1.grid(row=1, column=0)
    submit_but1.configure(bg='green')
    submit_but2 = Button(q_root, text=" QUERY 2", padx=45, relief=RAISED, command=q2submit)
    submit_but2.grid(row=2, column=0)
    submit_but2.configure(bg='green')
    submit_but3 = Button(q_root, text=" QUERY 3", padx=45, relief=RAISED, command=q3submit)
    submit_but3.grid(row=3, column=0)
    submit_but3.configure(bg='green')
    submit_but4 = Button(q_root, text=" QUERY 4", padx=45, relief=RAISED, command=q4submit)
    submit_but4.grid(row=4, column=0)
    submit_but4.configure(bg='green')
    submit_but5 = Button(q_root, text=" QUERY 5", padx=45, relief=RAISED, command=q5submit)
    submit_but5.grid(row=5, column=0)
    submit_but5.configure(bg='green')
    submit_but6 = Button(q_root, text=" QUERY 6", padx=45, relief=RAISED, command=q6submit)
    submit_but6.grid(row=6, column=0)
    submit_but6.configure(bg='green')
    submit_but7 = Button(q_root, text=" QUERY 7", padx=45, relief=RAISED, command=q7submit)
    submit_but7.grid(row=7, column=0)
    submit_but7.configure(bg='green')
    submit_but8 = Button(q_root, text=" QUERY 8", padx=45, relief=RAISED, command=q8submit)
    submit_but8.grid(row=8, column=0)
    submit_but8.configure(bg='green')
    submit_but9 = Button(q_root, text=" QUERY 9", padx=45, relief=RAISED, command=q9submit)
    submit_but9.grid(row=9, column=0)
    submit_but9.configure(bg='green')
    submit_but10 = Button(q_root, text="QUERY 10", padx=45, relief=RAISED, command=q10submit)
    submit_but10.grid(row=10, column=0)
    submit_but10.configure(bg='green')
    submit_but11 = Button(q_root, text="QUERY 11", padx=45, relief=RAISED, command=q11submit)
    submit_but11.grid(row=11, column=0)
    submit_but11.configure(bg='green')
    submit_but12 = Button(q_root, text="QUERY 12", padx=45, relief=RAISED, command=q12submit)
    submit_but12.grid(row=12, column=0)
    submit_but12.configure(bg='green')
    submit_but13 = Button(q_root, text="QUERY 13", padx=45, relief=RAISED, command=q13submit)
    submit_but13.grid(row=13, column=0)
    submit_but13.configure(bg='green')
    submit_but14 = Button(q_root, text="QUERY 14", padx=45, relief=RAISED, command=q14submit)
    submit_but14.grid(row=14, column=0)
    submit_but14.configure(bg='green')
    submit_but15 = Button(q_root, text="QUERY 15", padx=45, relief=RAISED, command=q15submit)
    submit_but15.grid(row=15, column=0)
    submit_but15.configure(bg='green')
    submit_but16 = Button(q_root, text="QUERY 16", padx=45, relief=RAISED, command=q16submit)
    submit_but16.grid(row=16, column=0)
    submit_but16.configure(bg='green')
    submit_but17 = Button(q_root, text="QUERY 17", padx=45, relief=RAISED, command=q17submit)
    submit_but17.grid(row=17, column=0)
    submit_but17.configure(bg='green')
    submit_but18= Button(q_root, text="QUERY 18", padx=45, relief=RAISED, command=q18submit)
    submit_but18.grid(row=18, column=0)
    submit_but18.configure(bg='green')
    submit_but19 = Button(q_root, text="QUERY 19", padx=45, relief=RAISED, command=q19submit)
    submit_but19.grid(row=19, column=0)
    submit_but19.configure(bg='green')
    submit_but20 = Button(q_root, text="QUERY 20", padx=45, relief=RAISED, command=q20submit)
    submit_but20.grid(row=20, column=0)
    submit_but20.configure(bg='green')'''

    conn = sqlite3.connect('mydata.db')
    c = conn.cursor()
    root = Tk()
    root.configure(background='#A9A9A9')
    root.title("CRIMINAL DATABASE")

    root.geometry("807x779+650+150")
    root.title("Queries page")
    root.configure(background="#c0cece")

    root.geometry("807x779+650+150")
    root.title("New rootlevel")
    root.configure(background="#c0cece")

    heading_frame = tk.Frame(root)
    heading_frame.place(relx=0.025, rely=0.013, relheight=0.109, relwidth=0.96)

    heading_frame.configure(relief='groove')
    heading_frame.configure(borderwidth="2")
    heading_frame.configure(relief="groove")
    heading_frame.configure(background="#4651af")

    heading_label = tk.Label(heading_frame)
    heading_label.place(relx=0.103, rely=0.235, height=56, width=622)
    heading_label.configure(activebackground="#c0cece")
    heading_label.configure(background="#4651af")
    heading_label.configure(borderwidth="3")
    heading_label.configure(disabledforeground="#a3a3a3")
    heading_label.configure(font="TkHeadingFont")
    heading_label.configure(foreground="#000000")
    heading_label.configure(highlightcolor="#7aafad")
    heading_label.configure(text='''QUERIES''')

    # menubar = tk.Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
    # root.configure(menu = menubar)

    main_frame = tk.Frame(root)
    main_frame.place(relx=0.012, rely=0.205, relheight=0.687
                     , relwidth=0.973)
    main_frame.configure(relief='groove')
    main_frame.configure(borderwidth="2")
    main_frame.configure(relief="groove")
    main_frame.configure(background="#becbd8")

    def retq1():
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
            '''Select * from convict where firno = "18-19/288"''')
        rows = c.fetchall()
        global temp_list
        temp_list = []
        for i in rows:
            x = 0
            while (x < 7):
                temp_list.append(i[x])
                x = x + 1
        # print(temp_list)
        messagebox.showinfo("Convicted daetails with FIR np. 18-19/288 ", temp_list)
        del temp_list
        conn.close()
        return

    query_button1 = tk.Button(main_frame)
    query_button1.place(relx=0.013, rely=0.019, height=43, width=366)
    query_button1.configure(activebackground="#ececec")
    query_button1.configure(activeforeground="#000000")
    query_button1.configure(background="#6693d8")
    query_button1.configure(disabledforeground="#a3a3a3")
    query_button1.configure(foreground="#000000")
    query_button1.configure(highlightbackground="#d9d9d9")
    query_button1.configure(highlightcolor="black")
    query_button1.configure(pady="0")
    query_button1.configure(text='''CONVICTED DETAILS ARE''')
    query_button1.configure(command=retq1)

    def retq2():
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
            '''Select cname from complainant where area = "Vijayanagar"''')
        rows = c.fetchall()
        global temp_list
        temp_list = []
        for i in rows:
            x = 0
            while (x < 1):
                temp_list.append(i[x])
                x = x + 1
        # print(temp_list)
        messagebox.showinfo("Complainants from Vijayanagar ", temp_list)
        del temp_list
        conn.close()
        return

    query_button2 = tk.Button(main_frame)
    query_button2.place(relx=0.013, rely=0.112, height=43, width=366)
    query_button2.configure(activebackground="#ececec")
    query_button2.configure(activeforeground="#000000")
    query_button2.configure(background="#6693d8")
    query_button2.configure(disabledforeground="#a3a3a3")
    query_button2.configure(foreground="#000000")
    query_button2.configure(highlightbackground="#d9d9d9")
    query_button2.configure(highlightcolor="black")
    query_button2.configure(pady="0")
    query_button2.configure(text='''RETRIEVE COMPLAINANT NAMES FROM A PARTICULAR AREA''')
    query_button2.configure(command=retq2)

    def retq3():
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
            '''Select coname from convict where cogen = "Female"''')
        rows = c.fetchall()
        global temp_list
        temp_list = []
        for i in rows:
            x = 0
            while (x < 7):
                temp_list.append(i[x])
                x = x + 1
        # print(temp_list)
        messagebox.showinfo("All female convicts ", temp_list)
        del temp_list
        conn.close()
        return

    query_button3 = tk.Button(main_frame)
    query_button3.place(relx=0.013, rely=0.206, height=43, width=366)
    query_button3.configure(activebackground="#ececec")
    query_button3.configure(activeforeground="#000000")
    query_button3.configure(background="#6693d8")
    query_button3.configure(disabledforeground="#a3a3a3")
    query_button3.configure(foreground="#000000")
    query_button3.configure(highlightbackground="#d9d9d9")
    query_button3.configure(highlightcolor="black")
    query_button3.configure(pady="0")
    query_button3.configure(text='''RETRIEVE ALL FEMALE CONVICTS REGISTERED''')
    query_button3.configure(command=retq3)

    def retq4():
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
            '''Select * from officer where firno = "18-19/788"''')
        rows = c.fetchall()
        global temp_list
        temp_list = []
        for i in rows:
            x = 0
            while (x < 7):
                temp_list.append(i[x])
                x = x + 1
        # print(temp_list)
        messagebox.showinfo("Officer details handling case FIR no 18-19/788 ", temp_list)
        del temp_list
        conn.close()
        return

    query_button4 = tk.Button(main_frame)
    query_button4.place(relx=0.013, rely=0.299, height=43, width=366)
    query_button4.configure(activebackground="#ececec")
    query_button4.configure(activeforeground="#000000")
    query_button4.configure(background="#6693d8")
    query_button4.configure(disabledforeground="#a3a3a3")
    query_button4.configure(foreground="#000000")
    query_button4.configure(highlightbackground="#d9d9d9")
    query_button4.configure(highlightcolor="black")
    query_button4.configure(pady="0")
    query_button4.configure(text='''RETRIEVE OFFICER DETAILS HANDLING A PARTICULAR CASE''')
    query_button4.configure(command=retq4)

    def retq5():
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
            '''Select courtjud from court where firno = "18-19/288"''')
        rows = c.fetchall()
        global temp_list
        temp_list = []
        for i in rows:
            x = 0
            while (x < 1):
                temp_list.append(i[x])
                x = x + 1
        # print(temp_list)
        messagebox.showinfo("Judege for case with FIR no 18-19/288 ", temp_list)
        del temp_list
        conn.close()
        return

    query_button5 = tk.Button(main_frame)
    query_button5.place(relx=0.013, rely=0.393, height=43, width=366)
    query_button5.configure(activebackground="#ececec")
    query_button5.configure(activeforeground="#000000")
    query_button5.configure(background="#6693d8")
    query_button5.configure(disabledforeground="#a3a3a3")
    query_button5.configure(foreground="#000000")
    query_button5.configure(highlightbackground="#d9d9d9")
    query_button5.configure(highlightcolor="black")
    query_button5.configure(pady="0")
    query_button5.configure(text='''RETRIEVE JUDGE NAME FOR GIVEN FIR No.''')
    query_button5.configure(command=retq5)

    def retq6():
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
            '''Select prooftype from complaint where proofid = "254365"''')
        rows = c.fetchall()
        global temp_list
        temp_list = []
        for i in rows:
            x = 0
            while (x < 1):
                temp_list.append(i[x])
                x = x + 1
        # print(temp_list)
        messagebox.showinfo("Proof type with proof ID 254365 ", temp_list)
        del temp_list
        conn.close()
        return

    query_button6 = tk.Button(main_frame)
    query_button6.place(relx=0.013, rely=0.486, height=43, width=366)
    query_button6.configure(activebackground="#ececec")
    query_button6.configure(activeforeground="#000000")
    query_button6.configure(background="#6693d8")
    query_button6.configure(disabledforeground="#a3a3a3")
    query_button6.configure(foreground="#000000")
    query_button6.configure(highlightbackground="#d9d9d9")
    query_button6.configure(highlightcolor="black")
    query_button6.configure(pady="0")
    query_button6.configure(text='''RETRIEVE PROOF TYPE FOR GIVEN PROOF ID''')
    query_button6.configure(command=retq6)

    def retq7():
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
            '''Select courtpp from court where courtda = "Aisiri"''')
        rows = c.fetchall()
        global temp_list
        temp_list = []
        for i in rows:
            x = 0
            while (x < 1):
                temp_list.append(i[x])
                x = x + 1
        # print(temp_list)
        messagebox.showinfo("PP where DA = Aisiri is ", temp_list)
        del temp_list
        conn.close()
        return

    query_button7 = tk.Button(main_frame)
    query_button7.place(relx=0.013, rely=0.766, height=43, width=366)
    query_button7.configure(activebackground="#ececec")
    query_button7.configure(activeforeground="#000000")
    query_button7.configure(background="#6693d8")
    query_button7.configure(disabledforeground="#a3a3a3")
    query_button7.configure(foreground="#000000")
    query_button7.configure(highlightbackground="#d9d9d9")
    query_button7.configure(highlightcolor="black")
    query_button7.configure(pady="0")
    query_button7.configure(text='''RETRIEVE PP WHERE DA IS GIVEN''')
    query_button7.configure(command=retq7)

    def retq8():
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
            '''Select coname from convict where coheight > 160''')
        rows = c.fetchall()
        global temp_list
        temp_list = []
        for i in rows:
            x = 0
            while (x < 7):
                temp_list.append(i[x])
                x = x + 1
        # print(temp_list)
        messagebox.showinfo("Convicts taller than 160cm ", temp_list)
        del temp_list
        conn.close()
        return

    query_button8 = tk.Button(main_frame)
    query_button8.place(relx=0.013, rely=0.579, height=43, width=366)
    query_button8.configure(activebackground="#ececec")
    query_button8.configure(activeforeground="#000000")
    query_button8.configure(background="#6693d8")
    query_button8.configure(disabledforeground="#a3a3a3")
    query_button8.configure(foreground="#000000")
    query_button8.configure(highlightbackground="#d9d9d9")
    query_button8.configure(highlightcolor="black")
    query_button8.configure(pady="0")
    query_button8.configure(text='''RETRIEVE CONVICTS TALLER THAN GIVEN HEIGHT''')
    query_button8.configure(command=retq8)

    def retq9():
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
            '''Select witname from complaint where firno = "18-19/788" ''')
        rows = c.fetchall()
        global temp_list
        temp_list = []
        '''for i in rows:
            x = 0
            while (x < 1):
                temp_list.append(i[x])
                x = x + 1'''
        # print(temp_list)
        messagebox.showinfo("Witness for FIR No. 18-19/788 is ", temp_list)
        del temp_list
        conn.close()()
        return

    query_button9 = tk.Button(main_frame)
    query_button9.place(relx=0.013, rely=0.673, height=43, width=366)
    query_button9.configure(activebackground="#ececec")
    query_button9.configure(activeforeground="#000000")
    query_button9.configure(background="#6693d8")
    query_button9.configure(disabledforeground="#a3a3a3")
    query_button9.configure(foreground="#000000")
    query_button9.configure(highlightbackground="#d9d9d9")
    query_button9.configure(highlightcolor="black")
    query_button9.configure(pady="0")
    query_button9.configure(text='''RETRIEVE WITNESS FOR GIVEN FIR No.''')
    query_button9.configure(command=retq9)

    def retq10():
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
            '''Select offname from officer where offid = "245375"''')
        rows = c.fetchall()
        global temp_list
        temp_list = []
        for i in rows:
            x = 0
            while (x < 1):
                temp_list.append(i[x])
                x = x + 1
        # print(temp_list)
        messagebox.showinfo("Officer with ID = 245375 ", temp_list)
        del temp_list
        conn.close()
        return

    query_button10 = tk.Button(main_frame)
    query_button10.place(relx=0.013, rely=0.86, height=43, width=366)
    query_button10.configure(activebackground="#ececec")
    query_button10.configure(activeforeground="#000000")
    query_button10.configure(background="#6693d8")
    query_button10.configure(disabledforeground="#a3a3a3")
    query_button10.configure(foreground="#000000")
    query_button10.configure(highlightbackground="#d9d9d9")
    query_button10.configure(highlightcolor="black")
    query_button10.configure(pady="0")
    query_button10.configure(text='''RETRIEVE OFFICER WITH GIVEN ID ''')
    query_button10.configure(command=retq10)

    def retq11():
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
            '''Select courttype from court where courtno = "KA341"''')
        rows = c.fetchall()
        global temp_list
        temp_list = []
        for i in rows:
            x = 0
            while (x < 1):
                temp_list.append(i[x])
                x = x + 1
        # print(temp_list)
        messagebox.showinfo("Court type with courtnumber=KA341 ", temp_list)
        del temp_list
        conn.close()
        return

    query_button11 = tk.Button(main_frame)
    query_button11.place(relx=0.548, rely=0.019, height=43, width=336)
    query_button11.configure(activebackground="#ececec")
    query_button11.configure(activeforeground="#000000")
    query_button11.configure(background="#6693d8")
    query_button11.configure(disabledforeground="#a3a3a3")
    query_button11.configure(foreground="#000000")
    query_button11.configure(highlightbackground="#d9d9d9")
    query_button11.configure(highlightcolor="black")
    query_button11.configure(pady="0")
    query_button11.configure(text='''GET THE COURT DETAILS FOR GIVEN COURT ID''')
    query_button11.configure(command=retq11)

    def retq12():
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
            '''Select C.coname, P.area from convict as C, complainant as P where P.city = "Mysuru" ''')
        rows = c.fetchall()
        global temp_list
        temp_list = []
        for i in rows:
            x = 0
         #   while (x < 1):
            temp_list.append(i)
         #       x = x + 1
        # print(temp_list)
        messagebox.showinfo("Convictname and area in Mysuru", temp_list)
        del temp_list
        conn.close()
        return

    query_button12 = tk.Button(main_frame)
    query_button12.place(relx=0.548, rely=0.112, height=43, width=336)
    query_button12.configure(activebackground="#ececec")
    query_button12.configure(activeforeground="#000000")
    query_button12.configure(background="#6693d8")
    query_button12.configure(disabledforeground="#a3a3a3")
    query_button12.configure(foreground="#000000")
    query_button12.configure(highlightbackground="#d9d9d9")
    query_button12.configure(highlightcolor="black")
    query_button12.configure(pady="0")
    query_button12.configure(text='''CONVICTS NAME AND AREA IN MYSURU''')
    query_button12.configure(command=retq12)

    def retq13():
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
            '''Select coname from convict where coheight= "165"''')
        rows = c.fetchall()
        global temp_list
        temp_list = []
        for i in rows:
            x = 0
            while (x < 1):
                temp_list.append(i[x])
                x = x + 1
        # print(temp_list)
        messagebox.showinfo("Convictname with height 165cms ", temp_list)
        del temp_list
        conn.close()
        return

    query_button13 = tk.Button(main_frame)
    query_button13.place(relx=0.548, rely=0.206, height=43, width=336)
    query_button13.configure(activebackground="#ececec")
    query_button13.configure(activeforeground="#000000")
    query_button13.configure(background="#6693d8")
    query_button13.configure(disabledforeground="#a3a3a3")
    query_button13.configure(foreground="#000000")
    query_button13.configure(highlightbackground="#d9d9d9")
    query_button13.configure(highlightcolor="black")
    query_button13.configure(pady="0")
    query_button13.configure(text='''CONVICTS NAME AND AREA WHO ARE OF 165CMS HEIGHT''')
    query_button13.configure(command=retq13)

    def retq14():
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
            '''Select sum(comval),area from complaint C,complainant R where in R.city = "Bengaluru"''')
        rows = c.fetchall()
        global temp_list
        temp_list = []
        for i in rows:
            x = 0
            while (x < 1):
                temp_list.append(i[x])
                x = x + 1
        # print(temp_list)
        messagebox.showinfo("Total value lost during crime in Benagluru", temp_list)
        del temp_list
        conn.close()
        return

    query_button14 = tk.Button(main_frame)
    query_button14.place(relx=0.548, rely=0.299, height=43, width=336)
    query_button14.configure(activebackground="#ececec")
    query_button14.configure(activeforeground="#000000")
    query_button14.configure(background="#6693d8")
    query_button14.configure(disabledforeground="#a3a3a3")
    query_button14.configure(foreground="#000000")
    query_button14.configure(highlightbackground="#d9d9d9")
    query_button14.configure(highlightcolor="black")
    query_button14.configure(pady="0")
    query_button14.configure(text='''TOTAL VALUE LOST DURING CRIME IN BENGALURU''')
    query_button14.configure(command=retq14)

    def retq15():
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
            '''Select COUNT(*) from complainant where city= "Kurnool and complaint.date=2017%"''')
        rows = c.fetchall()
        global temp_list
        temp_list = []
        for i in rows:
            x = 0
            while (x < 1):
                temp_list.append(i[x])
                x = x + 1
        # print(temp_list)
        messagebox.showinfo("Complaint count in Kurnool in 2017", temp_list)
        del temp_list
        conn.close()
        return

    query_button15 = tk.Button(main_frame)
    query_button15.place(relx=0.548, rely=0.393, height=43, width=336)
    query_button15.configure(activebackground="#ececec")
    query_button15.configure(activeforeground="#000000")
    query_button15.configure(background="#6693d8")
    query_button15.configure(disabledforeground="#a3a3a3")
    query_button15.configure(foreground="#000000")
    query_button15.configure(highlightbackground="#d9d9d9")
    query_button15.configure(highlightcolor="black")
    query_button15.configure(pady="0")
    query_button15.configure(text='''TOTAL NUMBER OF CRIMES REGISTERED IN KURNOOL IN 2017''')
    query_button15.configure(command=retq15)

    return
def retrieve():
    ret_root = Tk()
    ret_root.geometry('700x700')
    ret_root.title("RETRIEVE QUERIES")
    ret_root.iconbitmap('C:\\Users\\ruchi\\PycharmProjects\\namaskara\\img3.ico')
    Frame1 = tk.Frame(ret_root)
    Frame1.place(relx=0.029, rely=0.06, relheight=0.261, relwidth=0.95)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#d9d9d9")
    # print(i[0],      i[1],         i[2],         i[3],         i[4],         i[5],         i[6],         i[7])
    conn = sqlite3.connect('mydata.db')
    compnum = conn.cursor()
    compnum.execute('''select comnum from complaint ''')
    compnumr = compnum.fetchall()
    global complist
    complist = []
    for i in compnumr:
        complist.append(i)
    # print(complist)
    var = StringVar(Frame1)
    var.set(complist[0])
    mynumber = tk.StringVar()
    complist2=tuple(complist)
    ret_complaint_no = ttk.Combobox(Frame1,textvariable=mynumber)
    ret_complaint_no['values'] = complist2
    ret_complaint_no.place(relx=0.03, rely=0.229, height=40, relwidth=0.382)
    print(ret_complaint_no.get())
    conn.close()()
    conn = sqlite3.connect('mydata.db')
    firnum = conn.cursor()
    firnum.execute('''select firno from complaint ''')
    firnumr = firnum.fetchall()
    global firlist
    firlist = []
    for i in firnumr:
        firlist.append(i)
    # print(complist)
    var1 = StringVar(Frame1)
    var1.set(firlist[0])
    mynumber1 = tk.StringVar()
    firlist2 = tuple(firlist)
    ret_fir_no = ttk.Combobox(Frame1, textvariable=mynumber1)
    ret_fir_no['values'] = firlist2
    ret_fir_no.place(relx=0.556, rely=0.229, height=40, relwidth=0.367)


    ret_date = DateEntry(Frame1, width=12, year=2019, month=7, day=22,
                    background='darkblue', foreground='white', borderwidth=2)
    ret_date.pack(padx=10, pady=10)
    ret_date.place(relx=0.03, rely=0.629, height=40,
                   relwidth=0.382)

    Label11 = tk.Label(Frame1)
    conn.close()()
    conn = sqlite3.connect('mydata.db')
    city = conn.cursor()
    city.execute('''select city from complainant ''')
    cityr = city.fetchall()
    global citylist
    citylist = []
    for i in cityr:
        citylist.append(i)
    # print(complist)
    var2 = StringVar(Frame1)
    var2.set(citylist[0])
    mynumber2 = tk.StringVar()
    citylist2 = tuple(citylist)
    ret_city = ttk.Combobox(Frame1, textvariable=mynumber2)
    ret_city['values'] = citylist2
    #ret_city = tk.Entry(Frame1)
    ret_city.place(relx=0.556, rely=0.629, height=40, relwidth=0.382)
    ret_city.configure(background="white")
    #ret_city.configure(disabledforeground="#a3a3a3")
    #ret_city.configure(font="TkFixedFont")
    #ret_city.configure(foreground="#000000")
    Label11.configure(background="#d9d9d9")
    Label11.configure(disabledforeground="#a3a3a3")
    Label11.configure(foreground="#000000")
    Label11.configure(text='''COMPLAINT NUMBER''')

    Label2 = tk.Label(Frame1)
    Label2.place(relx=0.556, rely=0.057, height=21, width=73)
    Label2.configure(background="#d9d9d9")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(foreground="#000000")
    Label2.configure(text='''FIR NUMBER''')

    Label3 = tk.Label(Frame1)
    Label3.place(relx=0.045, rely=0.514, height=11, width=34)
    Label3.configure(background="#d9d9d9")
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(foreground="#000000")
    Label3.configure(text='''DATE''')

    Label4 = tk.Label(Frame1)
    Label4.place(relx=0.571, rely=0.514, height=11, width=30)
    Label4.configure(background="#d9d9d9")
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(foreground="#000000")
    Label4.configure(text='''CITY''')

    ret_con_name = tk.Entry(ret_root)
    ret_con_name.place(relx=0.057, rely=0.403, height=40, relwidth=0.363)
    ret_con_name.configure(background="white")
    ret_con_name.configure(disabledforeground="#a3a3a3")
    ret_con_name.configure(font="TkFixedFont")
    ret_con_name.configure(foreground="#000000")
    ret_con_name.configure(insertbackground="black")

    Label5 = tk.Label(ret_root)
    Label5.place(relx=0.071, rely=0.358, height=21, width=107)
    Label5.configure(background="#d9d9d9")
    Label5.configure(disabledforeground="#a3a3a3")
    Label5.configure(foreground="#000000")
    Label5.configure(text='''CONVICTED NAME''')

    def Find():
        print(ret_complaint_no.get())
        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()

        c.execute(
                '''select * from convict where firno = '{}'   '''.format(
                    ret_fir_no.get()))
        c1=conn.cursor()
        c1.execute('''select * from complainant where firno ='{}'  '''.format (ret_fir_no.get()))


        try:
            def pop():
                rows = c.fetchall()
                global temp_list
                temp_list=[]
                for i in rows:
                    x=0
                    while (x<=len(temp_list)):
                        temp_list.append(i[x])
                        x=x+1
                print(temp_list)
                messagebox._show("QUERIES FOUND", temp_list)
                del temp_list[:]
            pop()
            conn.close()()

        except IndexError:
            messagebox.showerror("ERROR","No Value entered")


        ret_root.destroy()
    Button1 = tk.Button(ret_root, command=Find)
    Button1.place(relx=0.6, rely=0.403, height=44, width=227)
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#d9d9d9")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(foreground="#000000")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''SUBMIT''')

    Label1 = tk.Label(Frame1)
    Label1.place(relx=0.03, rely=0.057, height=21, width=124)
    Label1.configure(background="#d9d9d9")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#000000")
    Label1.configure(text='COMPLAINT NUMBER')
    return


def enter():
    enter_root = Tk()
    enter_root.iconbitmap('C:\\Users\\ruchi\\PycharmProjects\\namaskara\\img3.ico')
    enter_root.title('Enter Crime Details')
    b=StringVar(enter_root, value='0')
    n=StringVar(enter_root,value='NULL')
    l=StringVar(enter_root,value='NULL')
    v=StringVar(enter_root,value='NULL')
    e=StringVar(enter_root,value='MM/DD/YYYY')
    c_name = Entry(enter_root, width=30)
    c_name.grid(row=0, column=1, padx=20)
    c_age = Entry(enter_root, width=30)
    c_age.grid(row=1, column=1)
    c_gender = Entry(enter_root, width=30)
    c_gender.grid(row=2, column=1)
    c_id = Entry(enter_root, width=30)
    c_id.grid(row=3, column=1)
    area = Entry(enter_root, width=30)
    area.grid(row=4, column=1)
    city = Entry(enter_root, width=30)
    city.grid(row=5, column=1)
    co_name = Entry(enter_root, width=30)
    co_name.grid(row=6, column=1)
    co_height = Entry(enter_root, width=30)
    co_height.grid(row=7, column=1)
    co_gen = Entry(enter_root, width=30)
    co_gen.grid(row=8, column=1)
    co_ph = Entry(enter_root, width=30)
    co_ph.grid(row=9, column=1)
    co_id = Entry(enter_root, width=30)
    co_id.grid(row=10, column=1)
    co_iden = Entry(enter_root, width=30,text=v)
    co_iden.grid(row=11, column=1)
    com_num = Entry(enter_root, width=30)
    com_num.grid(row=12, column=1)
    com_date = Entry(enter_root, width=30,text=e)
    com_date.grid(row=13, column=1)
    com_val = Entry(enter_root, width=30,text=b)
    com_val.grid(row=14, column=1)
    fir_no = Entry(enter_root, width=30)
    fir_no.grid(row=0, column=4)
    sec = Entry(enter_root, width=30)
    sec.grid(row=1, column=4)
    act = Entry(enter_root, width=30)
    act.grid(row=2, column=4)
    proof_type = Entry(enter_root, width=30,text=n)
    proof_type.grid(row=3, column=4)
    proof_id = Entry(enter_root, width=30,text=n)
    proof_id.grid(row=4, column=4)
    off_name = Entry(enter_root, width=30)
    off_name.grid(row=5, column=4)
    off_id = Entry(enter_root, width=30)
    off_id.grid(row=6, column=4)
    off_type = Entry(enter_root, width=30)
    off_type.grid(row=7, column=4)
    wit_name = Entry(enter_root, width=30,text=l)
    wit_name.grid(row=8, column=4)
    wit_age = Entry(enter_root, width=30,text=l)
    wit_age.grid(row=9, column=4)
    wit_gen = Entry(enter_root, width=30,text=l)
    wit_gen.grid(row=10, column=4)
    wit_ph = Entry(enter_root, width=30,text=l)
    wit_ph.grid(row=11, column=4)
    wit_rel = Entry(enter_root, width=30,text=l)
    wit_rel.grid(row=12, column=4)
    court_da = Entry(enter_root, width=30)
    court_da.grid(row=13, column=4)
    court_pp = Entry(enter_root, width=30)
    court_pp.grid(row=14, column=4)
    court_no = Entry(enter_root, width=30)
    court_no.grid(row=15, column=1)
    court_jud = Entry(enter_root, width=30)
    court_jud.grid(row=16, column=1)
    court_type = Entry(enter_root, width=30)
    court_type.grid(row=17, column=1)
    l1 = Label(enter_root, text=" Complainant Name ")
    l1.grid(row=0, column=0)
    l2 = Label(enter_root, text=" Complainant Age ")
    l2.grid(row=1, column=0)
    l3 = Label(enter_root, text=" Gender ")
    l3.grid(row=2, column=0)
    l4 = Label(enter_root, text=" Complainant ID ")
    l4.grid(row=3, column=0)
    l5 = Label(enter_root, text=" Area ")
    l5.grid(row=4, column=0)
    l6 = Label(enter_root, text=" City ")
    l6.grid(row=5, column=0)
    l7 = Label(enter_root, text=" Convict Name  ")
    l7.grid(row=6, column=0)
    l8 = Label(enter_root, text=" Height ")
    l8.grid(row=7, column=0)
    l9 = Label(enter_root, text=" Gender ")
    l9.grid(row=8, column=0)
    l10 = Label(enter_root, text=" Phone Number ")
    l10.grid(row=9, column=0)
    l11 = Label(enter_root, text=" ID ")
    l11.grid(row=10, column=0)
    l12 = Label(enter_root, text=" Identification ")
    l12.grid(row=11, column=0)
    l13 = Label(enter_root, text=" Complaint No. ")
    l13.grid(row=12, column=0)
    l14 = Label(enter_root, text=" DATE ")
    l14.grid(row=13, column=0)
    l15 = Label(enter_root, text=" Value Lost ")
    l15.grid(row=14, column=0)
    l16 = Label(enter_root, text=" FIR Number ")
    l16.grid(row=0, column=3)
    l17 = Label(enter_root, text=" Section ")
    l17.grid(row=1, column=3)
    l18 = Label(enter_root, text=" Act ")
    l18.grid(row=2, column=3)
    l19 = Label(enter_root, text=" Proof Type ")
    l19.grid(row=3, column=3)
    l20 = Label(enter_root, text=" Proof ID ")
    l20.grid(row=4, column=3)
    l21 = Label(enter_root, text=" Officer Type ")
    l21.grid(row=7, column=3)
    l22 = Label(enter_root, text=" Officer Name ")
    l22.grid(row=5, column=3)
    l23 = Label(enter_root, text=" Officer ID ")
    l23.grid(row=6, column=3)
    l24 = Label(enter_root, text=" Witness Name ")
    l24.grid(row=8, column=3)
    l25 = Label(enter_root, text=" Witness Age ")
    l25.grid(row=9, column=3)
    l26 = Label(enter_root, text=" Gender ")
    l26.grid(row=10, column=3)
    l27 = Label(enter_root, text=" Phone Number ")
    l27.grid(row=11, column=3)
    l28 = Label(enter_root, text=" Relation w Victim ")
    l28.grid(row=12, column=3)
    l29 = Label(enter_root, text=" Defence Lawyer ")
    l29.grid(row=13, column=3)
    l30 = Label(enter_root, text=" Public Prosec. ")
    l30.grid(row=14, column=3)
    l31 = Label(enter_root, text=" Court Number ")
    l31.grid(row=15, column=0)
    l32 = Label(enter_root, text=" Judge ")
    l32.grid(row=16, column=0)
    l33 = Label(enter_root, text=" Court Type ")
    l33.grid(row=17, column=0)

    def submit():

        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()
        try:
            c.execute('''insert into complainant values
                          ( :a1 , :a2 , :a3 , :a4 , :a5 , :b1 , :b2 )''',
                      {
                          'a1': c_name.get(),
                          'a2': c_age.get(),
                          'a3': c_gender.get(),
                          'a4': c_id.get(),
                          'a5': area.get(),
                          'b1': city.get(),
                          'b2': fir_no.get()
                      }
                      )
            conn.commit()
            c.execute('''insert into convict values
                          (:a1, :a2 ,:a3 ,:a4 ,:a5 ,:b1, :b2)''',
                      {
                          'a1': co_name.get(),
                          'a2': co_height.get(),
                          'a3': co_gen.get(),
                          'a4': co_ph.get(),
                          'a5': co_id.get(),
                          'b1': co_iden.get(),
                          'b2': fir_no.get()
                      }
                      )
            conn.commit()
            c.execute('''insert into complaint values
                                  (:a1 ,:a2 ,:a3, :a4, :a5, :b1, :b2, :b3, :b4, :b5, :c1, :c2, :c3 )''',
                      {
                          'a1': com_num.get(),
                          'a2': com_date.get(),
                          'a3': com_val.get(),
                          'a4': fir_no.get(),
                          'a5': sec.get(),
                          'b1': act.get(),
                          'b2': proof_type.get(),
                          'b3': proof_id.get(),
                          'b4': wit_name.get(),
                          'b5': wit_age.get(),
                          'c1': wit_gen.get(),
                          'c2': wit_ph.get(),
                          'c3': wit_rel.get()
                      }
                      )
            conn.commit()
            c.execute('''insert into officer values
                                  (:a1 ,:a2 ,:a3, :a4 )''',
                      {
                          'a1': off_name.get(),
                          'a2': off_type.get(),
                          'a3': off_id.get(),
                          'a4': fir_no.get()
                      }
                      )
            conn.commit()
            c.execute('''insert into court values
                                  (:a1 ,:a2 ,:a3, :a4, :a5, :b1)''',
                      {
                          'a1': court_da.get(),
                          'a2': court_pp.get(),
                          'a3': court_no.get(),
                          'a4': court_jud.get(),
                          'a5': court_type.get(),
                          'b1': fir_no.get()
                      }
                      )
        except sqlite3.IntegrityError:
            messagebox.showerror('ERROR','VALUE NOT ENTERED OR ALREADY EXISTS IN THE DATABASE')

        conn.commit()
        conn.close()()
        c_name.delete(0, END)
        c_age.delete(0, END)
        c_gender.delete(0, END)
        c_id.delete(0, END)
        area.delete(0, END)
        city.delete(0, END),
        co_name.delete(0, END),
        co_height.delete(0, END),
        co_gen.delete(0, END),
        co_ph.delete(0, END),
        co_id.delete(0, END),
        co_iden.delete(0, END),
        com_num.delete(0, END),
        com_date.delete(0, END),
        com_val.delete(0, END),
        fir_no.delete(0, END),
        sec.delete(0, END),
        act.delete(0, END),
        proof_type.delete(0, END),
        proof_id.delete(0, END),
        off_name.delete(0, END),
        off_id.delete(0, END),
        off_type.delete(0, END),
        wit_name.delete(0, END),
        wit_age.delete(0, END),
        wit_gen.delete(0, END),
        wit_ph.delete(0, END),
        wit_rel.delete(0, END),
        court_da.delete(0, END),
        court_pp.delete(0, END),
        court_no.delete(0, END),
        court_jud.delete(0, END),
        court_type.delete(0, END)
    submit_but1 = Button(enter_root, text="SUBMIT", padx=45, relief=RAISED, command=submit)
    submit_but1.grid(row=15, column=4)
    submit_but1.configure(bg='green')
         #  messagebox.showerror('ERROR', 'ALREADY EXISTS IN THE TABLE')
         #except sqlite3.IntegrityError:
        #    messagebox.showerror('ERROR','ALREADY EXISTS IN THE TABLE')
        #except sqlite3.IntegrityError:
        # messagebox.showerror('ERROR','ALREADY EXISTS IN THE TABLE')

retrieve_but=Button(root,text="RETRIEVE",padx=50,pady=6,command=retrieve)
retrieve_but.place(x=120,y=180)

enter_but=Button(root,text="ENTER",padx=50,pady=6,command=enter)
enter_but.place(x=310,y=180)
enter_but=Button(root,text="QUERIES ",padx=50,pady=6,command=query)
enter_but.place(x=50,y=40)
root.mainloop()
