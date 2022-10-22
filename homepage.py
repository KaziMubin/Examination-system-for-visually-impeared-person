from tkinter import *
from sign_in import SignIn
from sign_up import SignUp
import attend_exam
from examresult import ExamResult
import pyttsx3
from speech_recognition import *


class HomePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        btn = IntVar()
        # btn2 = StringVar()
        # tchecker.set(False)
        # schecker.set(False)

        checkteacher = Radiobutton(self, text='Teacher', value=1, variable=btn)
        checkteacher.bind('<Button-1>', lambda e: self.showteacher(controller) if btn.get() != 1 else
        self.showstudent(controller))
        checkteacher.grid(row=0, column=0)

        checkstudent = Radiobutton(self, text='Student', value=2, variable=btn)
        checkstudent.bind('<Button-1>', lambda e: self.showstudent(controller) if btn.get() != 2 else
        self.showteacher(controller))
        checkstudent.grid(row=1, column=0)

    def showteacher(self, controller):
        sframe = Frame(self)
        sframe.config(borderwidth=2, height=200, width=300)
        sframe.grid(row=4, column=0, sticky='nsew')
        bsignin = Button(sframe, text='Sign In', command=lambda: controller.showframe(SignIn), width=10)
        bsignin.grid()
        bsignup = Button(sframe, text='Sign Up', command=lambda: controller.showframe(SignUp), width=10)
        bsignup.grid()

    def showstudent(self, controller):
        eframe = Frame(self)
        eframe.grid(row=4, column=0, sticky='nsew')
        eframe.config(borderwidth=2, height=200, width=300)
        batnexam = Button(eframe, text='Participate', command=lambda: controller.showframe(attend_exam.AttendExam), width=10)
        batnexam.grid(row=0, column=0)
        bresult = Button(eframe, text='Result', command=lambda: controller.showframe(ExamResult), width=10)
        bresult.grid(row=1, column=0)
        self.speekthese('participant', 'result', controller)

    def speekthese(self, text, text2, controller):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.say(text2)
        engine.runAndWait()
        self.command_writ(controller)

    def command_writ(self, controller):

        print('1111111111')
        r = Recognizer()
        with Microphone(device_index=1) as source:
            r.energy_threshold = 2000
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Speak:")
            audio = r.listen(source)
            print('111111111')

        try:
            print("You said '" + r.recognize_google(audio) + "';")
            inp = str(r.recognize_google(audio))
            if inp.endswith('participate', 0, len(inp)):
                controller.showframe(attend_exam.AttendExam)
            elif inp.endswith('result', 0, len(inp)):
                controller.showframe(ExamResult)
            else:
                self.command_writ(controller)
        except UnknownValueError:
            print("Could not understand audio")
            self.command_writ(controller)
        except RequestError as e:
            print("Could not request results; {0}".format(e))

        # data = read.write()
        # b1 = 'attend exam'
        # b2 = 'result'
        # length = len(data)
        # if len(b1) == length and b1 == data:
        #     controller.showframe(AttendExam)
        # elif len(b2) == length and b2 == data:
        #     controller.showframe(ExamResult)
        # else:
        #     read.declareerror('Invalid speech')
        #     read.write()
        #
        # print(data)
