from tkinter import *
from homepage import HomePage
from sign_in import SignIn
from sign_up import SignUp
import attend_exam
import examresult
from moderator import Moderator
from examin_paper import ExaminPaper
from question_make import MakeQuestion
#import conversion


class Culpture(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        f1 = Frame(self)
        f1.grid(row=0, column=0, sticky='nsew')
        f1.grid_columnconfigure(0, weight=1)
        f1.grid_rowconfigure(0, weight=1)
        self.frames = {}
        for F in (HomePage, SignIn, SignUp, examresult.ExamResult, attend_exam.AttendExam, MakeQuestion, ExaminPaper, Moderator):  #  ExamPaper,
            frame = F(f1, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

            # frame.grid_columnconfigure(1, weight=1)
            # frame.grid_rowconfigure(1, weight=1)

        self.showframe(HomePage)

    def showframe(self, framename):
        currentframe = self.frames[framename]
        currentframe.tkraise()


app = Culpture()

w = 350
h = 500
x = 200
y = 100
app.geometry('%dx%d+%d+%d' % (w, h, x, y))
app.title('Examination System for Blind Persons')

app.mainloop()
