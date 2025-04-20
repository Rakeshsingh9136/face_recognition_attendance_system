from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Developer:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x730+0+0")
                self.root.title("Developer")

                title_lbl=Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="white",fg="blue")
                title_lbl.place(x=0,y=0,width=1530,height=45)

                img2_top=Image.open(r"Images/image4.jpg")
                img2_top=img2_top.resize((1530,710),Image.Resampling.LANCZOS)
                self.photoimg2_top=ImageTk.PhotoImage(img2_top)

                flbl=Label(self.root,image=self.photoimg2_top)
                flbl.place(x=0,y=55,width=1530,height=710) 

# ********************************* Frame ********************************************

                mai_frame=Frame(flbl,bd=2,bg="white")
                mai_frame.place(x=500,y=0,width=600,height=650)

                img1_top=Image.open(r"Images/image5.jpg")
                img1_top=img1_top.resize((200,200),Image.Resampling.LANCZOS)
                self.photoimg3_top=ImageTk.PhotoImage(img1_top)

                flbl1=Label(mai_frame,image=self.photoimg3_top)
                flbl1.place(x=380,y=0,width=200,height=200) 

# *********************************  Developer *********************************************
                Dev_lbl=Label(mai_frame,text="Name:- RAKESH SINGH",font=("times new roman",12,"bold"),bg="white")
                Dev_lbl.place(x=0,y=5)
                Dev_lbl=Label(mai_frame,text="Roll_no:- 191251015026",font=("times new roman",12,"bold"),bg="white")
                Dev_lbl.place(x=0,y=45)

                Dev_lbl=Label(mai_frame,text="Semester:- 8th",font=("times new roman",12,"bold"),bg="white")
                Dev_lbl.place(x=0,y=90)

                Dev_lbl=Label(mai_frame,text="Branch:- Computer Science And Engineering",font=("times new roman",12,"bold"),bg="white")
                Dev_lbl.place(x=0,y=135)

                img4_top=Image.open(r"Images/image6.jpg")
                img4_top=img4_top.resize((600,450),Image.Resampling.LANCZOS)
                self.photoimg4_top=ImageTk.PhotoImage(img4_top)

                flbl1=Label(mai_frame,image=self.photoimg4_top)
                flbl1.place(x=0,y=210,width=600,height=450)




if __name__=="__main__":
        root=Tk()
        obj=Developer(root)
        root.mainloop()