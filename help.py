from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class Help:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x730+0+0")
                self.root.title("Help")

                title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
                title_lbl.place(x=0,y=0,width=1530,height=45)

                img2_top=Image.open(r"Images/image.jpg")
                img2_top=img2_top.resize((1530,710),Image.Resampling.LANCZOS)
                self.photoimg2_top=ImageTk.PhotoImage(img2_top)

                flbl=Label(self.root,image=self.photoimg2_top)
                flbl.place(x=0,y=55,width=1530,height=710) 

                Dev_lbl=Label(flbl,text="Email: rakeshsinghdos2016@yahoo.com",font=("times new roman",12,"bold"),bg="white",fg="green")
                Dev_lbl.place(x=600,y=305)

                Dev_lbl=Label(flbl,text="Mobile: +91-8400267075",font=("times new roman",12,"bold"),bg="white",fg="green")
                Dev_lbl.place(x=600,y=335)



if __name__=="__main__":
        root=Tk()
        obj=Help(root)
        root.mainloop()