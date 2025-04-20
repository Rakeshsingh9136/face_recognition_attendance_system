from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import os
import csv

mydata = []

class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x730+0+0")
        self.root.title("Attendance of Students")

        # ********************** Variables **********************
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_Attendance = StringVar()

        # ********************** Images **********************
        img = Image.open(r"Images/image7.jpg").resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=800, height=200)

        img1 = Image.open(r"Images/image8.jpg").resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=800, y=0, width=800, height=200)

        img3 = Image.open(r"Images/image9.jpg").resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ********************** Main Frame **********************
        mai_frame = Frame(bg_img, bd=2)
        mai_frame.place(x=10, y=60, width=1500, height=650)

        # ********************** Left Frame **********************
        left_frame = LabelFrame(mai_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 12, "bold"))
        left_frame.place(x=40, y=10, width=710, height=580)

        img_left = Image.open(r"Images/image10.jpg").resize((710, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(left_frame, image=self.photoimg_left).place(x=20, y=0, width=710, height=130)

        l_Inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        l_Inside_frame.place(x=0, y=135, width=700, height=370)

        # ********************** Labels and Entries **********************
        Label(l_Inside_frame, text="Attendance_Id:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(l_Inside_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 12, "bold")).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        Label(l_Inside_frame, text="Roll:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(l_Inside_frame, width=20, textvariable=self.var_atten_roll, font=("times new roman", 12, "bold")).grid(row=0, column=3, padx=10, pady=5, sticky=W)

        Label(l_Inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(l_Inside_frame, width=20, textvariable=self.var_atten_name, font=("times new roman", 12, "bold")).grid(row=1, column=1, padx=10, pady=5, sticky=W)

        Label(l_Inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(l_Inside_frame, width=20, textvariable=self.var_atten_dep, font=("times new roman", 12, "bold")).grid(row=1, column=3, padx=10, pady=5, sticky=W)

        Label(l_Inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(l_Inside_frame, width=20, textvariable=self.var_atten_time, font=("times new roman", 12, "bold")).grid(row=2, column=1, padx=10, pady=5, sticky=W)

        Label(l_Inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(l_Inside_frame, width=20, textvariable=self.var_atten_date, font=("times new roman", 12, "bold")).grid(row=2, column=3, padx=10, pady=5, sticky=W)

        Label(l_Inside_frame, text="Attendance_Status:", font=("times new roman", 12, "bold"), bg="white").grid(row=3, column=0)
        self.atten_status = ttk.Combobox(l_Inside_frame, width=20, textvariable=self.var_atten_Attendance,
                                         font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        self.atten_status.current(0)

        # ********************** Button Frame **********************
        btn_frame = Frame(l_Inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=50, y=250, width=715, height=40)

        Button(btn_frame, text="Import CSV", command=self.importcsv, width=18, font=("times new roman", 12, "bold"),
               bg="blue", fg="yellow").grid(row=0, column=0)
        Button(btn_frame, text="Export CSV", command=self.exportcsv, width=18, font=("times new roman", 12, "bold"),
               bg="blue", fg="yellow").grid(row=0, column=1)
        Button(btn_frame, text="Reset", command=self.reset_data, width=18, font=("times new roman", 12, "bold"),
               bg="blue", fg="yellow").grid(row=0, column=2)

        # ********************** Right Frame **********************
        right_frame = LabelFrame(mai_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=710, height=580)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=690, height=445)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendaceReportTable = ttk.Treeview(table_frame,
                                                 column=("Id", "Roll", "Name", "Department", "time", "date", "Attendance"),
                                                 xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("Id", text="Attendance_id")
        self.AttendaceReportTable.heading("Roll", text="Roll")
        self.AttendaceReportTable.heading("Name", text="Name")
        self.AttendaceReportTable.heading("Department", text="Department")
        self.AttendaceReportTable.heading("time", text="Time")
        self.AttendaceReportTable.heading("date", text="Date")
        self.AttendaceReportTable.heading("Attendance", text="Attendance")

        self.AttendaceReportTable["show"] = "headings"

        self.AttendaceReportTable.column("Id", width=100)
        self.AttendaceReportTable.column("Roll", width=100)
        self.AttendaceReportTable.column("Name", width=100)
        self.AttendaceReportTable.column("Department", width=100)
        self.AttendaceReportTable.column("time", width=100)
        self.AttendaceReportTable.column("date", width=100)
        self.AttendaceReportTable.column("Attendance", width=100)

        self.AttendaceReportTable.pack(fill=BOTH, expand=1)
        self.AttendaceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # ********************** Fetch Data to Table **********************
    def fetchdata(self, rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for row in rows:
            self.AttendaceReportTable.insert("", END, values=row)

    # ********************** Fixed Import CSV **********************
    def importcsv(self):
        global mydata
        mydata.clear()
        try:
            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                             filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            if not fln:
                return
            with open(fln, newline="") as myfile:
                csvreader = csv.reader(myfile)
                header_skipped = False
                for row in csvreader:
                    if not row or len(row) < 7:
                        continue
                    if not header_skipped and row[0].lower() in ["attendance_id", "id", "attendanceid"]:
                        header_skipped = True
                        continue
                    if len(row) == 7:
                        mydata.append(row)
                self.fetchdata(mydata)

        except Exception as e:
            messagebox.showerror("Error", f"Error importing CSV:\n{str(e)}", parent=self.root)

    # ********************** Export CSV **********************
    def exportcsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",
                                               defaultextension=".csv",
                                               filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                                               parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile)
                for row in mydata:
                    exp_write.writerow(row)
                messagebox.showinfo("Export Successful", f"Your data has been exported to {os.path.basename(fln)}", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)

    # ********************** Get Cursor **********************
    def get_cursor(self, event=""):
        cursor_row = self.AttendaceReportTable.focus()
        content = self.AttendaceReportTable.item(cursor_row)
        row = content['values']
        if row:
            self.var_atten_id.set(row[0])
            self.var_atten_roll.set(row[1])
            self.var_atten_name.set(row[2])
            self.var_atten_dep.set(row[3])
            self.var_atten_time.set(row[4])
            self.var_atten_date.set(row[5])
            self.var_atten_Attendance.set(row[6])

    # ********************** Reset Data **********************
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_Attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()
