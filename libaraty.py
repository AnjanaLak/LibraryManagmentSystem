from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox

class Library:

    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='grey')

###########################FRAME################################################################

        mainFrame = Frame(self.root)
        mainFrame.grid()

        titleFrame = Frame(mainFrame, width=1350, padx=20, bd=20, relief=RIDGE)
        titleFrame.pack(side=TOP)

        self.lblTitle = Label(titleFrame, width=39, font=('arial', 40, 'bold'), text="Library Management Systems\t", padx=12, bg='blue')
        self.lblTitle.grid()

        buttonFrame = Frame(mainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        buttonFrame.pack(side=BOTTOM)

        frameDetail = Frame(mainFrame, bd=20, width=1350, height=100, padx=20, relief=RIDGE)
        frameDetail.pack(side=BOTTOM)

        dataFrame = Frame(mainFrame, bd=20, width=1300, height=400, padx=20, relief=RIDGE)
        dataFrame.pack(side=BOTTOM)

        dataFrameLeft = LabelFrame(dataFrame, bd=10,  width=800, height=300, padx=20, relief=RIDGE,
                                   font=('arial', 12, 'bold'), text="Library Mgt Info:")
        dataFrameLeft.pack(side=LEFT)

        dataFrameRight = LabelFrame(dataFrame, bd=10, width=450, height=300, padx=20, relief=RIDGE,
                                   font=('arial', 12, 'bold'), text="Book Details:")
        dataFrameRight.pack(side=RIGHT)

        #################### WIDGET ###############################################

        self.lblMemberType = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Member Type: ", padx=2, pady=2)
        self.lblMemberType.grid(row=0, column=0, sticky=W) ### code to create a label

        self.cboMemberType = ttk.Combobox(dataFrameLeft, state='readonly', font=('arial', 12, 'bold'), width=23)
        self.cboMemberType['value'] = ('', 'student', 'Lecturer', 'Admin Staff')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0, column=1) ### code for creating a combobox

        self.lblBookID = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Book ID: ", padx=2, pady=2)
        self.lblBookID.grid(row=0, column=2, sticky=W)
        ### code for entry
        self.textBookID = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.textBookID.grid(row=0, column=3)

        self.lblRef = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Reference No: ", padx=2, pady=2)
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtRef.grid(row=1, column=1)

        self.lblBookTitle = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Book Title: ", padx=2, pady=2)
        self.lblBookTitle.grid(row=1, column=2, sticky=W)
        self.txtRef = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtRef.grid(row=1, column=3)

        self.lblBookTitle = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Book Title: ", padx=2, pady=2)
        self.lblBookTitle.grid(row=1, column=2, sticky=W)
        self.txtRef = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtRef.grid(row=1, column=3)

        self.lblTitle = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Member Type: ", padx=2, pady=2)
        self.lblTitle.grid(row=2, column=0, sticky=W)
        self.cboTitle = ttk.Combobox(dataFrameLeft, state='readonly', font=('arial', 12, 'bold'), width=23)
        self.cboTitle['value'] = ('', 'Mr.', 'Mrs.', 'Miss.')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2, column=1)

        self.lblAuthor = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Author: ", padx=2, pady=2)
        self.lblAuthor.grid(row=2, column=2, sticky=W)
        self.txtAuthor = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtAuthor.grid(row=2, column=3)

        self.lblFirstName = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="First Name: ", padx=2, pady=2)
        self.lblFirstName.grid(row=3, column=0, sticky=W)
        self.txtFirstName = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtFirstName.grid(row=3, column=1)

        self.lblDateBorrowed = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Date Borrowed: ", padx=2, pady=2)
        self.lblDateBorrowed.grid(row=3, column=2, sticky=W)
        self.txtDateBorrowed = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtDateBorrowed.grid(row=3, column=3)

        self.lblSurname = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Surname: ", padx=2, pady=2)
        self.lblSurname.grid(row=4, column=0, sticky=W)
        self.txtSurname = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtSurname.grid(row=4, column=1)

        self.lblDateDue = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Due Date: ", padx=2, pady=2)
        self.lblDateDue.grid(row=4, column=2, sticky=W)
        self.txtDateDue = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtDateDue.grid(row=4, column=3)

        self.lblAddress1 = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Address 1: ", padx=2, pady=2)
        self.lblAddress1.grid(row=5, column=0, sticky=W)
        self.txtAddress1 = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtAddress1.grid(row=5, column=1)

        self.lblDaysOnLoan = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Days on Loan: ", padx=2, pady=2)
        self.lblDaysOnLoan.grid(row=5, column=2, sticky=W)
        self.txtDaysOnLoan = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtDaysOnLoan.grid(row=5, column=3)

        self.lblAddress2 = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Address 2: ", padx=2, pady=2)
        self.lblAddress2.grid(row=6, column=0, sticky=W)
        self.txtAddress2 = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtAddress2.grid(row=6, column=1)

        self.lblLateReturnFine = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Return Fine: ", padx=2, pady=2)
        self.lblLateReturnFine.grid(row=6, column=2, sticky=W)
        self.txtLateReturnFine = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtLateReturnFine.grid(row=6, column=3)

        self.lblPostCode = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Post Code: ", padx=2, pady=2)
        self.lblPostCode.grid(row=7, column=0, sticky=W)
        self.txtPostCode = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtPostCode.grid(row=7, column=1)

        self.lblDateOverdue = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Date Overdue: ", padx=2, pady=2)
        self.lblDateOverdue.grid(row=7, column=2, sticky=W)
        self.txtDateOverdue = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtDateOverdue.grid(row=7, column=3)

        self.lblMobileNo = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Mobile No: ", padx=2, pady=2)
        self.lblMobileNo.grid(row=8, column=0, sticky=W)
        self.txtMobileNo = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtMobileNo.grid(row=8, column=1)

        self.lblSellingPrice = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Selling Price: ", padx=2, pady=2)
        self.lblSellingPrice.grid(row=8, column=2, sticky=W)
        self.txtSellingPrice = Entry(dataFrameLeft, font=('arial', 12, 'bold'), width=25)
        self.txtSellingPrice.grid(row=8, column=3)


















if __name__ == '__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()


