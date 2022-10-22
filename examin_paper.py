from tkinter import *
from db import *
import question_make
# import sign_up
# import sign_in


class ExaminPaper(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        sfram = Frame(self)
        sfram.grid(row=0, column=0, sticky='new')
        rownum = 0
        # ------------------------------------- getting the exam code -------------------------------------
        ecode = StringVar()
        examcode = Label(sfram, text='Give specific EXAM_CODE: ')
        examcode.grid(row=rownum, column=0)
        codeentry = Entry(sfram, textvariable=ecode)
        codeentry.grid(row=rownum, column=1)
        rownum += 1
        # ------------------------------- Get paper code to get a paper -----------------------------------
        pcode = IntVar()
        pcodelabel = Label(sfram, text='Give a specific paper code to examine')
        pcodelabel.grid(row=rownum, column=0)
        pcodeentry = Entry(sfram, textvariable=pcode)
        pcodeentry.grid(row=rownum, column=1)
        rownum += 1

        btn = Button(sfram, text='Get Paper')
        btn.grid(row=rownum, column=0, sticky='w')
        btn.bind('<Button-1>', lambda e: self.code_check(str(ecode.get()), int(pcode.get())))
        backbutton = Button(self, text='Make Question', width=10)
        backbutton.grid(row=rownum+1, column=0, sticky='w')
        backbutton.bind('<Button-1>', lambda e: controller.showframe(question_make.MakeQuestion))
        rownum += 1

    # ------------------------------------- Getting code checked ------------------------------------
    # ------------------------------------- Getting code checked ------------------------------------
    def code_check(self, code, pcode):

        if code_existence_check_t(code) == 'true':
            self.getpaper(code, pcode)
        else:
            pfram = Frame(self)
            pfram.grid(row=1, column=0)
            errorlabel = Label(pfram, text='------------- This EXAM CODE is not valid for you -------------')
            errorlabel.grid(row=0, column=0)

    # ------------------------------------- Getting paper for those code ------------------------------------
    # ------------------------------------- Getting paper for those code ------------------------------------
    def getpaper(self, ecode, pcode):
        pfram = Frame(self)
        pfram.grid(row=1, column=0, sticky='esw')
        rownum = 0
        wls = gettingwrittenanswer(ecode, pcode)
        mls = gettingmultipleanswer(ecode, pcode)
        tfls = gettingtruefalseanswer(ecode, pcode)

        written = []*len(wls)
        multi = []*len(mls)
        tf = []*len(tfls)

        wmark = []*len(wls)
        mulmark = []*len(mls)
        tfmark = []*len(tfls)

        for i in range(len(wls)):
            written[i] = Text(pfram, width=40, height=30)
            written[i].grid(row=rownum, column=0, sticky='nsew')
            written[i].delete('1.0', "END")
            written[i].insert("END", wls[i])

            wmark[i] = StringVar()
            mark = Entry(pfram, width=10, textvariable=wmark[i])
            mark.grid(row=rownum, column=1, sticky='e')
            rownum += 1

        for i in range(len(mls)):
            multi[i] = Text(pfram, width=5, height=5)
            multi[i].grid(row=rownum, column=0, sticky='nsew')
            multi[i].delete('1.0', "END")
            multi[i].insert("END", mls[i])

            mulmark[i] = StringVar()
            mark = Entry(pfram, width=10, textvariable=mulmark[i])
            mark.grid(row=rownum, column=1, sticky='e')
            rownum += 1

        for i in range(len(tfls)):
            tf[i] = Text(pfram, width=5, height=5)
            tf[i].grid(row=rownum, column=0, sticky='nsew')
            tf[i].delete('1.0', "END")
            tf[i].insert("END", tfls[i])

            tfmark[i] = StringVar()
            mark = Entry(pfram, width=10, textvariable=tfmark[i])
            mark.grid(row=rownum, column=1, sticky='e')
            rownum += 1

        subbtn = Button(pfram, text='submit')
        subbtn.grid(row=rownum, column=0)
        subbtn.bind('<Button-1>', lambda e: self.saving(pcode, ecode, wls, mls, tfls, wmark, mulmark, tfmark))  # ---- Saving the marks

    def saving(self, pcode, ecode, wls, mls, tfls, wmark, mulmark, tfmark):
        for i in range(len(wls)):
            savingwmark(pcode, ecode, wmark[i], wls[i])
        for i in range(len(mls)):
            savingmulmark(pcode, ecode, mulmark[i], mls[i])
        for i in range(len(tfls)):
            savingtfmark(pcode, ecode, tfmark[i], tfls[i])

