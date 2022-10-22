from tkinter import *
from speech_recognition import *
#from exampaper import ExamPaper
# import exampaper
#import homepage
#from db import *
#import pyttsx3



class AttendExam(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        atframe = Frame(self)
        atframe.grid(row=0, column=0)

        self.bind('<Button-3>', lambda e: self.speekit(namedata, 'Name'))

        namedata = StringVar()
        regdata = IntVar()
        pentry = IntVar()
        ecdata = StringVar()

        self.entrylist = [namedata, regdata, pentry, ecdata]
        self.entrydata = ['name', 'Registration No', 'Paper Code', 'Exam Code']
        nlabel = Label(atframe, text='Name')
        nlabel.grid(row=0, column=0)
        nentry = Entry(atframe, width=40, textvariable=namedata)
        nentry.grid(row=0, column=1)
        nentry.bind("<Return>", lambda i: self.speekit(regdata, 'Registration No.'))

        reglabel = Label(atframe, text='Reg No.')
        reglabel.grid(row=1, column=0)
        regentry = Entry(atframe, width=40, textvariable=regdata)
        regentry.grid(row=1, column=1)
        regentry.bind("<Return>", lambda i: self.speekit(pentry, 'Paper Code'))

        paplabel = Label(atframe, text='Paper Code')
        paplabel.grid(row=2, column=0)
        papentry = Entry(atframe, width=40, textvariable=pentry)
        papentry.grid(row=2, column=1)
        papentry.bind("<Return>", lambda i: self.speekit(ecdata, 'Exam Code'))

        eclabel = Label(atframe, text='Exam Code')
        eclabel.grid(row=3, column=0)
        ecentry = Entry(atframe, width=40, textvariable=ecdata)
        ecentry.grid(row=3, column=1)
        ecentry.bind("<Return>", lambda i: self.check(str(ecdata.get()), int(pentry.get()), str(namedata.get()), str(regdata.get())))
        # self.c = ecdata.get()
        # self.p = pentry.get()
        # self.n = namedata.get()
        # self.r = regdata.get()
        backbutton = Button(atframe, text='Back', width=10)
        backbutton.grid(row=4, column=1, sticky='e')
        backbutton.bind('<Button-1>', lambda e: controller.showframe(homepage.HomePage))

    def check(self, code, pcode, name, reg):
        mframe = Frame(self)
        mframe.grid(row=1, column=0)
        if code_existence_check_std(code, name, reg) == 'true' and code != '' and name != '' and reg != '':
            errormessage = Label(mframe, text='Wrong input data here...........')
            errormessage.grid(row=1, column=0)
        else:
            subbutton = Button(mframe, text='Submit')
            subbutton.grid(row=0, column=0,)
            subbutton.bind('<Button-1>', lambda i: self.anspaper(code, pcode, name, reg))

    def anspaper(self, code, pcode, name, reg):
        lframe = Frame(self)
        lframe.grid(row=2, column=0)
        # at = attend_exam.AttendExam(parent, controller)
        self.answer = ' '
        rownum = 0
        q = Label(lframe, text='------------ You will Get Answer Paper Code and Exam Code if valid -------------')
        q.grid(row=rownum, column=0, columnspan=2)
        rownum += 1
        # ------------------------------------------ Written question -----------------------------------
        # ------------------------------------------ Written question -----------------------------------
        writtenls = getwrittenquestion(code)
        wq = [''] * len(writtenls)
        atext = [''] * len(writtenls)
        for i in range(len(writtenls)):
            print(i)
            wq[i] = StringVar()
            qlabel = Label(lframe, textvariable=wq[i])
            qlabel.grid(row=rownum, column=0, sticky='w')
            wq[i].set('# ' + str(writtenls[i]))
            rownum += 1
            atext[i] = Text(lframe, width=35, height=5)
            atext[i].grid(row=rownum, column=0, padx=8, pady=5)
            rownum += 1
        # ------------------------------------------ true/false question -----------------------------------
        # ------------------------------------------ true/false question -----------------------------------
        tfls = gettruefalsequestion(code)
        tfq = [''] * len(tfls)
        tfans = [''] * len(tfls)
        for i in range(len(tfls)):
            tfq[i] = StringVar()
            tfans[i] = StringVar()
            qlabel = Label(lframe, textvariable=tfq[i])
            qlabel.grid(row=rownum, column=0, sticky='w')
            tfq[i].set('# ' + str(tfls[i]))
            rownum += 1
            tfen = Entry(lframe, width=5, textvariable=tfans[i])
            tfen.grid(row=rownum, column=0, padx=8, pady=5)
            rownum += 1
        # ans = StringVar(value=self.answer)
        # atext.bind('<Return>', lambda e: qaudio.nextquestion(question2.get(), a1.get(), a2.get(), a3.get(), a4.get()))
        # atext.focus()
        # atext.focus_set()

        # ------------------------------------------ Multiple question -----------------------------------
        # ------------------------------------------ Multiple question -----------------------------------
        multiplels = getmultiplequestion(code)
        mulq = [''] * 4
        mulans = [''] * len(multiplels)
        for i in range(len(multiplels)):
            mulans[i] = StringVar()
            for j in range(len(multiplels[i])):
                if j == 0:
                    mulq[j] = StringVar()
                    q2label = Label(lframe, textvariable=mulq[j])
                    q2label.grid(row=rownum, column=0, pady=5)
                    mulq[j].set('# '+str(multiplels[i][j]))
                    rownum += 1
                else:
                    mulq[j] = StringVar()
                    a = Label(lframe, textvariable=mulq[j])
                    a.grid(row=rownum, column=0, sticky='w')
                    mulq[j].set(str(multiplels[i][j]))
                    rownum += 1
            mans = Entry(lframe, textvariable=mulans[i])
            mans.grid(row=rownum, column=0, sticky='w')
            rownum += 1

        subbtn = Button(lframe, text='Submit')
        subbtn.grid(row=rownum, column=0)
        subbtn.bind('<Button-1>', lambda e: [savingwans(pcode, code, name, reg, atext),
                                             savingmulans(pcode, code, name, reg, mulans),
                                             savingtfans(pcode, code, name, reg, tfans)])

    def speekit(self, ent, text):

        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

        self.command_writ(ent)

    def speek(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def command_writ(self, ent):
        print('1111111111')
        r = Recognizer()
        with Microphone(device_index=1) as source:
            r.energy_threshold = 8000
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Speak:")
            audio = r.listen(source)
            print('111111111')

        try:
            print("You said '" + r.recognize_sphinx(audio) + "';")
            inp = str(r.recognize_sphinx(audio))
            # tem = inp
            if inp.endswith('enter', 0, len(inp)):
                for i in self.entrylist:
                    if self.entrylist[i] == ent and i+1 <len(self.entrylist):
                        self.speekit(self.entrylist[i+1], self.entrydata[i+1])
            # elif inp.endswith('repeat', 0, len(inp)):
            #     for i in self.entrylist:
            #         if self.entrylist[i] == ent:
            #             self.speekit(self.entrylist[i], self.entrydata[i])
            else:
                self.speek(inp)
                ent.set(inp)
                self.command_writ(ent)
        except UnknownValueError:
            print("Could not understand audio")
            self.command_writ(ent)
        except RequestError as e:
            print("Could not request results; {0}".format(e))

    # def printer(self,val):
    #     print(val)
        # for i in range(len(val)):
        #     print('wwww '+str(val[i]))
        # backbutton = Button(self, text='Back', width=10)
        # backbutton.grid(row=rownum, column=1, sticky='w')
        # backbutton.bind('<Button-1>', lambda e: controller.showframe(attend_exam.AttendExam))
    # def getcode(self):
    #     return self.c
    #
    # def getpcode(self):
    #     return self.p