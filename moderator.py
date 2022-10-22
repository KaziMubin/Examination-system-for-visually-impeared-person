from tkinter import *
import examin_paper
import question_make


class Moderator(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        examinlabel = Label(self, text='Press to examin answer paper.')
        examinlabel.grid(row=0, column=0)
        examinbutton = Button(self, text='Examin Paper', width=10)
        examinbutton.grid(row=0, column=1)
        examinbutton.bind('<Button-1>', lambda e: controller.showframe(examin_paper.ExaminPaper))

        createlabel = Label(self, text='Press to create a new question')
        createlabel.grid(row=1, column=0, pady=5)
        createbutton = Button(self, text='Create Question', width=10)
        createbutton.grid(row=1, column=1, pady=5)
        createbutton.bind('<Button-1>', lambda e: controller.showframe(question_make.MakeQuestion))
