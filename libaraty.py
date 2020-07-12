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

        






if __name__ == '__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()


