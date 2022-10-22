# import time
import pyttsx3
from speech_recognition import *


# class Conversion:
#
#     def speekthese(self, text, text2):
#         engine = pyttsx3.init()
#         engine.say(text)
#         engine.runAndWait()
#         engine.say(text2)
#         engine.runAndWait()
#         self.command_writ()
#
#     def command_writ(self):
#
#         print('1111111111')
#         r = Recognizer()
#         with Microphone(device_index=1) as source:
#             r.energy_threshold = 8000
#             r.adjust_for_ambient_noise(source, duration=0.5)
#             print("Speak:")
#             audio = r.listen(source)
#             print('111111111')
#
#         try:
#             print("You said '" + r.recognize_sphinx(audio) + "';")
#             inp = str(r.recognize_sphinx(audio))
#             if inp.endswith('one', 0, len(inp)):
#                 print('1111111')
#             elif inp.endswith('four', 0, len(inp)):
#                 print('4444444')
#             else:
#                 self.command_writ()
#         except UnknownValueError:
#             print("Could not understand audio")
#             self.command_writ()
#         except RequestError as e:
#             print("Could not request results; {0}".format(e))
#
#     def speekit(self, nentry, text):
#
#         engine = pyttsx3.init()
#         engine.say(text)
#         engine.runAndWait()
#
#         nentry.focus()
#
#     def next(self, te):
#         import attend_exam
#         import home
#         import question_make
#         if te == 'one':
#             home.Culpture.showframe(attend_exam.AttendExam)
#         elif te == 'four':
#             home.Culpture.showframe(question_make.MakeQuestion)

def command_writ():

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
        inp = str(r.recognize_sphinx(audio))
        if inp.endswith('one', 0, len(inp)):
            print('1111111')
        elif inp.endswith('four', 0, len(inp)):
            print('4444444')
        else:
            command_writ()
    except UnknownValueError:
        print("Could not understand audio")
        command_writ()
    except RequestError as e:
        print("Could not request results; {0}".format(e))

command_writ()



    #     data = self.write()
    #     self.declare(data)
    #     nentry.
    # def declare(self, text):
    #     engine = pyttsx3.init()
    #     engine.say(text)
    #     engine.runAndWait()
    #     self.write()
    #
    # def write(self):
    #     r = Recognizer()
    #     with Microphone() as source:
    #         r.energy_threshold = 4000
    #         r.adjust_for_ambient_noise(source, duration=0.5)
    #         print("Speak:")
    #         audio = r.listen(source)
    #     try:
    #         print("You said '" + r.recognize_sphinx(audio) + "';")
    #         data = str(r.recognize_sphinx(audio))
    #         return data
    #     except UnknownValueError:
    #         print("Could not understand audio")
    #     except RequestError as e:
    #         print("Could not request results; {0}".format(e))
    #
    #



        # def speekit(self, nentry, text):
        #     engine = pyttsx3.init()
        #     engine.say(text)
        #     engine.runAndWait()
        #
        #     nentry.focus()
        #
        # def write(self):
        #     # r = sr.Recognizer()
        #     # with sr.Microphone() as source:
        #     #     print("Speak:")
        #     #     audio = r.listen(source)
        #     # data = r.recognize_sphinx(audio)
        #     data2 = 'Attend Exam'.lower()
        #     return data2
        #

        #
        # def callnext(self, text):
        #     engine = pyttsx3.init()
        #     engine.say(text)
        #     engine.runAndWait()
        #
        #     # data = str(self.write())
        #     # length = len(data)
        #     # match = 'submit'
        #     #
        #     # if len(match) == length and match == data:
        #     #     next.controller.showframe(ExamPaper)
        #
        # def nextquestion(self, question, text1, text2, text3, text4):
        #     l = [question, text1, text2, text3, text4]
        #     for i in l:
        #         engine = pyttsx3.init()
        #         engine.say(i)
        #         engine.runAndWait()

        # file1 = gTTS(text=text, lang='en')
        # fn1 = text+'.mp3'
        # file1.save(fn1)
        #
        # question = pyglet.media.load(fn1)
        # question.play()
        # time.sleep(question.duration)

        # nexten.focus()
        # print('i am after sleep')
        # os.remove(fn1)
        # r = sr.Recognizer()
        # with sr.Microphone() as source:
        #     print("Speak:")
        #     audio = r.listen(source)
        # return r.recognize_sphinx(audio)

    # def write(self):
    #     r = sr.Recognizer()
    #     with sr.Microphone() as source:
    #         print("Speak:")
    #         audio = r.listen(source)
    #
    #     try:
    #         print("You said " + r.recognize_google(audio))
    #     except sr.UnknownValueError:
    #         print("Could not understand audio")
    #     except sr.RequestError as e:
    #         print("Could not request results; {0}".format(e))
