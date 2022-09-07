from ast import Try
from logging import exception, root
from tkinter import *
from tkinter import ttk
from webbrowser import get
from PIL import Image, ImageTk
from tkmacosx import Button
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

myData=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2560x1600+0+0")
        self.root.title("Face Recognition System")


        # ============== variables ===========

        self.var_atten_id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_program=StringVar()
        self.var_date=StringVar()
        self.var_time=StringVar()
        self.var_attendance=StringVar()


        # 1st image

        img0 = Image.open(
            "image/st1.jpg")
        img0 = img0.resize((850, 250), Image.ANTIALIAS)
        self.photoimg0 = ImageTk.PhotoImage(img0)

        f_lbl = Label(self.root, image=self.photoimg0)
        f_lbl.place(x=0, y=0, width=850, height=250)

        # 2nd image

        img1 = Image.open(
            "image/st2.jpg")
        img1 = img1.resize((850, 250), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=850, y=0, width=850, height=250)

        # bg image
        img3 = Image.open(
            "image/img7.webp")
        img3 = img3.resize((1680, 1050), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=250, width=1680, height=850)

        # ============= title ==============

        title_lbl = Label(bg_img, text="STUDENT ATTENDANCE SYSTEM", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1680, height=40)

        # ============ main frame==========

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=50, width=1655, height=685)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details", font=(
            "times ner=w roman", 15, "bold"), bg="white")
        Left_frame.place(x=20, y=10, width=790, height=660)

        img_left = Image.open(
            "image/st4.jpg")
        img_left = img_left.resize((780, 200), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=780, height=200)

        details_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Attendance Details", font=(
            "times new roman", 13, "bold"), bg="white")
        details_frame.place(x=5, y=225, width=778, height=350)


        # ========= labels and entry =======
        # ======== attendance id ========
        attendanceId_label = Label(details_frame, text="Attendance ID :", font=(
            "times new roman", 13, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=30, pady=20, sticky=W)

        attendanceId_entry = ttk.Entry(details_frame, width=30,textvariable=self.var_atten_id, font=(
            "times new roman", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=2, pady=20, sticky=W)

        # ========= name ============
        name_label = Label(details_frame, text="Name :", font=(
            "times new roman", 13, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx=30, pady=20, sticky=W)

        name_entry = ttk.Entry(details_frame, width=30,textvariable=self.var_name, font=(
            "times new roman", 12, "bold"))
        name_entry.grid(row=0, column=3, padx=2, pady=20, sticky=W)

        # =========== roll ===========

        roll_label = Label(details_frame, text="Roll No :", font=(
            "times new roman", 13, "bold"), bg="white")
        roll_label.grid(row=1, column=0, padx=30, pady=20, sticky=W)

        roll_entry = ttk.Entry(details_frame, width=30,textvariable=self.var_roll, font=(
            "times new roman", 12, "bold"))
        roll_entry.grid(row=1, column=1, padx=2, pady=20, sticky=W)

        # ============ program ==========

        program_label = Label(details_frame, text="Program :", font=(
            "times new roman", 13, "bold"), bg="white")
        program_label.grid(row=1, column=2, padx=30, pady=20, sticky=W)

        program_entry = ttk.Entry(details_frame, width=30,textvariable=self.var_program, font=(
            "times new roman", 12, "bold"))
        program_entry.grid(row=1, column=3, padx=2, pady=20, sticky=W)

        # ============= time ============

        time_label = Label(details_frame, text="Time :", font=(
            "times new roman", 13, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=30, pady=20, sticky=W)

        time_entry = ttk.Entry(details_frame, width=30, textvariable=self.var_time, font=(
            "times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=2, pady=20, sticky=W)

        # ============ date ===========

        date_label = Label(details_frame, text="Date :", font=(
            "times new roman", 13, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=30, pady=20, sticky=W)

        date_entry = ttk.Entry(details_frame, width=30,textvariable=self.var_date, font=(
            "times new roman", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=2, pady=20, sticky=W)



        # ============ attendance ========

        atten_label = Label(details_frame, text="Status", font=(
            "times new roman", 13, "bold"), bg="white")
        atten_label.grid(row=3, column=0, padx=30,pady=20, sticky=W)

        atten_combo = ttk.Combobox(details_frame, state="readonly",textvariable=self.var_attendance, font=(
            "times new roman", 13, "bold"), width=30)
        atten_combo["values"] = ("Select Status", "Present", "Absent")
        atten_combo.current(0)
        atten_combo.grid(row=3, column=1, padx=2, pady=20, sticky=W)

        # buttons frame

        btn_frame = Frame(details_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=280, width=773, height=50)

        #import
        import_btn = Button(btn_frame, text="Import CSV", command=self.importCSV, font=(
            "times ner=w roman", 12, "bold"), bg="blue", fg="white", cursor="hand", width=255, height=50)
        import_btn.grid(row=0, column=0)

        # export
        export_btn = Button(btn_frame, text="Export CSV",  command=self.exportCSV, font=(
            "times ner=w roman", 12, "bold"), bg="blue", fg="white", cursor="hand", width=255, height=50)
        export_btn.grid(row=0, column=1)

        # update
        # update_btn = Button(btn_frame, text="Update", font=(
        #     "times ner=w roman", 12, "bold"), bg="blue", fg="white", cursor="hand", width=192, height=50)
        # update_btn.grid(row=0, column=2)

        # Reset
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data,font=(
            "times ner=w roman", 12, "bold"), bg="blue", fg="white", cursor="hand", width=255, height=50)
        reset_btn.grid(row=0, column=2)

        # right label frame

        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details", font=(
            "times new roman", 12, "bold"), bg="white")
        Right_frame.place(x=840, y=10, width=790, height=660)

        # ========= Table Frame ========

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=778, height=630)

        # scroll bar ====================

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,
                                          columns=("id","name","roll","program","time","date","attendance"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("program",text="Program")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=150)
        self.AttendanceReportTable.column("name",width=200)
        self.AttendanceReportTable.column("roll",width=150)
        self.AttendanceReportTable.column("program",width=200)
        self.AttendanceReportTable.column("time",width=200)
        self.AttendanceReportTable.column("date",width=200)
        self.AttendanceReportTable.column("attendance",width=150)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)




        # ================= fetch data ======================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    #     =================== import csv ============

    def importCSV(self):
        global myData
        myData.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvRead=csv.reader(myfile,delimiter=",")
            for i in csvRead:
                myData.append(i)
            self.fetchData(myData)

#     ================ export csv ==============

    def exportCSV(self):
        try:
            if len(myData)<1:
                messagebox.showerror("Error","No Data Found",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",
                                         filetypes=(("CSV File", "*.csv"),("All File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Data Exported Successfully To "+os.path.basename(fln))
        except exception as es:
            messagebox.showerror(
            "Error", f"Due To:{str(es)}", parent=self.root)



    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_name.set(rows[1])
        self.var_roll.set(rows[2])
        self.var_program.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance.set(rows[6])


        # =========== reset ===========

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_program.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("Select Status")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
