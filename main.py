import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from tkmacosx import Button
from time import strftime
from datetime import datetime
from student import Student
import subprocess
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2560x1600+0+0")
        self.root.title("Face Recognition System")


        # 1st image

        img0 = Image.open(
            "image/img5.jpg")
        img0 = img0.resize((565, 150), Image.ANTIALIAS)
        self.photoimg0 = ImageTk.PhotoImage(img0)

        f_lbl = Label(self.root, image=self.photoimg0)
        f_lbl.place(x=0, y=0, width=565, height=150)

        # 2nd image

        img1 = Image.open(
            "image/img3.jpg")
        img1 = img1.resize((565, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=565, y=0, width=565, height=150)

        # 3rd imgae

        img2 = Image.open(
            "image/img1.jpg")
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

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1680, height=40)

        # ========== time=========

        def time():
            string = strftime('%H:%M:%S ')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',20,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=30)
        time()

       

        # Student button
        img4 = Image.open(
            "image/student.jpg")
        img4 = img4.resize((250, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,
                    command=self.student_details, cursor="hand")
        b1.place(x=300, y=150, width=250, height=220)

        b1_1 = Button(bg_img, command=self.student_details, text="Student Details", cursor="hand", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=300, y=350, width=250, height=40)

        # Detect face button
        img5 = Image.open(
            "image/img8.jpg")
        img5 = img5.resize((250, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand",command=self.face_data,)
        b1.place(x=650, y=150, width=250, height=220)

        b1_1 = Button(bg_img, text="Face Recognition", cursor="hand",command=self.face_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=650, y=350, width=250, height=40)

        # Attendance button
        img6 = Image.open(
            "image/Best-attendance.jpg")
        img6 = img6.resize((250, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand",command=self.attendance_data)
        b1.place(x=1000, y=150, width=250, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand", command=self.attendance_data,font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1000, y=350, width=250, height=40)


        # Train Face button
        img8 = Image.open(
            "image/img4.webp")
        img8 = img8.resize((250, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand",command=self.train_data,)
        b1.place(x=300, y=500, width=250, height=220)

        b1_1 = Button(bg_img, text="Train Face Data", cursor="hand",command=self.train_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=300, y=700, width=250, height=40)

        # Photos Face button
        img9 = Image.open(
            "image/photos.jpg")
        img9 = img9.resize((250, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9,
                    cursor="hand", command=self.open_img)
        b1.place(x=650, y=500, width=250, height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand", command=self.open_img, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=650, y=700, width=250, height=40)

        # Logout button
        img10 = Image.open(
            "image/logout.jpg")
        img10 = img10.resize((250, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10,
                    cursor="hand",command=self.iExit)
        b1.place(x=1000, y=500, width=250, height=220)

        b1_1 = Button(bg_img, text="Logout", cursor="hand",command=self.iExit, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1000, y=700, width=250, height=40)


        # ================ open data folder =============

    def open_img(self):
        subprocess.Popen(["open", 'data'])

        # ================ Function buttons ==========

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
