from tkinter import *
from db import *
import examin_paper
import sign_up
import sign_in


class MakeQuestion(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        mframe = Frame(self)
        mframe.grid(row=0, column=0, sticky='nwe')
        rownum = 0
        w_questionentry = IntVar()
        mul_questionentry = IntVar()
        tf_questionentry = IntVar()
        #  ------------------------------------------------------------------------------------------------------ #
        #  ------------------------ Exam Code and Title ----------------------------- #
        #  ------------------------------------------------------------------------------------------------------ #
        codeentry = StringVar()
        exam_code = Label(mframe, text='Exam Code')
        exam_code.grid(row=rownum, column=0)
        rownum += 1
        examcode_entry = Entry(mframe, textvariable=codeentry)
        examcode_entry.grid(row=rownum, column=0)
        rownum += 1

        qlabel = Label(mframe, text='----------------- Give number of question ----------------')
        qlabel.grid(row=rownum, column=0, columnspan=2, padx=6, pady=3)
        rownum += 1
        #  ------------------------------------------------------------------------------------------------------ #
        #  --------------------Give Question (Written, True/False, Choose the Right answer)---------------------- #
        #  ------------------------------------------------------------------------------------------------------ #

        #  --------------------------------- Written question part ---------------------------------------------- #
        num_of_w_question = Label(mframe, text='Number of Written question')
        num_of_w_question.grid(row=rownum, column=0)
        number_of_w_questionentry = Entry(mframe, textvariable=w_questionentry)  # ----------------- Written question
        number_of_w_questionentry.grid(row=rownum, column=1)
        rownum += 1

        #  --------------------------------- Multiple question part ---------------------------------------------- #
        num_of_multiple_question = Label(mframe, text='Number of Written question')  # ----------- Multiple question
        num_of_multiple_question.grid(row=rownum, column=0)
        number_of_multiple_questionentry = Entry(mframe, textvariable=mul_questionentry)
        number_of_multiple_questionentry.grid(row=rownum, column=1)
        rownum += 1

        #  --------------------------------- True/False question part ---------------------------------------------- #
        num_of_tf_question = Label(mframe, text='Number of True/False question')
        num_of_tf_question.grid(row=rownum, column=0)
        number_of_tf_questionentry = Entry(mframe, textvariable=tf_questionentry)  # ----------- true_false question
        number_of_tf_questionentry.grid(row=rownum, column=1)
        rownum += 1

        submit = Button(mframe, text='Make')
        submit.grid(row=rownum, column=0)
        submit.bind('<Button-1>', lambda e: [self.ccheck(codeentry.get(), w_questionentry.get(),
                                             mul_questionentry.get(), tf_questionentry.get())])
        backbutton = Button(mframe, text='Examin Paper', width=10)
        backbutton.grid(row=rownum+1, column=0)
        backbutton.bind('<Button-1>', lambda e: controller.showframe(examin_paper.ExaminPaper))

    def ccheck(self, code, number_of_w, number_of_multiple, number_of_tf):

        if code_existence_check_t(code) == 'true':
            fframe = Frame(self)
            fframe.grid(row=1, column=0, sticky='wse')
            rownum1 = 0
            w = Label(fframe, text='------------------------ This Exam code already exist --------------------------')
            w.grid(row=rownum1, column=0)
            rownum1 += 1
        else:
            self.questions(code, number_of_w, number_of_multiple, number_of_tf)

    def questions(self, code, numofwquestion, numofmulquestion, numoftfquestion):
        sframe = Frame(self)
        sframe.grid(row=1, column=0, sticky='wse')
        wqs = ['wr'] * numofwquestion
        tfqs = [''] * numoftfquestion
        mulqs = [''] * numofmulquestion
        option1 = [''] * numofmulquestion
        option2 = [''] * numofmulquestion
        option3 = [''] * numofmulquestion
        rownum2 = 0

        w = Label(sframe, text='------------------------ Give Written Question --------------------------')
        w.grid(row=rownum2, column=0, columnspan=2, padx=6, pady=3)
        rownum2 += 1
        for i in range(numofwquestion):
            wqs[i] = StringVar()
            wquestion = Label(sframe, text='Question ' + str(i) + ') ')
            wquestion.grid(row=rownum2, column=0, columnspan=1, padx=0, pady=3)
            wquestionentry = Entry(sframe, textvariable=wqs[i])
            wquestionentry.grid(row=rownum2, column=1, columnspan=1, padx=2, pady=0)
            rownum2 += 1

        mul = Label(sframe, text='--------------------- Give Multiple Choice Question ----------------------------')
        mul.grid(row=rownum2, column=0, columnspan=2, padx=6, pady=3)
        rownum2 += 1
        for i in range(numofmulquestion):
            mulqs[i] = StringVar()
            option1[i] = StringVar()
            option2[i] = StringVar()
            option3[i] = StringVar()
            multipleqlabel = Label(sframe, text='Question ' + str(i) + ') ')
            multipleqlabel.grid(row=rownum2, column=0)
            multipleqentry = Entry(sframe, textvariable=mulqs[i])
            multipleqentry.grid(row=rownum2, column=1)
            rownum2 += 1

            oplabel = Label(sframe, text='Give your options')
            oplabel.grid(row=rownum2, column=0)
            rownum2 += 1
            multipleopentry1 = Entry(sframe, textvariable=option1[i])
            multipleopentry2 = Entry(sframe, textvariable=option2[i])
            multipleopentry3 = Entry(sframe, textvariable=option3[i])
            multipleopentry1.grid(row=rownum2, column=1)
            rownum2 += 1
            multipleopentry2.grid(row=rownum2, column=1)
            rownum2 += 1
            multipleopentry3.grid(row=rownum2, column=1)
            rownum2 += 1

        tf = Label(sframe, text='--------------------- Give True/False Question ----------------------------')
        tf.grid(row=rownum2, column=0, columnspan=2, padx=6, pady=3)
        rownum2 += 1
        for i in range(numoftfquestion):
            tfqs[i] = StringVar()
            tfquestion = Label(sframe, width=10, text='Question ' + str(i) + ') ')
            tfquestion.grid(row=rownum2, column=0, columnspan=1, padx=0, pady=0)
            tfquestionentry = Entry(sframe, textvariable=tfqs[i])
            tfquestionentry.grid(row=rownum2, column=1, columnspan=1, padx=2, pady=0)
            rownum2 += 1

        submit = Button(sframe, text='Upload')
        submit.grid(row=rownum2, column=0)
        submit.bind('<Button-1>',
                    lambda e: self.savingqs(code, numofwquestion, numofmulquestion, numoftfquestion,
                                             wqs, mulqs, tfqs, option3, option2, option1))

    def savingqs(self, code, numofwquestion, numofmulquestion, numoftfquestion,
                  wqs, mulqs, tfqs, option3, option2, option1):
        written_qs_list = [] * numofwquestion
        multiple_qs_list = [''] * numofmulquestion
        truefalse_qs_list = [] * numoftfquestion

        for i in range(numofwquestion):
            written_qs_list.append(wqs[i].get())
            written_q(code, wqs[i].get())

        for i in range(numofmulquestion):
            multiple_qs_list[i] = [mulqs[i].get(), option1[i].get(), option2[i].get(),
                                   option3[i].get()]
            multiple_q(code, mulqs[i].get(), option1[i].get(), option2[i].get(), option3[i].get())

        for i in range(numoftfquestion):
            truefalse_qs_list.append(tfqs[i].get())
            truefalse_q(code, tfqs[i].get())

        print(written_qs_list)
        print(multiple_qs_list)
        print(truefalse_qs_list)



