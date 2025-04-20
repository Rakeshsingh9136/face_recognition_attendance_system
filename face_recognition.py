from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import numpy as np
import os


class Face_Recognition:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x730+0+0")
                self.root.title("Face Recognition System")

                # Label
                title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
                title_lbl.place(x=0,y=0,width=1530,height=45)

                # First Image
                img2_top=Image.open(r"Images/image7.jpg")
                img2_top=img2_top.resize((650,700),Image.Resampling.LANCZOS)
                self.photoimg2_top=ImageTk.PhotoImage(img2_top)

                flbl=Label(self.root,image=self.photoimg2_top)
                flbl.place(x=0,y=55,width=650,height=700) 

                # Second Image
                img3_down=Image.open(r"Images/image8.jpg")
                img3_down=img3_down.resize((950,700),Image.Resampling.LANCZOS)
                self.photoimg3_down=ImageTk.PhotoImage(img3_down)

                bg_img=Label(self.root,image=self.photoimg3_down)
                bg_img.place(x=650,y=55,width=950,height=700)

                # Button
                b1_1=Button(bg_img,command=self.face_recog,text="Face Recognition",cursor="hand2",font=("times new roman",16,"bold"),bg="red",fg="white")
                b1_1.place(x=370,y=600,width=200,height=40)

        # ============================ Attendance ================================
        def mark_attendence(self,i,r,n,d):
                with open("rak.csv","r+",newline="\n") as f:
                        mydatalist=f.readlines()
                        name_linst=[]
                        for line in mydatalist:
                                entry=line.split(",")
                                name_linst.append(entry[0])
                        if((i not in name_linst) and (r not in name_linst) and (n not in name_linst) and (d not in name_linst)):
                                now=datetime.now()
                                d1=now.strftime("%d/%m/%Y")
                                dtstring=now.strftime("%H:%M:%S")
                                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")


        # ========================== Face Recognition ============================
        def face_recog(self):
                def draw_boundary(img, classifier, scalefactor, minNeighbours, color, text, clf):
                        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        features = classifier.detectMultiScale(gray_image, scalefactor, minNeighbours)
                        cord = []

                        for (x, y, w, h) in features:
                                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                                confidence = int((100 * (1 - predict / 300)))

                                conn = mysql.connector.connect(host="localhost", username="root", password="", database="mydata")
                                my_cursor = conn.cursor()
                                
                                my_cursor.execute("select Name from student where student_id=" + str(id))
                                n = my_cursor.fetchone()
                                n = "+".join(str(x) for x in n) if n else ""

                                my_cursor.execute("select Roll_No from student where student_id=" + str(id))
                                r = my_cursor.fetchone()
                                r = "+".join(str(x) for x in r) if r else ""

                                my_cursor.execute("select Dep from student where student_id=" + str(id))
                                d = my_cursor.fetchone()
                                d = "+".join(str(x) for x in d) if d else ""

                                my_cursor.execute("select student_id from student where student_id=" + str(id))
                                i = my_cursor.fetchone()
                                i = "+".join(str(x) for x in i) if i else ""

                                if confidence > 77:
                                        cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                        cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                        cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                        cv2.putText(img, f"Dep:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                        self.mark_attendence(i, r, n, d)
                                        return True  # Face recognized and attendance marked
                                else:
                                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                                        cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                        return False

                def recognize(img, clf, face_cascad):
                        return draw_boundary(img, face_cascad, 1.1, 10, (255, 255, 255), "Face", clf)

                face_cascad = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                clf = cv2.face.LBPHFaceRecognizer_create()
                clf.read("classifier.xml")

                video_cap = cv2.VideoCapture(0)

                while True:
                        ret, img = video_cap.read()
                        recognized = recognize(img, clf, face_cascad)
                        cv2.imshow("Welcome to Face Recognition", img)

                        if recognized:
                                messagebox.showinfo("Attendance", "Attendance marked. Closing camera.")
                                break
                        if cv2.waitKey(1) == 13:  # Press Enter key to exit manually
                                break

                video_cap.release()
                cv2.destroyAllWindows()



if __name__=="__main__":
        root=Tk()
        obj=Face_Recognition(root)
        root.mainloop()
