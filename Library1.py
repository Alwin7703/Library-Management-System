import datetime
from tkinter import *
from tkinter import Listbox, Tk, messagebox, ttk
import tkinter
#import loginlib
import mysql.connector


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        
        # ================================= Variables ======================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()


        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        # ================================= DataFrameLeft ======================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=860,height=350)

        lblMember=Label(DataFrameLeft,text="Member Type",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameLeft,text="PRN No:",bg="powder blue",font=("arial",12,"bold"),padx=2)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,text="ID No:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,text="Firstname:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,text="Lastname:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)


        lblAddress1=Label(DataFrameLeft,text="Address1:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,text="Address2:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,text="Post Code:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,text="Mobile:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        
        lblBookId=Label(DataFrameLeft,text="Book Id:",bg="powder blue",font=("arial",12,"bold"),padx=2)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,text="Book Title:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,text="Author Name:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)
        
        lblDateBorrowed=Label(DataFrameLeft,text="Date Borrowed:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,text="Date Due:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)
        
        lblDaysOnBook=Label(DataFrameLeft,text="Days On Book:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,text="Late Return Fine:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.latereturnfine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDate=Label(DataFrameLeft,text="Date Over Due:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateOverDate.grid(row=7,column=2,sticky=W)
        txtDateOverDate=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverDate.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,text="Actual Price:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)
        


        # ================================= DataFrameRight ======================================

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=870,y=5,width=580,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")


        listBooks=['Python Crash Course','Head-First Python','Learn Python the Hard Way','Python Programming','Introduction to Machine Learning with Python','Fluent Python','Grokking Algorithms','C++ Primer','Learn To Program With C++','Effective C++','Object Oriented Programming in C++ ','Let Us C','THE HITCHHIKER\'S GUIDE TO PYTHON','THE RECURSIVE BOOK OF RECURSION','Learning PHP, MySQL & JavaScript','Murach\'s MySQL','Head First Java ','Effective Java ',' Data Structures Using C and C++','Practical Malware Analysis','The Cyber Effect','Social Engineering']
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            
            if (x=="Python Crash Course"):
                self.bookid_var.set("BKID1001")
                self.booktitle_var.set("Python Crash Course")
                self.author_var.set("Eric Matthes")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.800")
            
            elif (x=="Head-First Python"):
                self.bookid_var.set("BKID1022")
                self.booktitle_var.set("Head-First Python")
                self.author_var.set("Paul Barry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.725")

            elif (x=="Learn Python the Hard Way"):
                self.bookid_var.set("BKID1035")
                self.booktitle_var.set("Learn Python the Hard Way")
                self.author_var.set("Zed Shaw")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.515")

            elif (x=="Python Programming"):
                self.bookid_var.set("BKID1039")
                self.booktitle_var.set("Python Programming")
                self.author_var.set("John M. Zelle")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.600")
            
            elif (x=="Introduction to Machine Learning with Python"):
                self.bookid_var.set("BKID1044")
                self.booktitle_var.set("Introduction to Machine Learning with Python")
                self.author_var.set("Sarah Guido")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.900")



            
                
                
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)


        # ================================= Buttons Frame ======================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=60)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnShowData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnShowData.grid(row=0,column=1)

        btnUpdateData=Button(Framebutton,command=self.update,text="Update ",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnUpdateData.grid(row=0,column=2)

        btnDeleteData=Button(Framebutton,command=self.delete,text="Delete ",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnDeleteData.grid(row=0,column=3)

        btnResetData=Button(Framebutton,command=self.reset,text="Reset ",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnResetData.grid(row=0,column=4)

        btnExitData=Button(Framebutton,command=self.iExit,text="Exit ",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnExitData.grid(row=0,column=5)

        # ================================= Information Frame ======================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=210)


        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","idno","firstname","lastname","address1","address2","postid","mobile",
                                                            "bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("idno",text="ID No.")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("idno",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
    
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="alwin",database="college")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.member_var.get(),
                                                                                                            self.prn_var.get(),
                                                                                                            self.id_var.get(),
                                                                                                            self.firstname_var.get(),
                                                                                                            self.lastname_var.get(),
                                                                                                            self.address1_var.get(),
                                                                                                            self.address2_var.get(),
                                                                                                            self.postcode_var.get(),
                                                                                                            self.mobile_var.get(),
                                                                                                            self.bookid_var.get(),
                                                                                                            self.booktitle_var.get(),
                                                                                                            self.author_var.get(),
                                                                                                            self.dateborrowed_var.get(),
                                                                                                            self.datedue_var.get(),
                                                                                                            self.daysonbook_var.get(),
                                                                                                            self.latereturnfine_var.get(),
                                                                                                            self.dateoverdue_var.get(),
                                                                                                            self.finalprice_var.get()
                                                                                                             ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="alwin",database="college")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,Firstname=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,BookID=%s,Booktitle=%s,Author=%s,Dateborrowed=%s,datedue=%s,daysofBook=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where PRN_NO=%s",(
                                                                                                            self.member_var.get(),
                                                                                                            self.id_var.get(),
                                                                                                            self.firstname_var.get(),
                                                                                                            self.lastname_var.get(),
                                                                                                            self.address1_var.get(),
                                                                                                            self.address2_var.get(),
                                                                                                            self.postcode_var.get(),
                                                                                                            self.mobile_var.get(),
                                                                                                            self.bookid_var.get(),
                                                                                                            self.booktitle_var.get(),
                                                                                                            self.author_var.get(),
                                                                                                            self.dateborrowed_var.get(),
                                                                                                            self.datedue_var.get(),
                                                                                                            self.daysonbook_var.get(),
                                                                                                            self.latereturnfine_var.get(),
                                                                                                            self.dateoverdue_var.get(),
                                                                                                            self.finalprice_var.get(),
                                                                                                            self.prn_var.get(),                                                                                                            
                                                                                                            ))
        
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Member has been Updated")


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="alwin",database="college")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if (len(rows)!=0):
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN No:\t\t"+ self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID No:\t\t"+ self.id_var.get()+"\n")
        self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"LastName:\t\t"+ self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author:\t\t"+ self.author_var.get()+"\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"DaysOnBook:\t\t"+ self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"LateReturnFine:\t\t"+ self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"DateOverDue:\t\t"+ self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"FinalPrice:\t\t"+ self.finalprice_var.get()+"\n")
        
    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="alwin",database="college")
            my_cursor=conn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")



if __name__=="__main__":
    root=Tk()   
    obj=LibraryManagementSystem(root)
    root.mainloop()
 

'''
root=Tk()
obj=LibraryManagementSystem(root)
root.mainloop()'''

