from tkinter import *
from db import *
import homepage
import pyttsx3
from speech_recognition import *


class ExamResult(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        sfram = Frame(self)
        sfram.grid(row=0, column=0)
        nentry = StringVar()
        identry = IntVar()
        ecodeentry = StringVar()
        self.bind('<Button-1>', lambda e: self.speekthese(nentry, 'your name', controller))

        self.entdata = ['your id', 'your exam code']
        self.ententry = [identry, ecodeentry]

        namelabel = Label(sfram, text="Your name")
        namelabel.grid(row=1, column=0)
        nameentry = Entry(sfram, textvariable=nentry)
        nameentry.grid(row=1, column=1)

        iddlabel = Label(sfram, text="Your ID")
        iddlabel.grid(row=2, column=0)
        nameentry = Entry(sfram, textvariable=identry)
        nameentry.grid(row=2, column=1)

        examlabel = Label(sfram, text="Your Exam Code")
        examlabel.grid(row=3, column=0)
        nameentry = Entry(sfram, textvariable=ecodeentry)
        nameentry.grid(row=3, column=1)

        subbtn = Button(sfram, text='Submit')
        subbtn.grid(row=4, column=0)
        subbtn.bind('<Button-1>', lambda e: self.showresult(result(str(nentry.get()), int(identry.get()), str(ecodeentry.get()))))
        backbutton = Button(sfram, text='Back', width=10)
        backbutton.grid(row=4, column=1, sticky='e')
        backbutton.bind('<Button-1>', lambda e: controller.showframe(homepage.HomePage))

    def showresult(self, res):
        reslabel = Label(self, text='Your mark is '+str(res))
        reslabel.grid(row=6, column=0, columnspan=2, padx=10, ipadx=10, pady=5)

    def speekthese(self, ent, text, controller):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        self.command_writ(ent, controller)

    def command_writ(self, ent, controller):

        print('1111111111')
        r = Recognizer()
        with Microphone(device_index=1) as source:
            r.energy_threshold = 2000
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Speak:")
            aud = r.listen(source)
            print('111111111')

        try:
            print("You said '" + r.recognize_google(aud) + "';")
            inp = str(r.recognize_google(aud))
            if inp.endswith('enter this', 0, len(inp)):

                self.speekthese(self.ententry[i], self.entdata[i], controller)
                i += 1
            else:
                ent.set(aud)
                self.speekthese(ent, inp, controller)
        except UnknownValueError:
            print("Could not understand audio")
            self.command_writ(ent, controller)
        except RequestError as e:
            print("Could not request results; {0}".format(e))