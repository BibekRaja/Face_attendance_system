from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
from tkmacosx import Button
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2560x1600+0+0")
        self.root.title("Face Recognition System")

        # ============= title ==============

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1680, height=60)

        # ======== top img =========

        img_top = Image.open(
            "image/img5.jpg")
        img_top = img_top.resize((1680, 400), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=65, width=1680, height=400)

        # ======== button =========

        b1_1 = Button(self.root, text="TRAIN DATA", cursor="hand", command=self.train_classifier, font=(
            "times new roman", 35, "bold"), bg="green", fg="white")
        b1_1.place(x=0, y=485, width=1680, height=90)

        # ======== bottom img ========

        img_bottom = Image.open(
            "image/train.jpg")
        img_bottom = img_bottom.resize((1680, 400), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=600, width=1680, height=400)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            # Gray Scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # ========= train the classifier and save =========

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo(
            "Result", "Training data set completed!!", parent=self.root)


# ===obj======
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()