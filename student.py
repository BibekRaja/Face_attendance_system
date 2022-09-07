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


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2560x1600+0+0")
        self.root.title("Face Recognition System")

        # ============= Variables ==========
        self.var_faculty = StringVar()
        self.var_program = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_add = StringVar()
        self.var_dob = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()

        # 1st image

        img0 = Image.open(
            "image/st1.jpg")
        img0 = img0.resize((565, 150), Image.ANTIALIAS)
        self.photoimg0 = ImageTk.PhotoImage(img0)

        f_lbl = Label(self.root, image=self.photoimg0)
        f_lbl.place(x=0, y=0, width=565, height=150)

        # 2nd image

        img1 = Image.open(
            "image/st2.jpg")
        img1 = img1.resize((565, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=565, y=0, width=565, height=150)

        # 3rd imgae

        img2 = Image.open(
            "image/st3.jpg")
        img2 = img2.resize((565, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1130, y=0, width=565, height=150)

        # bg image
        img3 = Image.open(
            "image/img7.webp")
        img3 = img3.resize((1680, 1050), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=150, width=1680, height=1050)

        # ============= title ==============

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1680, height=40)

        # frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=50, width=1655, height=785)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
            "times ner=w roman", 15, "bold"), bg="white")
        Left_frame.place(x=20, y=10, width=790, height=750)

        img_left = Image.open(
            "image/st4.jpg")
        img_left = img_left.resize((780, 200), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=780, height=200)

        # current course information
        current_course_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Current Course Information", font=(
            "times new roman", 13, "bold"), bg="white")
        current_course_frame.place(x=5, y=205, width=778, height=150)

        # department
        dep_label = Label(current_course_frame, text="Faculty", font=(
            "times new roman", 12, "bold"), bg="white",)

        dep_label.grid(row=0, column=0, padx=50, sticky=W,)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_faculty, state="readonly", font=(
            "times new roman", 12, "bold"), width=30)
        dep_combo["values"] = ("Select Faculty",
                               "Science and Technology", "Management")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Program", font=(
            "times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=50, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_program, state="readonly", font=(
            "times new roman", 12, "bold"), width=30)
        course_combo["values"] = ("Select Program",
                                  "B.E. Computer", "BIT", "BCA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year
        year_label = Label(current_course_frame, text="Year", font=(
            "times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=50, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, state="readonly", font=(
            "times new roman", 12, "bold"), width=30)
        year_combo["values"] = ("Select Year",
                                "2017-2021", "2018-2022", "2019-2023", "2020-2024", "2021-2025", "2022-2026")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=(
            "times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=50, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, state="readonly", font=(
            "times new roman", 12, "bold"), width=30)
        semester_combo["values"] = ("Select Semester", "First", "Second", "Third", "Fourth", "Fifth", "Six", "Seventh", "Eight")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student information
        class_student_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Class Student Information", font=(
            "times new roman", 13, "bold"), bg="white")
        class_student_frame.place(x=5, y=360, width=778, height=350)

        # student id
        studentID_label = Label(class_student_frame, text="StudentID :", font=(
            "times new roman", 12, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=30, pady=10, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_id, width=30, font=(
            "times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # student name
        studentName_label = Label(class_student_frame, text="Student Name :", font=(
            "times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=30, pady=10, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_name, width=30, font=(
            "times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Roll No.
        roll_no_label = Label(class_student_frame, text="Roll No. :", font=(
            "times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=1, column=0, padx=30, pady=10, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=30, font=(
            "times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Gender

        gender_label = Label(class_student_frame, text="Gender :", font=(
            "times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=1, column=2, padx=30, pady=10, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, state="readonly", font=(
            "times new roman", 12, "bold"), width=28)
        gender_combo["values"] = ("Select Gender",
                                  "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Email
        Email_label = Label(class_student_frame, text="Email :", font=(
            "times new roman", 12, "bold"), bg="white")
        Email_label.grid(row=2, column=0, padx=30, pady=10, sticky=W)

        Email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=30, font=(
            "times new roman", 12, "bold"))
        Email_entry.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # Address

        address_label = Label(class_student_frame, text="Address :", font=(
            "times new roman", 12, "bold"), bg="white")
        address_label.grid(row=2, column=2, padx=30, pady=10, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_add, width=30, font=(
            "times new roman", 12, "bold"))
        address_entry.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        # DOB.

        dob_label = Label(class_student_frame, text="DOB :", font=(
            "times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=3, column=0, padx=30, pady=10, sticky=W)
        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=30, font=(
            "times new roman", 12, "bold"))
        dob_entry.grid(row=3, column=1, padx=2, pady=10, sticky=W)

        # Mobile No.
        Mobile_no_label = Label(class_student_frame, text="Mobile No. :", font=(
            "times new roman", 12, "bold"), bg="white")
        Mobile_no_label.grid(row=3, column=2, padx=30, pady=10, sticky=W)

        Mobile_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_mobile, width=30, font=(
            "times new roman", 12, "bold"))
        Mobile_no_entry.grid(row=3, column=3, padx=2, pady=10, sticky=W)

        # radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=4, column=0, padx=35, pady=10, sticky=W)

        radiobtn2 = ttk.Radiobutton(
            class_student_frame,  text="No Photo Sample", variable=self.var_radio1, value="No")
        radiobtn2.grid(row=4, column=1, padx=35, pady=10, sticky=W)

        # buttons frame

        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=220, width=773, height=50)

        # save
        save_btn = Button(btn_frame, text="Save", command=self.add_data, font=(
            "times ner=w roman", 12, "bold"), bg="blue", fg="white", cursor="hand", width=192, height=50)
        save_btn.grid(row=0, column=0)

        # update
        update_btn = Button(btn_frame, text="Update", command=self.update_data, font=(
            "times ner=w roman", 12, "bold"), bg="blue", fg="white", cursor="hand", width=192, height=50)
        update_btn.grid(row=0, column=1)

        # delete
        dlt_btn = Button(btn_frame, text="Delete", command=self.delete_data, font=(
            "times ner=w roman", 12, "bold"), bg="blue", fg="white", cursor="hand", width=192, height=50)
        dlt_btn.grid(row=0, column=2)

        # Reset
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, font=(
            "times ner=w roman", 12, "bold"), bg="blue", fg="white", cursor="hand", width=192, height=50)
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=270, width=773, height=50)

        # take a photo
        take_photo_btn = Button(btn_frame1, text="Take Photo Sample", command=self.generate_dataset, font=(
            "times ner=w roman", 12, "bold"), bg="blue", fg="white", cursor="hand", width=800, height=50)
        take_photo_btn.grid(row=0, column=0)

        # update photo


        # right label frame

        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"), bg="white")
        Right_frame.place(x=840, y=10, width=790, height=750)

        # rigth image
        img_right = Image.open(
            "image/st5.jpg")
        img_right = img_right.resize((780, 200), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=780, height=200)





        # ========= Table Frame ========

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=210, width=778, height=500)

        # scroll bar ====================

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("faculty", "program", "year", "sem",   "id", "name", "roll",
                                          "gender", "email", "add", "dob", "mobile", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # heading=================
        self.student_table.heading("faculty", text="Faculty")
        self.student_table.heading("program", text="Program")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student Id")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("add", text="Address")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("mobile", text="Mobile No")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("faculty", width=200)
        self.student_table.column("program", width=200)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=200)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("email", width=200)
        self.student_table.column("add", width=200)
        self.student_table.column("dob", width=100)
        self.student_table.column("mobile", width=200)

        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ============== Function decleration ===========

    def add_data(self):
        if self.var_faculty.get() == "Select Faculty" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="127.0.0.1", username="root", password="testroot@1", database="face")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_faculty.get(),
                    self.var_program.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_add.get(),
                    self.var_dob.get(),
                    self.var_mobile.get(),
                    self.var_radio1.get()


                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student details has been added Successfully", parent=self.root)
            except exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

      # ====================== fetch data ==================

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="127.0.0.1", username="root", password="testroot@1", database="face")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

        # ================== get cursor ====================

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_faculty.set(data[0]),
        self.var_program.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_email.set(data[8]),
        self.var_add.set(data[9]),
        self.var_dob.set(data[10]),
        self.var_mobile.set(data[11]),
        self.var_radio1.set(data[12])

    #  ============== update function =============

    def update_data(self):
        if self.var_faculty.get() == "Select Faculty" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                Upadate = messagebox.askyesno(
                    "Update", "Do you want to update this student details?", parent=self.root)
                if Upadate > 0:
                    conn = mysql.connector.connect(
                        host="127.0.0.1", username="root", password="testroot@1", database="face")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Faculty=%s,Program=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Email=%s,Address=%s,DOB=%s,Mobile=%s,Photosample=%s where Student_id=%s", (
                        self.var_faculty.get(),
                        self.var_program.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_add.get(),
                        self.var_dob.get(),
                        self.var_mobile.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))

                    conn.commit()
                    self.fetch_data()

                    conn.close()

                else:
                    if not Upadate:
                        return
                messagebox.showinfo(
                    "Success", "Student details successfully updated.", parent=self.root)

            except exception as es:
                messagebox.showerror(
                    "Error", f"Due To: {str(es)}", parent=self.root)


#  ================ delete function ============


    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Error", "Student Id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page", "Do you want to delete the student details?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="127.0.0.1", username="root", password="testroot@1", database="face")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Deleted", "Successfully deleted student details", parent=self.root)
            except exception as es:
                messagebox.showerror(
                    "Error", f"Due To: {str(es)}", parent=self.root)

    # ==================== reset function ==============
    def reset_data(self):
        self.var_faculty.set("Select Faculty"),
        self.var_program.set("Select Program"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_email.set(""),
        self.var_add.set(""),
        self.var_dob.set(""),
        self.var_mobile.set(""),
        self.var_radio1.set("")

      # ==================== Generate data set or Take photo samples =============

    def generate_dataset(self):

        if self.var_faculty.get() == "Select Faculty" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="127.0.0.1", username="root", password="testroot@1", database="face")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Faculty=%s,Program=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Email=%s,Address=%s,DOB=%s,Mobile=%s,Photosample=%s where Student_id=%s", (
                    self.var_faculty.get(),
                    self.var_program.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_add.get(),
                    self.var_dob.get(),
                    self.var_mobile.get(),
                    self.var_radio1.get(),
                    self.var_id.get() == id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ========== Load predifined data on face frontal form opencv =========

                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3
                    # Minimun Neighobr=5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo(
                    "Result", "Generating data set completed !!!", parent=self.root)

            except exception as es:
                messagebox.showerror(
                    "Error", f"Due To: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
