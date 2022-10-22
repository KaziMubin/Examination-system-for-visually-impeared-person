from tkinter import *
import moderator
# import question_make
# from examin_paper import ExaminPaper
import homepage
# import sign_up
from db import login


class SignIn(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        uent = StringVar()
        pasent = StringVar()

        ulabel = Label(self, text='Username')  # -----------------------------username---------------------------------
        ulabel.grid(row=0, column=0, columnspan=2)
        uentry = Entry(self, width=30, textvariable=uent)
        uentry.grid(row=1, column=0, columnspan=2)
        plabel = Label(self, text='Password')  # -----------------------------password---------------------------------
        plabel.grid(row=3, column=0, columnspan=2)
        pentry = Entry(self, width=30, textvariable=pasent)
        pentry.grid(row=4, column=0, columnspan=2)

        blogin = Button(self, text='Log In', width=10)
        blogin.grid(row=5, column=0)
        blogin.bind('<Button-1>', lambda e: self.log(uent.get(), pasent.get(), controller))
        backbutton = Button(self, text='Back', width=10)
        backbutton.grid(row=5, column=1, sticky='e')
        backbutton.bind('<Button-1>', lambda e: controller.showframe(homepage.HomePage))

    def log(self, user, pas, controller):
        if login(str(user), str(pas)) == 'true' and str(user) != '' and str(pas) != '':
            controller.showframe(moderator.Moderator)
        else:
            ulabel = Label(self, text="Username Password doesn't match")  # -------- Login Error Message --------------
            ulabel.grid(row=6, column=0)

    # def current(self):
    #     print(self.u)
    #     return self.u

# ExaminPaper.ecurrent_user(uent.get())