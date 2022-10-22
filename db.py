import mysql.connector
from mysql.connector import Error


# from conversion import *
# ------------------------------------------------------------------------------------------------------------------ #
# ----------------------------------------------- Creating connection ---------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------ #

def create_mysql_connection(host_name, user_name, user_pass):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_pass
        )
        print("###################################")
    except Error as err:
        print(err)
    return connection

# ------------------------------------------------------------------------------------------------------------------ #
# ----------------------------------------------- Creating database ------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------ #

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
    except Error as err:
        print(err)

# ------------------------------------------------------------------------------------------------------------------ #
# ----------------------------------------------- Creating database connection ------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------ #

def create_database_connection(host_name, user_name, user_pass, db):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_pass,
            database=db
        )
    except Error as err:
        print(err)
    return connection

# ------------------------------------------------------------------------------------------------------------------ #
# ----------------------------------------------- Creating Table --------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------ #


def create_table(connection, query, table):
    cursor = connection.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS " + table)
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
    except Error as err:
        print(err)

# ------------------------------------------------------------------------------------------------------------------ #
# ----------------------------------------------- Insert Data ------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------ #

def insert_data(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as err:
        print(err)
    cursor.close()
    connection.close()


# ------------------------------------------------------------------------------------------------------------------ #
# -------------------------------------------- Teacher Exam Input ----------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------ #


def teacher_input(name, idd, user, pas):  # ---------------------- Teachers table input -------------------------
    db_con = create_database_connection("localhost", "root", "izak3662", "ESVIP")
    query = "INSERT INTO Teacher_Tab(Name, Id, Teach_username, Password) VALUES({}, {}, {}, {});".format(name, idd,
                                                                                                         user, pas)
    insert_data(db_con, query)


# ------------------------------------------------------------------------------------------------------------------ #
# -------------------------------------- Username check ------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------ #


def usernamecheck(connection, username):  # ------------------- Username duplication check for teachers
    db_con = connection.connect('data.db')
    curs = db_con.cursor()
    curs.execute("SELECT Teach_username FROM Teacher_Tab")
    ulist = curs.fetchall()

    for i in range(len(ulist)):
        if username == ulist[i]:
            curs.close()
            db_con.close()
            return 'true'
        else:
            continue
    curs.close()
    db_con.close()
    return 'false'


# ------------------------------------------------------------------------------------------------------------------ #
# ----------------------------------------------- Teachers Login --------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------ #


def login(connection, user, pas):
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()

    curs.execute("SELECT Teach_username, Password FROM Teacher_Tab")
    loglist = curs.fetchall()

    for i in range(len(loglist)):
        if loglist[i][0] == user and loglist[i][1] == pas and user != '' and pas != '':
            curs.close()
            db_con.close()
            return 'true'
        else:
            print('con')
            continue
    curs.close()
    db_con.close()
    return 'false'


# ------------------------------------------------------------------------------------------------------------------ #
# ---------------------------------- Checking if the teacher has made that course.---------------------------------- #
# ------------------------------------------------------------------------------------------------------------------ #


def code_existence_check_t(connection,
                           code):  # ----------------Either the teacher has made this exam before -----------
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()
    x = 'false'
    curs.execute("SELECT Exam_Code FROM Written_Exam")
    ls1 = curs.fetchall()
    curs.execute("SELECT Exam_Code FROM Multiple_Choice_Exam")
    ls2 = curs.fetchall()
    curs.execute("SELECT Exam_Code FROM True_False_Exam")
    ls3 = curs.fetchall()
    ls = [ls1, ls2, ls3]
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            if ls[i][j] == code:
                x = 'true'
                curs.close()
                db_con.close()
                return x
            else:
                continue

    curs.close()
    db_con.close()
    return x


def code_existence_check_std(connection, code, name, idd):
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()
    x = 'false'

    curs.execute("SELECT Examcode FROM Student_Tab WHERE Name = ? AND Id = ?", (name, idd))
    c = curs.fetchall()
    for i in range(len(c)):
        if c[i] == code:
            x = 'true'
            curs.close()
            db_con.close()
            return x
        else:
            continue

    curs.close()
    db_con.close()
    return x


# ------------------------------------------------------------------------------------------------------------------ #
# ---------------------------------------------- Setting Question -------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------ #


def written_q(connection, code, question):
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()
    curs.execute("INSERT INTO Written_Exam(Exam_Code, Question) VALUES(?, ?);", (code, question))
    db_con.commit()
    curs.close()
    db_con.close()


def multiple_q(connection, code, question, op1, op2, op3):
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()
    curs.execute("INSERT INTO Multiple_Choice_Exam(Exam_Code, Question, Option1, Option2, Option3)"
                 " VALUES(?, ?, ?, ?, ?);", (code, question, op1, op2, op3))
    db_con.commit()
    curs.close()
    db_con.close()


def truefalse_q(connection, code, question):
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()
    curs.execute("INSERT INTO True_False_Exam(Exam_Code, Question) VALUES(?, ?);",
                 (code, question))
    db_con.commit()
    curs.close()
    db_con.close()


# ------------------------------------------------------------------------------------------------------------------ #
# ----------------------------------------------- Getting The  Questions ------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------ #


def getwrittenquestion(connection,
                       code):  # --------------------------------- Written ---------------------------------------
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()
    # if code:
    curs.execute("SELECT Question FROM Written_Exam WHERE Exam_Code = ?", (code,))
    wquestion = curs.fetchall()
    # else:
    # return ''
    curs.close()
    db_con.close()
    return wquestion


def gettruefalsequestion(connection,
                         code):  # ------------------------------------ true/false --------------------------------
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()

    # if code:
    curs.execute("SELECT Question FROM True_False_Exam WHERE "
                 "Exam_Code = ?", (code,))
    tfquestion = curs.fetchall()
    # else:
    #     return ''

    curs.close()
    db_con.close()
    return tfquestion


def getmultiplequestion(connection,
                        code):  # ------------------------------------ multiple choice ----------------------------
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()

    # if code:
    curs.execute("SELECT Question, Option1, Option2, Option3 FROM Multiple_Choice_Exam WHERE "
                 "Exam_Code = ?", (code,))
    ls = curs.fetchall()
    mquestion = [''] * len(ls)

    for i in range(len(ls)):
        mquestion[i] = ls[i]
    # else:
    #     return ''

    curs.close()
    db_con.close()
    return mquestion


#  ---------------------------------------------------------------------------------------------------- #
#  ----------------------------------------- Saving Answer --------------------------------------------- #
#  ---------------------------------------------------------------------------------------------------- #


def savingwans(connection, pcode, ecode, name, reg, atext):  # --------------------- Written answer mark
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()
    for i in range(len(atext)):
        a = atext[i].get('1.0', "end")
        curs.execute("INSERT INTO Student_Tab(Name, Id, Examcode, Papercode, WrittenAnswer) VALUES(?, ?, ?, ?, ?);",
                     (name, reg, ecode, pcode, str(a)))

    db_con.commit()
    curs.close()
    db_con.close()


def savingmulans(connection, pcode, ecode, name, reg, mulans):  # --------------------- Multiple answer mark
    print(mulans)
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()
    for i in range(len(mulans)):
        print(len(mulans))
        a = str(mulans[i])
        print(a)
        curs.execute("INSERT INTO Student_Tab(Name, Id, Examcode, Papercode, MultipleAnswer) VALUES(?, ?, ?, ?, ?);",
                     (name, reg, ecode, pcode, a))

    db_con.commit()
    curs.close()
    db_con.close()


def savingtfans(connection, pcode, ecode, name, reg, tfans):  # --------------------- True/False answer mark
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()
    for i in range(len(tfans)):
        a = tfans[i].get()
        curs.execute("INSERT INTO Student_Tab(Name, Id, Examcode, Papercode, TrueFalseAnswer) VALUES(?, ?, ?, ?, ?);",
                     (name, reg, ecode, pcode, a))

    db_con.commit()
    curs.close()
    db_con.close()


#  ---------------------------------------------------------------------------------------------------- #
#  ----------------------------------------- Getting Answer --------------------------------------------- #
#  ---------------------------------------------------------------------------------------------------- #


def gettingwrittenanswer(connection, code, pcode):  # ----------------------- Written Answer
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()

    curs.execute("SELECT WrittenAnswer FROM Student_Tab WHERE Examcode = ? AND Papercode = ?;", (code, pcode))
    wans = curs.fetchall()
    curs.close()
    db_con.close()
    return wans


def gettingmultipleanswer(connection, code, pcode):  # ----------------------- Multiple Answer
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()

    curs.execute("SELECT MultipleAnswer FROM Student_Tab WHERE Examcode = ? AND Papercode = ?;", (code, pcode))
    mans = curs.fetchall()
    curs.close()
    db_con.close()
    return mans


def gettingtruefalseanswer(connection, code, pcode):  # ----------------------- True/False Answer
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()

    curs.execute("SELECT TrueFalseAnswer FROM Student_Tab WHERE Examcode = ? AND Papercode = ?;", (code, pcode))
    tfans = curs.fetchall()
    curs.close()
    db_con.close()
    return tfans


# --------------------------------------------------- Saving the Marks --------------------------------------------
# --------------------------------------------------- Saving the Marks --------------------------------------------


def savingwmark(connection, pcode, ecode, wmark, wans):  # --------------------- Written answer mark
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()

    curs.execute(
        "INSERT INTO Student_Tab(WMarks) VALUES(?) WHERE Examcode = ? AND Papercode = ? AND WrittenAnswer = ?;",
        (wmark, ecode, pcode, wans))

    db_con.commit()
    curs.close()
    db_con.close()


def savingmulmark(connection, pcode, ecode, mulmark, mulans):  # --------------------- Multiple answer mark
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()

    curs.execute("INSERT INTO Student_Tab(MMarks) VALUES(?) WHERE Examcode = ? AND Papercode = ? AND"
                 " MultipleAnswer = ?;", (mulmark, ecode, pcode, mulans))

    db_con.commit()
    curs.close()
    db_con.close()


def savingtfmark(connection, pcode, ecode, tfmark, tfans):  # --------------------- True/False answer mark
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()

    curs.execute("INSERT INTO Student_Tab(TFMarks) VALUES(?) WHERE Examcode = ? AND Papercode = ? AND"
                 " TrueFalseAnswer = ?;", (tfmark, ecode, pcode, tfans))

    db_con.commit()
    curs.close()
    db_con.close()


# --------------------------------------------- Result ------------------------------------------------
# --------------------------------------------- Result ------------------------------------------------


def result(connection, name, idd, ecode):
    db_con = connection.connect('data.db')
    print("Created")
    curs = db_con.cursor()

    curs.execute("SELECT WMarks, MMarks, TFMarks FROM Student_Tab WHERE Name = ? AND Id = ? AND Examcode = ?;",
                 (name, idd, ecode))
    marks = curs.fetchall()
    res = 0
    for i in range(len(marks)):
        res = res + marks[i][0]
        res = res + marks[i][1]
        res = res + marks[i][2]

    curs.close()
    db_con.close()
    return res


# creat()

mysql_con = create_mysql_connection("localhost", "root", "izak3662")
create_database(mysql_con, "CREATE DATABASE ESVIP")
db_con = create_database_connection("localhost", "root", "izak3662", "ESVIP")

tab_list = ['Teacher_tab', 'Student_Tab', 'Written_Exam', 'Multiple_Choice_Exam', 'True_False_Exam']
create_table(db_con,
             "CREATE TABLE Teacher_tab(Name TEXT, Id INTEGER, Teach_username TEXT, Password TEXT);",
             "Teacher_tab")
create_table(db_con,
             "CREATE TABLE Student_Tab(Name TEXT, Id INTEGER, Examcode TEXT, WrittenAnswer TEXT,"
             "MultipleAnswer TEXT, TrueFalseAnswer TEXT, "
             " WMarks REAL, MMarks REAL, TFMarks REAL, Papercode INTEGER);",
             "Student_Tab")
create_table(db_con,
             "CREATE TABLE Multiple_Choice_Exam(Exam_Code TEXT,"
             " Question TEXT, Option1 TEXT, Option2 TEXT, Option3 TEXT);",
             "Multiple_Choice_Exam")
create_table(db_con,
             "CREATE TABLE Written_Exam(Exam_Code TEXT, Question TEXT);",
             "Written_Exam")
create_table(db_con,
             "CREATE TABLE True_False_Exam(Exam_Code TEXT, Question TEXT);",
             "True_False_Exam")

# savingmulans('789', '34', 'asik', 12, 3)

# def checkvalidation(frame, btn, con, vc, course, exam, vcdata):
#     vcode = int(vcdata.get())
#     ccode = str(course.get())
#     ecode = str(exam.get())
#     print(vcode)
#     print(ccode)
#     print(ecode)
#     res = validationcheck(vcode, ccode, ecode)
#     if res:
#         frame.bind('<Return>', con.showframe(ExamPaper))
#         btn.bind('<Return>', con.showframe(ExamPaper))
#     else:
#         error_read = Conversion()
#         error_read.declare('Validation Code Error')
#         error_read.speekit(vc, 'Validation Code')

# student_input('Amin', 3329, 'Sylhet Engineering College', 'CSE', 'CSE-101', '1st Term')
# teacher_input('Abidul Haque', 'cse201055', 'Sylhet Engineering College', 'CSE', 'CSE-507', 'abidul1234', '12345')
# teacher_input('Asad Shams', 'cse201360', 'Sylhet Engineering College', 'CSE', 'CSE-701', 'asad1234', '54321')
# make_q('Sylhet Engineering College', 'CSE', 'CSE-101','1st Term', 3, 303132, 1, 'What is a peripheral device', 'op1',
#        'op2', 'op3', 'op4')
# make_q('Sylhet Engineering College', 'CSE', 'CSE-101', '1st Term', 3, 303132, 2, 'Which is not a peripheral device',
#        'mouse', 'mobile phone', 'microprocessor', 'headphone')
# db_con.commit()

# def student_input(std, reg, code):
#     db_con = connection.connect('data.db')
#     print("Created")
#     curs = db_con.cursor()
#
#     curs.execute("INSERT INTO Student_Tab(Std_Name, Reg_No, Examcode) VALUES(?, ?, ?);", (std, reg, code))
#     db_con.commit()
#     curs.close()
#     db_con.close()
# def exampaperinfo(std, reg, code, pcode):
#     db_con = connection.connect('data.db')
#     print("Created")
#     curs = db_con.cursor()
#
#     curs.execute("INSERT INTO Student_Tab(Name, Id, Examcode, Papercode) VALUES(?, ?, ?, ?);", (std, reg, code, pcode))
#
#     db_con.commit()
#     curs.close()
#     db_con.close()


# print('end')
