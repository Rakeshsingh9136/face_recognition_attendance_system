from tkinter import *
from tkinter import ttk
from time import strftime
from datetime import datetime
import tkinter
from PIL import Image,ImageTk
from student import Student
from train import train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer
from help import Help
import os
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]


class Face_recognition_system:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x730+0+0")
                self.root.title("Face Recognition System")

                img=Image.open(r"Images/image.jpg")
                img=img.resize((550,130),Image.Resampling.LANCZOS)
                self.photoimg=ImageTk.PhotoImage(img)

                flbl=Label(self.root,image=self.photoimg)
                flbl.place(x=0,y=0,width=550,height=130)       

                img1=Image.open(r"Images/image1.jpg")
                img1=img1.resize((550,130),Image.Resampling.LANCZOS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                flbl=Label(self.root,image=self.photoimg1)
                flbl.place(x=500,y=0,width=550,height=130)            

                img2=Image.open(r"Images/image2.jpeg")
                img2=img2.resize((550,130),Image.Resampling.LANCZOS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                flbl=Label(self.root,image=self.photoimg2)
                flbl.place(x=1000,y=0,width=550,height=130)  

                img3=Image.open(r"Images/image3.jpg")
                img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                bg_img=Label(self.root,image=self.photoimg3)
                bg_img.place(x=0,y=130,width=1530,height=800)            

# label creating for the system
                title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
                title_lbl.place(x=0,y=0,width=1530,height=45)


# ******************************** Time **************************************************
                def time():
                        string=strftime('%H:%M:%S %p')
                        lbl.config(text=string)
                        lbl.after(1000,time)
                lbl=Label(title_lbl,font=("times new roman",12,"bold"),bg="white",fg="black")
                lbl.place(x=0,y=0,width=110,height=50)
                time()
 #   buttons1 in the face recognition

                img4=Image.open(r"Images/image4.jpg")
                img4=img4.resize((220,220),Image.Resampling.LANCZOS)
                self.photoimg4=ImageTk.PhotoImage(img4)

                b1=Button(bg_img,command=self.student_details,image=self.photoimg4,cursor="hand2")
                b1.place(x=200,y=100,width=220,height=220)

                b1_1=Button(bg_img,command=self.student_details,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="yellow")
                b1_1.place(x=200,y=320,width=220,height=40)

#   buttons2 in the face recognition

                img5=Image.open(r"Images/image5.jpg")
                img5=img5.resize((500,220),Image.Resampling.LANCZOS)
                self.photoimg5=ImageTk.PhotoImage(img5)

                b2=Button(bg_img,command=self.face_data,image=self.photoimg5,cursor="hand2")
                b2.place(x=500,y=100,width=220,height=220)

                b2_1=Button(bg_img,command=self.face_data,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="yellow")
                b2_1.place(x=500,y=320,width=220,height=40)

#   buttons3 in the Attendence face recognition

                img6=Image.open(r"Images/image6.jpg")
                img6=img6.resize((220,220),Image.Resampling.LANCZOS)
                self.photoimg6=ImageTk.PhotoImage(img6)

                b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
                b3.place(x=800,y=100,width=220,height=220)

                b3_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="green",fg="yellow")
                b3_1.place(x=800,y=320,width=220,height=40)

#   buttons4 in the face recognition

                img7=Image.open(r"Images/image7.jpg")
                img7=img7.resize((220,220),Image.Resampling.LANCZOS)
                self.photoimg7=ImageTk.PhotoImage(img7)

                b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.Help_data)
                b4.place(x=1100,y=100,width=220,height=220)

                b1_1=Button(bg_img,text="Help",cursor="hand2",command=self.Help_data,font=("times new roman",15,"bold"),bg="green",fg="yellow")
                b1_1.place(x=1100,y=320,width=220,height=40)

#   bottom buttons1 in the face recognition

                img8=Image.open(r"Images/image8.jpg")
                img8=img8.resize((220,220),Image.Resampling.LANCZOS)
                self.photoimg8=ImageTk.PhotoImage(img8)

                b5=Button(bg_img,command=self.train_data,image=self.photoimg8,cursor="hand2")
                b5.place(x=200,y=400,width=220,height=220)

                b5_1=Button(bg_img,command=self.train_data,text="Train face",cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="yellow")
                b5_1.place(x=200,y=600,width=220,height=40)


#   bottom buttons2 in the face recognition

                img9=Image.open(r"Images/image9.jpg")
                img9=img9.resize((220,220),Image.Resampling.LANCZOS)
                self.photoimg9=ImageTk.PhotoImage(img9)

                b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
                b6.place(x=500,y=400,width=220,height=220)

                b6_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="green",fg="yellow")
                b6_1.place(x=500,y=600,width=220,height=40)


#   bottom buttons3 in the face recognition

                img10=Image.open(r"Images/image10.jpg")
                img10=img10.resize((220,220),Image.Resampling.LANCZOS)
                self.photoimg10=ImageTk.PhotoImage(img10)

                b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.Developer_data)
                b7.place(x=800,y=400,width=220,height=220)

                b7_1=Button(bg_img,text="Developer",cursor="hand2",command=self.Developer_data,font=("times new roman",15,"bold"),bg="green",fg="yellow")
                b7_1.place(x=800,y=600,width=220,height=40)

#   bottom buttons3 in the face recognition

                img11=Image.open(r"Images/image.jpg")
                img11=img11.resize((220,220),Image.Resampling.LANCZOS)
                self.photoimg11=ImageTk.PhotoImage(img11)

                b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit_data)
                b8.place(x=1100,y=400,width=220,height=220)

                b8_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit_data,font=("times new roman",15,"bold"),bg="green",fg="yellow")
                b8_1.place(x=1100,y=600,width=220,height=40)

                # ******************************** Training the Image ********************************
        def open_img(self):
                os.startfile("data")
                # *********************************** Function Buttons *****************************************

        def student_details(self):
                self.new_window=Toplevel(self.root)
                self.app=Student(self.new_window)

        def train_data(self):
                self.new_window=Toplevel(self.root)
                self.app=train(self.new_window)

        def face_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition(self.new_window)

        def attendance_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Attendence(self.new_window)
        

        def Developer_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Developer(self.new_window)
        

        def Help_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Help(self.new_window)


        def exit_data(self):
                self.exit_data=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this window",parent=self.root)

                if self.exit_data>0:
                        self.root.destroy()
                else:
                        return






                
if __name__=="__main__":
        root=Tk()
        obj=Face_recognition_system(root)
        root.mainloop()








        