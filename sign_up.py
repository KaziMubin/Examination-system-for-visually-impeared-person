from tkinter import *
import moderator
# import question_make
# import examin_paper
import homepage
from db import teacher_input, usernamecheck


class SignUp(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.con = controller
        name = StringVar()
        idd = IntVar()
        username = StringVar()
        pas = StringVar()
        cpas = StringVar()

        # ----------------------- Teacher's sign up inputs -----------------------------------------------
        nlabel = Label(self, text='Name')  # ------------name------------------------------
        nlabel.grid(row=0, column=0)
        nentry = Entry(self, width=40, textvariable=name)
        nentry.grid(row=1, column=0, columnspan=2)

        idlabel = Label(self, text='Id')  # ------------Id------------------------------
        idlabel.grid(row=2, column=0)
        identry = Entry(self, width=40, textvariable=idd)
        identry.grid(row=3, column=0, columnspan=2)

        ulabel = Label(self, text='Username')  # ------------username------------------------------
        ulabel.grid(row=4, column=0)
        uentry = Entry(self, width=40, textvariable=username)
        uentry.grid(row=5, column=0, columnspan=2)

        plabel = Label(self, text='Password')  # ------------Password------------------------------
        plabel.grid(row=6, column=0)
        pentry = Entry(self, width=40, textvariable=pas)
        pentry.grid(row=7, column=0, columnspan=2)

        cplabel = Label(self, text='Confirm Password')  # ------------confirm password------------------------------
        cplabel.grid(row=8, column=0)
        cpentry = Entry(self, width=40, textvariable=cpas)
        cpentry.grid(row=9, column=0, columnspan=2)
        cpentry.bind('<Return>', lambda e: [self.validitycheck(str(pas.get()), str(cpas.get()), str(username.get()),
                                                               str(name.get()), str(idd.get()), subbutton, controller)])
        subbutton = Button(self, text='Submit', width=10)
        subbutton.grid(row=10, column=0, sticky='w')

        backbutton = Button(self, text='Back', width=10)
        backbutton.grid(row=10, column=1, sticky='e')
        backbutton.bind('<Button-1>', lambda e: controller.showframe(homepage.HomePage))

    def validitycheck(self, pas, cpas, username, name, idd, subbutton, controller):
        if pas == cpas and usernamecheck(username) == 'false' and pas != '' and username != '':

            subbutton.bind('<Button-1>', lambda e: [controller.showframe(moderator.Moderator),
                           teacher_input(name, idd, username, pas)])
        else:
            if pas != cpas:
                error = Label(self, text="Password and Confirmation Password doesn't match!!!")
                error.grid(row=11, column=0, sticky='we')
            elif username == '' or pas == '':
                error = Label(self, text="One or more blank field!!!")
                error.grid(row=11, column=0, sticky='we')
            else:
                error = Label(self, text="Username is taken/ No username input!!!")
                error.grid(row=11, column=0, sticky='we')

