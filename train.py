from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os


class train:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x730+0+0")
                self.root.title("Train the face")

                title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
                title_lbl.place(x=0,y=0,width=1530,height=45)

                img2_top=Image.open(r"Images/image.jpg")
                img2_top=img2_top.resize((1530,325),Image.Resampling.LANCZOS)
                self.photoimg2_top=ImageTk.PhotoImage(img2_top)

                flbl=Label(self.root,image=self.photoimg2_top)
                flbl.place(x=0,y=55,width=1530,height=325)  


                        # Button
                b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",16,"bold"),bg="red",fg="white")
                b1_1.place(x=0,y=330,width=1530,height=60)



                img3_down=Image.open(r"Images/image1.jpg")
                img3_down=img3_down.resize((1530,710),Image.Resampling.LANCZOS)
                self.photoimg3_down=ImageTk.PhotoImage(img3_down)

                bg_img=Label(self.root,image=self.photoimg3_down)
                bg_img.place(x=0,y=390,width=1530,height=500)

        def train_classifier(self):
                data_dir=("data")
                path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
                faces=[]
                ids=[]

                for image in path:
                        img=Image.open(image).convert('L') #Gray scale Image
                        imageNp=np.array(img,'uint8')
                        id=int(os.path.split(image)[1].split('.')[1])

                        faces.append(imageNp)
                        ids.append(id)

                        cv2.imshow("Training",imageNp)
                        cv2.waitKey(1)==13
                ids=np.array(ids)

                
                # ****************************** Train Te Classifier and save *************************************
                clf=cv2.face.LBPHFaceRecognizer_create()
                clf.train(faces,ids)
                clf.write("classifier.xml")
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Training Datasets completed !!!")




if __name__=="__main__":
        root=Tk()
        obj=train(root)
        root.mainloop()