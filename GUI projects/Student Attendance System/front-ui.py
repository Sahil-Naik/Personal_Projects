import tkinter as tk
import tkinter.messagebox
from functools import partial
import sqlite3

'''
Databases - admin -> Table -> admin_login(Username, Password, Mobile)
            staff -> Table -> staff_login(Username, Password, Mobile)
          student -> Table -> student_att(Name, PRN, Department, Division, Attendance, Month)
'''

def main_destroy():
    root.destroy()

# ----------------------- STAFF LOGIN -----------------------

def login_staff():
    root.withdraw()
    staff_win = tk.Toplevel(root)
    staff_win.title("Staff login")
    staff_win.geometry("640x480+500+200")
    staff_win.resizable(False, False)
    staff_uname_dtype = tk.StringVar()
    staff_pass_dtype = tk.StringVar()

    database_staff = 'staff.db'
    table_staff = 'staff_login'

    def after_staff_login():

        # ----------------------- BACK TO STAFF MAIN MENU -----------------------

        def back_to_login_staff():
            staff_logged.destroy()
            staff_win.deiconify()
            tkinter.messagebox.showinfo('Logged out', 'Logout Successfull!')

        # ----------------------- STUDENT ATTENDANCE -----------------------

        def student_attendance():

            def back_to_staff():
                student_att.destroy()
                staff_logged.deiconify()

            def retrieve_student_data(stud_name, stud_prn, month, database):
                conn = sqlite3.connect(database)
                c = conn.cursor()

                STUD_NAME = (stud_name.get())
                STUD_PRN = (stud_prn.get())
                ATT_MONTH = (month.get())

                if ATT_MONTH.upper()!='ALL':

                    command = (f"SELECT Attendance,Month FROM student_att WHERE Name='{STUD_NAME.capitalize()}'"
                               f" AND PRN='{STUD_PRN.capitalize()}' AND Month='{ATT_MONTH.capitalize()}'")

                    c.execute(command)
                    result_list = c.fetchall()

                    if len(result_list) == 1:
                        att_count = f'{result_list[0][0]}'
                        att_month = f'{result_list[0][1]}'

                        stud_att_count_l = tk.Label(student_att, text="Attendance Count", font=('Bahnshcrift', 16, 'bold'),
                                                    justify='center',
                                                    bg='khaki', fg='black')
                        stud_att_count_l.place(x=35, y=200, width=215, height=45)

                        stud_att_count = tk.Label(student_att, text=att_count, font=('Bahnshcrift', 45, 'bold'), justify='center',
                                                  bg='snow', fg='black')
                        stud_att_count.place(x=35, y=245, width=215, height=120)

                        stud_att_month = tk.Label(student_att, text="Month", font=('Bahnshcrift', 16, 'bold'), justify='center',
                                                  bg='khaki', fg='black')
                        stud_att_month.place(x=355, y=200, width=215, height=45)

                        stud_att_month_count = tk.Label(student_att, text=att_month, font=('Bahnshcrift', 25, 'bold'),
                                                        justify='center',
                                                        bg='snow', fg='black')
                        stud_att_month_count.place(x=355, y=245, width=215, height=120)

                    else:

                        stud_att_count_l = tk.Label(student_att, text="Attendance Count", font=('Bahnshcrift', 16, 'bold'),
                                                    justify='center',
                                                    bg='khaki', fg='black')
                        stud_att_count_l.place(x=35, y=200, width=215, height=45)

                        stud_att_count = tk.Label(student_att, text='No Data', font=('Bahnshcrift', 25, 'bold'),
                                                  justify='center',
                                                  bg='snow', fg='black')
                        stud_att_count.place(x=35, y=245, width=215, height=120)

                        stud_att_month = tk.Label(student_att, text="Month", font=('Bahnshcrift', 16, 'bold'),
                                                  justify='center',
                                                  bg='khaki', fg='black')
                        stud_att_month.place(x=355, y=200, width=215, height=45)

                        stud_att_month_count = tk.Label(student_att, text='No Data', font=('Bahnshcrift', 25, 'bold'),
                                                        justify='center',
                                                        bg='snow', fg='black')
                        stud_att_month_count.place(x=355, y=245, width=215, height=120)

                else:

                    command = (f"SELECT Attendance FROM student_att WHERE Name='{STUD_NAME.capitalize()}'"
                               f" AND PRN='{STUD_PRN.capitalize()}'")

                    c.execute(command)
                    result_list = c.fetchall()

                    att_sum = 0
                    for i in range(len(result_list)):
                        att_sum+=result_list[i][0]

                    if len(result_list) >= 1:

                        stud_att_count_l = tk.Label(student_att, text="Attendance Count",
                                                    font=('Bahnshcrift', 16, 'bold'),
                                                    justify='center',
                                                    bg='khaki', fg='black')
                        stud_att_count_l.place(x=35, y=200, width=215, height=45)

                        stud_att_count = tk.Label(student_att, text=att_sum, font=('Bahnshcrift', 45, 'bold'),
                                                  justify='center',
                                                  bg='snow', fg='black')
                        stud_att_count.place(x=35, y=245, width=215, height=120)

                        stud_att_month = tk.Label(student_att, text="Month", font=('Bahnshcrift', 16, 'bold'),
                                                  justify='center',
                                                  bg='khaki', fg='black')
                        stud_att_month.place(x=355, y=200, width=215, height=45)

                        stud_att_month_count = tk.Label(student_att, text='ALL', font=('Bahnshcrift', 32, 'bold'),
                                                        justify='center',
                                                        bg='snow', fg='black')
                        stud_att_month_count.place(x=355, y=245, width=215, height=120)

                    else:

                        stud_att_count_l = tk.Label(student_att, text="Attendance Count",
                                                    font=('Bahnshcrift', 16, 'bold'),
                                                    justify='center',
                                                    bg='khaki', fg='black')
                        stud_att_count_l.place(x=35, y=200, width=215, height=45)

                        stud_att_count = tk.Label(student_att, text='No Data', font=('Bahnshcrift', 25, 'bold'),
                                                  justify='center',
                                                  bg='snow', fg='black')
                        stud_att_count.place(x=35, y=245, width=215, height=120)

                        stud_att_month = tk.Label(student_att, text="Month", font=('Bahnshcrift', 16, 'bold'),
                                                  justify='center',
                                                  bg='khaki', fg='black')
                        stud_att_month.place(x=355, y=200, width=215, height=45)

                        stud_att_month_count = tk.Label(student_att, text='No Data', font=('Bahnshcrift', 25, 'bold'),
                                                        justify='center',
                                                        bg='snow', fg='black')
                        stud_att_month_count.place(x=355, y=245, width=215, height=120)



            staff_logged.withdraw()
            student_att = tk.Toplevel(staff_logged)
            student_att.title("Student Attendance")
            student_att.geometry("640x480+500+200")
            student_att.resizable(False, False)

            stud_name_dtype = tk.StringVar()
            stud_prn_dtype = tk.StringVar()
            att_month_dtype = tk.StringVar()

            # ----------------------- STUDENT ATTENDANCE FOREGROUNDS -----------------------

            background = tk.Label(student_att, text="", font=('Bahnshcrift', 22, 'bold'), justify='center',
                                  bg='gainsboro', fg='black')
            background.place(x=0, y=0, width=640, height=480)

            stud_header = tk.Label(student_att, text="STUDENT ATTENDANCE", font=('Bahnshcrift', 25, 'bold'), justify='center',
                                    bg='khaki', fg='black')
            stud_header.place(x=0, y=0, width=670, height=70)

            separator_1 = tk.Label(student_att, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                                   bg='black', fg='black')
            separator_1.place(x=0, y=0, width=670, height=3)

            separator_2 = tk.Label(student_att, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                                   bg='black', fg='black')
            separator_2.place(x=0, y=70, width=670, height=3)

            # ----------------------- STUDENT NAME -----------------------

            stud_name = tk.Label(student_att, text="NAME", font=('Bahnshcrift', 15, 'bold'), justify='center',
                                  bg='khaki', fg='black')
            stud_name.place(x=10, y=95, width=115, height=40)

            stud_name_field = tk.Entry(student_att, textvariable=stud_name_dtype, font=('Bahnshcrift', 15, 'bold'))
            stud_name_field.place(x=121, y=95, width=165, height=40)

            # ----------------------- STUDENT PRN -----------------------

            stud_prn = tk.Label(student_att, text="PRN", font=('Bahnshcrift', 15, 'bold'), justify='center',
                                  bg='khaki', fg='black')
            stud_prn.place(x=325, y=95, width=115, height=40)

            stud_prn_field = tk.Entry(student_att, textvariable=stud_prn_dtype,
                                        font=('Bahnshcrift', 15, 'bold'))
            stud_prn_field.place(x=430, y=95, width=165, height=40)

            # ----------------------- ATTENDANCE MONTH -----------------------

            att_month = tk.Label(student_att, text="MONTH", font=('Bahnshcrift', 15, 'bold'), justify='center',
                                  bg='khaki', fg='black')
            att_month.place(x=10, y=145, width=115, height=40)

            att_month_field = tk.Entry(student_att, textvariable=att_month_dtype,
                                        font=('Bahnshcrift', 15, 'bold'))
            att_month_field.place(x=121, y=145, width=165, height=40)



            stud_get_data = partial(retrieve_student_data, stud_name_dtype, stud_prn_dtype, att_month_dtype, 'student.db')

            check_student = tk.Button(student_att, text="Check Student", font=('Bahnshcrift', 13, 'bold'),
                                    command=stud_get_data, bg='lawngreen', bd=3, fg='black')
            check_student.place(x=360, y=145, width=195)

            # ----------------------- STUDENT ATTENDANCE -----------------------

            stud_att_count_l = tk.Label(student_att, text="Attendance Count", font=('Bahnshcrift', 16, 'bold'), justify='center',
                                bg='khaki', fg='black')
            stud_att_count_l.place(x=35, y=200, width=215, height=45)

            stud_att_count = tk.Label(student_att, text="", font=('Bahnshcrift', 45, 'bold'), justify='center',
                                bg='snow', fg='black')
            stud_att_count.place(x=35, y=245, width=215, height=120)

            stud_att_month = tk.Label(student_att, text="Month", font=('Bahnshcrift', 16, 'bold'), justify='center',
                                bg='khaki', fg='black')
            stud_att_month.place(x=355, y=200, width=215, height=45)

            stud_att_month_count = tk.Label(student_att, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                                bg='snow', fg='black')
            stud_att_month_count.place(x=355, y=245, width=215, height=120)


            staff_main_menu = tk.Button(student_att, text="Back", font=('Bahnshcrift', 13, 'bold'),
                                      command=back_to_staff, bg='black', bd=0, fg='white')
            staff_main_menu.place(x=540, y=430, width=65)

        # ----------------------- REGISTER STUDENT -----------------------

        def register_student():

            def regex_update_student(name, prn, dept, div, att, month, database):
                conn = sqlite3.connect(database)
                c = conn.cursor()

                s_name = (name.get())
                s_prn = (prn.get())
                s_dept = (dept.get())
                s_div = (div.get())
                s_att = att.get()
                s_month = (month.get())

                print(s_name,s_prn,s_dept,s_div,s_att,s_month)

                check_info_command = (f"SELECT * FROM student_att WHERE Name='{s_name.capitalize()}'"
                                      f" AND PRN='{s_prn.capitalize()}' AND Department='{s_dept.capitalize()}'"
                                      f" AND Division='{s_div.capitalize()}'AND Month='{s_month.capitalize()}';")

                c.execute(check_info_command)

                list_result = c.fetchall()
                print(list_result)

                if len(list_result)==1:
                    tkinter.messagebox.showinfo('Updated', 'Update Successfull!')
                    with conn:
                        update_command = (f"UPDATE student_att SET Attendance={s_att} WHERE Name='{s_name.capitalize()}'"
                                          f" AND PRN='{s_prn.capitalize()}' AND Month='{s_month.capitalize()}';")
                        c.execute(update_command)

                else:
                    tkinter.messagebox.showinfo('Registered', 'Registration Successfull!')
                    with conn:
                        insert_command = (f"INSERT INTO student_att VALUES ('{s_name.capitalize()}','{s_prn.capitalize()}',"
                                          f"'{s_dept.capitalize()}','{s_div.capitalize()}',{s_att},'{s_month.capitalize()}');")
                        c.execute(insert_command)

            def back_to_staff():
                student_registration.destroy()
                staff_logged.deiconify()

            staff_logged.withdraw()
            student_registration = tk.Toplevel(staff_logged)
            student_registration.title("Student Registration")
            student_registration.geometry("640x480+500+200")
            student_registration.resizable(False, False)

            new_stud_name = tk.StringVar()
            new_stud_prn = tk.StringVar()
            new_stud_department = tk.StringVar()
            new_stud_division = tk.StringVar()
            new_stud_attendance = tk.StringVar()
            new_stud_month = tk.StringVar()

            # ----------------------- REGISTER STUDENT FOREGROUNDS -----------------------

            background = tk.Label(student_registration, text="", font=('Bahnshcrift', 22, 'bold'), justify='center',
                                  bg='gainsboro', fg='black')
            background.place(x=0, y=0, width=640, height=480)

            stud_header = tk.Label(student_registration, text="STUDENT REGISTRATION", font=('Bahnshcrift', 25, 'bold'),
                                   justify='center',
                                   bg='khaki', fg='black')
            stud_header.place(x=0, y=0, width=670, height=70)

            separator_1 = tk.Label(student_registration, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                                   bg='black', fg='black')
            separator_1.place(x=0, y=0, width=670, height=3)

            separator_2 = tk.Label(student_registration, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                                   bg='black', fg='black')
            separator_2.place(x=0, y=70, width=670, height=3)

            staff_main_menu = tk.Button(student_registration, text="Back", font=('Bahnshcrift', 13, 'bold'),
                                        command=back_to_staff,
                                        bg='black', bd=0, fg='white')
            staff_main_menu.place(x=540, y=430, width=65)

            # ----------------------- STUDENT NAME -----------------------

            stud_name = tk.Label(student_registration, text="NAME", font=('Bahnshcrift', 15, 'bold'), justify='center',
                                 bg='khaki', fg='black')
            stud_name.place(x=10, y=105, width=115, height=40)

            stud_name_field = tk.Entry(student_registration, textvariable=new_stud_name, font=('Bahnshcrift', 15, 'bold'))
            stud_name_field.place(x=121, y=105, width=165, height=40)

            # ----------------------- STUDENT PRN -----------------------

            stud_prn = tk.Label(student_registration, text="PRN", font=('Bahnshcrift', 13, 'bold'), justify='center',
                                bg='khaki', fg='black')
            stud_prn.place(x=325, y=105, width=115, height=40)

            stud_prn_field = tk.Entry(student_registration, textvariable=new_stud_prn,
                                      font=('Bahnshcrift', 15, 'bold'))
            stud_prn_field.place(x=430, y=105, width=165, height=40)

            # ----------------------- STUDENT DEPARTMENT -----------------------

            stud_dept = tk.Label(student_registration, text="DEPARTMENT", font=('Bahnshcrift', 11, 'bold'), justify='center',
                                 bg='khaki', fg='black')
            stud_dept.place(x=10, y=155, width=115, height=40)


            stud_dept_field = tk.Entry(student_registration, textvariable=new_stud_department,
                                       font=('Bahnshcrift', 15, 'bold'))
            stud_dept_field.place(x=121, y=155, width=165, height=40)

            # ----------------------- STUDENT DIVISION -----------------------

            stud_div = tk.Label(student_registration, text="DIVISION", font=('Bahnshcrift', 13, 'bold'), justify='center',
                                bg='khaki', fg='black')
            stud_div.place(x=320, y=160, width=115, height=40)

            stud_div_field = tk.Entry(student_registration, textvariable=new_stud_division,
                                      font=('Bahnshcrift', 15, 'bold'))
            stud_div_field.place(x=430, y=160, width=165, height=40)

            # ----------------------- STUDENT ATTENDANCE -----------------------

            stud_att = tk.Label(student_registration, text="ATTENDANCE", font=('Bahnshcrift', 12, 'bold'), justify='center',
                                 bg='khaki', fg='black')
            stud_att.place(x=320, y=220, width=125, height=40)

            stud_att_field = tk.Entry(student_registration, textvariable=new_stud_attendance,
                                       font=('Bahnshcrift', 15, 'bold'))
            stud_att_field.place(x=440, y=220, width=165, height=40)

            # ----------------------- ATTENDANCE MONTH -----------------------

            stud_att_month = tk.Label(student_registration, text="MONTH", font=('Bahnshcrift', 15, 'bold'), justify='center',
                                 bg='khaki', fg='black')
            stud_att_month.place(x=10, y=220, width=115, height=40)

            stud_att_month_field = tk.Entry(student_registration, textvariable=new_stud_month,
                                       font=('Bahnshcrift', 15, 'bold'))
            stud_att_month_field.place(x=121, y=220, width=165, height=40)

            # ----------------------- REGISTER STUDENT -----------------------

            stud_regex = partial(regex_update_student, new_stud_name, new_stud_prn, new_stud_department,
                                 new_stud_division, new_stud_attendance, new_stud_month, 'student.db')

            check_student = tk.Button(student_registration, text="Check Student", font=('Bahnshcrift', 13, 'bold'),
                                      command=stud_regex, bg='lawngreen', bd=3, fg='black')
            check_student.place(x=210, y=295, width=195)

        # ----------------------- STAFF LOGGED WINDOW -----------------------

        staff_win.withdraw()
        staff_logged = tk.Toplevel(staff_win)
        staff_logged.title("Staff")
        staff_logged.geometry("640x480+500+200")
        staff_logged.resizable(False, False)

        staff_header = tk.Label(staff_logged, text="STAFF", font=('Bahnshcrift', 25, 'bold'), justify='center',
                                bg='khaki', fg='black')
        staff_header.place(x=0, y=0, width=670, height=70)

        separator_1 = tk.Label(staff_logged, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                               bg='black', fg='black')
        separator_1.place(x=0, y=0, width=670, height=3)

        separator_2 = tk.Label(staff_logged, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                               bg='black', fg='black')
        separator_2.place(x=0, y=70, width=670, height=3)

        staff_log_out = tk.Button(staff_logged, text="Log Out", font=('Bahnshcrift', 13, 'bold'), command=back_to_login_staff,
                               bg='Red', bd=0, fg='white')
        staff_log_out.place(x=525, y=430, width=85)

        # ----------------------- CHECK STUDENT ATTENDANCE BUTTON -----------------------

        student_attendance = tk.Button(staff_logged, text="STUDENT ATTENDANCE", font=('Bahnshcrift', 18, 'bold'),
                                       command=student_attendance, bg='darkslategrey', bd=1, fg='white')
        student_attendance.place(x=165, y=140, width=320)

        # ----------------------- REGISTER STUDENT BUTTON -----------------------

        regx_student = tk.Button(staff_logged, text="REGISTER STUDENT", font=('Bahnshcrift', 18, 'bold'),
                                 command=register_student, bg='darkslategrey', bd=1, fg='white')
        regx_student.place(x=165, y=240, width=320)

    # ----------------------- BACK TO ROOT MAIN MENU -----------------------

    def back_to_main():
        staff_win.destroy()
        root.deiconify()

    # ----------------------- STAFF LOGIN CHECK -----------------------

    def check_staff_credentials(username, password, database):
        conn = sqlite3.connect(database)
        c = conn.cursor()

        USER = (username.get())
        PASS = (password.get())

        command = (f"SELECT * FROM '{table_staff}' WHERE Username='{USER}' AND Password='{PASS}'")

        c.execute(command)

        if len(c.fetchall()) == 1:
            login_stat = tk.Label(staff_win, text="", font=('Bahnshcrift', 12, 'bold'), justify='center',
                                  fg='red', bg='gainsboro')
            login_stat.place(x=260, y=80, width=140, height=55)

            after_staff_login()

        else:
            login_stat = tk.Label(staff_win, text="Login Failed", font=('Bahnshcrift', 12, 'bold'), justify='center',
                                  fg='red', bg='gainsboro')
            login_stat.place(x=260, y=80, width=140, height=55)


        conn.commit()
        conn.close()

    # ----------------------- STAFF PAGE FOREGROUNDS -----------------------

    background = tk.Label(staff_win, text="", font=('Bahnshcrift', 22, 'bold'), justify='center',
                          bg='gainsboro', fg='black')
    background.place(x=0, y=0, width=640, height=480)

    staff_header = tk.Label(staff_win, text="STAFF LOGIN", font=('Bahnshcrift', 25, 'bold'), justify='center',
                        bg='khaki', fg='black')
    staff_header.place(x=0, y=0, width=670, height=70)

    separator_1 = tk.Label(staff_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    separator_1.place(x=0, y=0, width=670, height=3)

    separator_2 = tk.Label(staff_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    separator_2.place(x=0, y=70, width=670, height=3)


    # --------- Staff Username Label & Entry box ---------

    staff_name = tk.Label(staff_win, text="Username", font=('Bahnshcrift', 18, 'bold'), justify='center',
                           bg='khaki', fg='black')
    staff_name.place(x=55, y=150, width=170, height=50)

    staff_name_field = tk.Entry(staff_win, textvariable=staff_uname_dtype, font=('Bahnshcrift', 18, 'bold'))\
        .place(x=235, y=150, width=315, height=50)

    name_separator_1 = tk.Label(staff_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    name_separator_1.place(x=50, y=147, width=503, height=3)

    name_separator_2 = tk.Label(staff_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    name_separator_2.place(x=50, y=201, width=503, height=3)

    name_separator_3 = tk.Label(staff_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    name_separator_3.place(x=50, y=148, width=3, height=53)

    name_separator_4 = tk.Label(staff_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    name_separator_4.place(x=225, y=148, width=11, height=53)

    name_separator_5 = tk.Label(staff_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    name_separator_5.place(x=550, y=148, width=3, height=53)

    # --------- Staff Password Label & Entry box ---------

    staff_pass = tk.Label(staff_win, text="Password", font=('Bahnshcrift', 18, 'bold'), justify='center',
                           bg='khaki', fg='black')
    staff_pass.place(x=55, y=220, width=170, height=50)

    staff_pass_field = tk.Entry(staff_win, textvariable=staff_pass_dtype, show='*', font=('Bahnshcrift', 18, 'bold'))\
        .place(x=235, y=220, width=315, height=50)

    pass_separator_1 = tk.Label(staff_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    pass_separator_1.place(x=50, y=217, width=503, height=3)

    pass_separator_2 = tk.Label(staff_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    pass_separator_2.place(x=50, y=271, width=503, height=3)

    pass_separator_3 = tk.Label(staff_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    pass_separator_3.place(x=50, y=218, width=3, height=53)

    pass_separator_4 = tk.Label(staff_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    pass_separator_4.place(x=225, y=218, width=11, height=53)

    pass_separator_5 = tk.Label(staff_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    pass_separator_5.place(x=550, y=218, width=3, height=53)

    logged = partial(check_staff_credentials, staff_uname_dtype, staff_pass_dtype, database_staff)

    staff_login = tk.Button(staff_win, text="Login", font=('Bahnshcrift', 20, 'bold'), command=logged,
                            bg='lawngreen', bd=3, fg='black')
    staff_login.place(x=280, y=300, width=105)

    staff_back = tk.Button(staff_win, text="Back", font=('Bahnshcrift', 13, 'bold'), command=back_to_main, bg='black',
                           bd=0, fg='white')
    staff_back.place(x=540, y=430, width=65)

# ----------------------- ADMIN LOGIN UI -----------------------

def login_admin():
    root.withdraw()
    admin_win = tk.Toplevel(root)
    admin_win.title("Admin login")
    admin_win.geometry("640x480+500+200")
    admin_win.resizable(False, False)

    database_admin = 'admin.db'

    admin_uname_dtype = tk.StringVar()
    admin_pass_dtype = tk.StringVar()

    # ----------------------- AFTER ADMIN LOGS IN -----------------------

    def after_admin_login():

        # ----------------------- ADMIN CHANGES STAFF -----------------------

        def change_staff():


            # ----------------------- BACK FROM ADMIN MAIN MENU TO ADMIN LOG IN MAIN MENU -----------------------

            def back_admin_staff():
                admin_changes_staff.withdraw()
                admin_logged.deiconify()

            # ----------------------- ADMIN REGISTERS NEW STAFF -----------------------

            def regex_staff():

                # ----------------------- BACK FROM ADMIN STAFF CHANGE TO ADMIN LOGGED IN MAIN MENU -----------------------

                def back_staff_admin():
                    new_staff.destroy()
                    admin_changes_staff.deiconify()

                # ----------------------- ADMIN SUCCESSFULLY ADDS NEW STAFF -----------------------

                def clicked_create(username, password, mobile, database):
                    conn = sqlite3.connect(database)
                    c = conn.cursor()

                    NEW_STAFF = (username.get())
                    NEW_PASS = (password.get())
                    NEW_MOB = (mobile.get())

                    test_staff_command = (f"SELECT * FROM staff_login WHERE Username='{NEW_STAFF}' OR Mobile='{NEW_MOB}'")
                    c.execute(test_staff_command)

                    if len(c.fetchall()) >= 1:
                        tkinter.messagebox.showinfo('Database', 'Username or Mobile already registered!')

                    else:
                        tkinter.messagebox.showinfo('Database', 'Staff registered!')
                        command = (f"INSERT INTO staff_login VALUES ('{NEW_STAFF}','{NEW_PASS}','{NEW_MOB}')")
                        c.execute(command)
                        conn.commit()

                admin_changes_staff.withdraw()
                new_staff = tk.Toplevel(admin_changes_staff)
                new_staff.title("Manage Staff")
                new_staff.geometry("640x480+500+200")
                new_staff.resizable(False, False)
                background = tk.Label(new_staff, text="", font=('Bahnshcrift', 22, 'bold'), justify='center',
                                      bg='gainsboro', fg='black')
                background.place(x=0, y=0, width=640, height=480)
                staff_name_dtype = tk.StringVar()
                staff_pass_dtype = tk.StringVar()
                staff_mobile_dtype = tk.StringVar()

                staff_regex_header = tk.Label(new_staff, text="NEW STAFF", font=('Bahnshcrift', 25, 'bold'),
                                              justify='center', bg='khaki', fg='black')
                staff_regex_header.place(x=0, y=0, width=670, height=70)

                separator_1 = tk.Label(new_staff, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                                       bg='black', fg='black')
                separator_1.place(x=0, y=0, width=670, height=3)

                separator_2 = tk.Label(new_staff, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                                       bg='black', fg='black')
                separator_2.place(x=0, y=70, width=670, height=3)

                newstaff_name = tk.Label(new_staff, text="Username", font=('Bahnshcrift', 18, 'bold'), justify='center',
                                      bg='khaki', fg='black')
                newstaff_name.place(x=55, y=130, width=170, height=50)

                newstaff_name_field = tk.Entry(new_staff, textvariable=staff_name_dtype, font=('Bahnshcrift', 18, 'bold'))
                newstaff_name_field.place(x=235, y=130, width=315, height=50)

                newstaff_pass = tk.Label(new_staff, text="Password", font=('Bahnshcrift', 18, 'bold'), justify='center',
                                      bg='khaki', fg='black')
                newstaff_pass.place(x=55, y=200, width=170, height=50)

                newstaff_pass_field = tk.Entry(new_staff, textvariable=staff_pass_dtype, show='*',
                                               font=('Bahnshcrift', 18, 'bold'))
                newstaff_pass_field.place(x=235, y=200, width=315, height=50)

                newstaff_mobile = tk.Label(new_staff, text="Mobile", font=('Bahnshcrift', 18, 'bold'), justify='center',
                                      bg='khaki', fg='black')
                newstaff_mobile.place(x=55, y=270, width=170, height=50)

                newstaff_mobile_field = tk.Entry(new_staff, textvariable=staff_mobile_dtype, show='*',
                                               font=('Bahnshcrift', 18, 'bold'))
                newstaff_mobile_field.place(x=235, y=270, width=315, height=50)


                created = partial(clicked_create, staff_name_dtype, staff_pass_dtype, staff_mobile_dtype, 'staff.db')

                regx_staff_ = tk.Button(new_staff, text="Register", font=('Bahnshcrift', 19, 'bold'),
                                            command=created, bg='limegreen', bd=1, fg='black')
                regx_staff_.place(x=310, y=350, width=125)











                regx_staff_back = tk.Button(new_staff, text="Back", font=('Bahnshcrift', 13, 'bold'),
                                           command=back_staff_admin, bg='black', bd=0, fg='white')
                regx_staff_back.place(x=540, y=430, width=65)

            # ----------------------- ADMIN UPDATES OLD STAFF -----------------------

            def update_staff():

                def clicked_update(username, password, mobile, database):
                    conn = sqlite3.connect(database)
                    c = conn.cursor()

                    UP_STAFF = (username.get())
                    UP_PASS = (password.get())
                    UP_MOB = (mobile.get())

                    test_staff_command = (f"SELECT * FROM staff_login WHERE Username='{UP_STAFF}' AND Mobile='{UP_MOB}'")
                    c.execute(test_staff_command)

                    if len(c.fetchall()) == 0:
                        tkinter.messagebox.showinfo('Not Found', 'No such User found!')

                    else:
                        tkinter.messagebox.showinfo('Database', 'Staff Update!')
                        command = (f"UPDATE staff_login SET Username='{UP_STAFF}', Password='{UP_PASS}', Mobile='{UP_MOB}'"
                                   f"WHERE Username='{UP_STAFF}' AND Mobile='{UP_MOB}'")
                        c.execute(command)
                        conn.commit()



                # --------------------- BACK FROM ADMIN STAFF UPDATE TO ADMIN LOGGED IN MAIN MENU ---------------------

                def back_staff_admin():
                    staff_update.destroy()
                    admin_changes_staff.deiconify()

                admin_changes_staff.withdraw()
                staff_update = tk.Toplevel(admin_changes_staff)
                staff_update.title("Manage Staff")
                staff_update.geometry("640x480+500+200")
                staff_update.resizable(False, False)
                background = tk.Label(staff_update, text="", font=('Bahnshcrift', 22, 'bold'), justify='center',
                                      bg='gainsboro', fg='black')
                background.place(x=0, y=0, width=640, height=480)

                upd_staff_back = tk.Button(staff_update, text="Back", font=('Bahnshcrift', 13, 'bold'),
                                       command=back_staff_admin, bg='black', bd=0, fg='white')
                upd_staff_back.place(x=540, y=430, width=65)

                staff_name_dtype = tk.StringVar()
                staff_pass_dtype = tk.StringVar()
                staff_mobile_dtype = tk.StringVar()

                staff_regex_header = tk.Label(staff_update, text="NEW STAFF", font=('Bahnshcrift', 25, 'bold'),
                                              justify='center', bg='khaki', fg='black')
                staff_regex_header.place(x=0, y=0, width=670, height=70)

                separator_1 = tk.Label(staff_update, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                                       bg='black', fg='black')
                separator_1.place(x=0, y=0, width=670, height=3)

                separator_2 = tk.Label(staff_update, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                                       bg='black', fg='black')
                separator_2.place(x=0, y=70, width=670, height=3)

                upstaff_name = tk.Label(staff_update, text="Username", font=('Bahnshcrift', 18, 'bold'), justify='center',
                                         bg='khaki', fg='black')
                upstaff_name.place(x=55, y=130, width=170, height=50)

                upstaff_name_field = tk.Entry(staff_update, textvariable=staff_name_dtype,
                                               font=('Bahnshcrift', 18, 'bold'))
                upstaff_name_field.place(x=235, y=130, width=315, height=50)

                upstaff_pass = tk.Label(staff_update, text="Password", font=('Bahnshcrift', 18, 'bold'), justify='center',
                                         bg='khaki', fg='black')
                upstaff_pass.place(x=55, y=200, width=170, height=50)

                upstaff_pass_field = tk.Entry(staff_update, textvariable=staff_pass_dtype, show='*',
                                               font=('Bahnshcrift', 18, 'bold'))
                upstaff_pass_field.place(x=235, y=200, width=315, height=50)

                upstaff_mobile = tk.Label(staff_update, text="Mobile", font=('Bahnshcrift', 18, 'bold'), justify='center',
                                           bg='khaki', fg='black')
                upstaff_mobile.place(x=55, y=270, width=170, height=50)

                upstaff_mobile_field = tk.Entry(staff_update, textvariable=staff_mobile_dtype, show='*',
                                                 font=('Bahnshcrift', 18, 'bold'))
                upstaff_mobile_field.place(x=235, y=270, width=315, height=50)

                upd_staff = partial(clicked_update, staff_name_dtype, staff_pass_dtype, staff_mobile_dtype, 'staff.db')

                up_staff_ = tk.Button(staff_update, text="Register", font=('Bahnshcrift', 19, 'bold'),
                                        command=upd_staff, bg='limegreen', bd=1, fg='black')
                up_staff_.place(x=310, y=350, width=125)

            admin_logged.withdraw()
            admin_changes_staff = tk.Toplevel(admin_logged)
            admin_changes_staff.title("Manage Staff")
            admin_changes_staff.geometry("640x480+500+200")
            admin_changes_staff.resizable(False, False)

            background = tk.Label(admin_changes_staff, text="", font=('Bahnshcrift', 22, 'bold'), justify='center',
                                  bg='gainsboro', fg='black')
            background.place(x=0, y=0, width=640, height=480)

            staff_change_header = tk.Label(admin_changes_staff, text="ADMIN-STAFF", font=('Bahnshcrift', 25, 'bold'),
                                           justify='center', bg='khaki', fg='black')
            staff_change_header.place(x=0, y=0, width=670, height=70)

            separator_1 = tk.Label(admin_changes_staff, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                                   bg='black', fg='black')
            separator_1.place(x=0, y=0, width=670, height=3)

            separator_2 = tk.Label(admin_changes_staff, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                                   bg='black', fg='black')
            separator_2.place(x=0, y=70, width=670, height=3)

            new_staff_db = tk.Button(admin_changes_staff, text="REGISTER STAFF", font=('Bahnshcrift', 18, 'bold'),
                                     command=regex_staff, bg='darkslategrey', bd=1, fg='white')
            new_staff_db.place(x=125, y=150, width=390)

            update_staff_db = tk.Button(admin_changes_staff, text="UPDATE STAFF", font=('Bahnshcrift', 18, 'bold'),
                                     command=update_staff, bg='darkslategrey', bd=1, fg='white')
            update_staff_db.place(x=125, y=250, width=390)

            staff_back = tk.Button(admin_changes_staff, text="Back", font=('Bahnshcrift', 13, 'bold'),
                                   command=back_admin_staff, bg='black', bd=0, fg='white')
            staff_back.place(x=540, y=430, width=65)

        # ----------------------- BACK TO ADMIN MAIN MENU -----------------------

        def back_to_login_admin():
            admin_logged.destroy()
            admin_win.deiconify()
            tkinter.messagebox.showinfo('Logged out', 'Logout Successfull!')

        admin_win.withdraw()
        admin_logged = tk.Toplevel(admin_win)
        admin_logged.title("ADMIN")
        admin_logged.geometry("640x480+500+200")
        admin_logged.resizable(False, False)

        background = tk.Label(admin_logged, text="", font=('Bahnshcrift', 22, 'bold'), justify='center',
                              bg='gainsboro', fg='black')
        background.place(x=0, y=0, width=640, height=480)

        admin_header = tk.Label(admin_logged, text="ADMIN", font=('Bahnshcrift', 25, 'bold'), justify='center',
                                bg='khaki', fg='black')
        admin_header.place(x=0, y=0, width=670, height=70)

        separator_1 = tk.Label(admin_logged, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                               bg='black', fg='black')
        separator_1.place(x=0, y=0, width=670, height=3)

        separator_2 = tk.Label(admin_logged, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                               bg='black', fg='black')
        separator_2.place(x=0, y=70, width=670, height=3)

        staff_db = tk.Button(admin_logged, text="STAFF DATABASE", font=('Bahnshcrift', 18, 'bold'),
                             command=change_staff, bg='darkslategrey', bd=1, fg='white')
        staff_db.place(x=125, y=190, width=390)

        admin_log_out = tk.Button(admin_logged, text="Log Out", font=('Bahnshcrift', 13, 'bold'),
                                  command=back_to_login_admin, bg='Red', bd=0, fg='white')
        admin_log_out.place(x=525, y=430, width=85)


# ----------------------- BACK TO ROOT MAIN MENU -----------------------

    def back_to_main():
        admin_win.destroy()
        root.iconify()
        root.deiconify()

    # ----------------------- ADMIN LOGIN CHECK -----------------------

    def check_admin_credentials(admin, password, database):
        conn = sqlite3.connect(database)
        c = conn.cursor()

        ADMIN = (admin.get())
        PASS = (password.get())

        command = (f"SELECT * FROM admin_login WHERE Username='{ADMIN}' AND Password='{PASS}'")

        c.execute(command)

        if len(c.fetchall()) == 1:
            login_stat = tk.Label(admin_win, text="", font=('Bahnshcrift', 12, 'bold'), justify='center',
                                  fg='red', bg='gainsboro')
            login_stat.place(x=260, y=80, width=140, height=55)

            after_admin_login()

        else:
            login_stat = tk.Label(admin_win, text="Login Failed", font=('Bahnshcrift', 12, 'bold'), justify='center',
                                  fg='red', bg='gainsboro')
            login_stat.place(x=260, y=80, width=140, height=55)

    # ----------------------- ADMIN FOREGROUNDS -----------------------

    background = tk.Label(admin_win, text="", font=('Bahnshcrift', 22, 'bold'), justify='center',
                          bg='gainsboro', fg='black')
    background.place(x=0, y=0, width=640, height=480)

    admin_header = tk.Label(admin_win, text="ADMIN LOGIN", font=('Bahnshcrift', 25, 'bold'), justify='center',
                        bg='khaki', fg='black')
    admin_header.place(x=0, y=0, width=670, height=70)

    separator_1 = tk.Label(admin_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                        bg='black', fg='black')
    separator_1.place(x=0, y=0, width=670, height=3)

    separator_2 = tk.Label(admin_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                        bg='black', fg='black')
    separator_2.place(x=0, y=70, width=670, height=3)

    # --------- Admin Username Label & Entry box ---------

    admin_name = tk.Label(admin_win, text="Admin", font=('Bahnshcrift', 18, 'bold'), justify='center',
                           bg='khaki', fg='black')
    admin_name.place(x=55, y=150, width=170, height=50)

    admin_name_field = tk.Entry(admin_win, textvariable=admin_uname_dtype, font=('Bahnshcrift', 18, 'bold'))\
        .place(x=235, y=150, width=315, height=50)

    name_separator_1 = tk.Label(admin_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    name_separator_1.place(x=50, y=147, width=503, height=3)

    name_separator_2 = tk.Label(admin_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    name_separator_2.place(x=50, y=201, width=503, height=3)

    name_separator_3 = tk.Label(admin_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    name_separator_3.place(x=50, y=148, width=3, height=53)

    name_separator_4 = tk.Label(admin_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    name_separator_4.place(x=225, y=148, width=11, height=53)

    name_separator_5 = tk.Label(admin_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    name_separator_5.place(x=550, y=148, width=3, height=53)

    # --------- Admin Password Label & Entry box ---------

    admin_pass = tk.Label(admin_win, text="Password", font=('Bahnshcrift', 18, 'bold'), justify='center',
                           bg='khaki', fg='black')
    admin_pass.place(x=55, y=220, width=170, height=50)

    admin_pass_field = tk.Entry(admin_win, textvariable=admin_pass_dtype, show='*', font=('Bahnshcrift', 18, 'bold'))\
        .place(x=235, y=220, width=315, height=50)

    pass_separator_1 = tk.Label(admin_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    pass_separator_1.place(x=50, y=217, width=503, height=3)

    pass_separator_2 = tk.Label(admin_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    pass_separator_2.place(x=50, y=271, width=503, height=3)

    pass_separator_3 = tk.Label(admin_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    pass_separator_3.place(x=50, y=218, width=3, height=53)

    pass_separator_4 = tk.Label(admin_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    pass_separator_4.place(x=225, y=218, width=11, height=53)

    pass_separator_5 = tk.Label(admin_win, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                           bg='black', fg='black')
    pass_separator_5.place(x=550, y=218, width=3, height=53)

    logged = partial(check_admin_credentials, admin_uname_dtype, admin_pass_dtype, database_admin)

    admin_login = tk.Button(admin_win, text="Login", font=('Bahnshcrift', 20, 'bold'), command=logged,
                            bg='lawngreen', bd=3, fg='black')
    admin_login.place(x=280, y=300, width=105)





    admin_back = tk.Button(admin_win, text="Back", font=('Bahnshcrift', 13, 'bold'), command=back_to_main, bg='black', bd=0,
                         fg='white')
    admin_back.place(x=540, y=430, width=65)


# ----------------------- ABOUT MESSAGE BOX -----------------------

def about_win():
    tkinter.messagebox.showinfo('About', 'Staff-Student Attendance System')

# ----------------------- CHECK VERSION MESSAGE BOX -----------------------

def check_version():
    tkinter.messagebox.showinfo('Version', 'Version: Pre-Alpha 1.0')

# Main window (root) which will be showed when software runs

root = tk.Tk()
root.geometry("640x480+500+200")
root.title("Student Attendance")
root.resizable(False, False)

background = tk.Label(root, text="", font=('Bahnshcrift', 22, 'bold'), justify='center',
                    bg='gainsboro', fg='black')
background.place(x=0, y=0, width=640, height=480)

op1_head = tk.Label(root, text="ATTENDANCE MANAGEMENT SYSTEM", font=('Bahnshcrift', 22, 'bold'), justify='center',
                    bg='khaki', fg='black')
op1_head.place(x=0, y=0, width=670, height=70)

separator_1 = tk.Label(root, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                       bg='black', fg='black')
separator_1.place(x=0, y=0, width=670, height=3)

separator_2 = tk.Label(root, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                       bg='black', fg='black')
separator_2.place(x=0, y=70, width=670, height=3)

staff_ = tk.Button(root, text="STAFF LOGIN", font=('Bahnshcrift', 18, 'bold'), command=login_staff, bg='darkslategrey',
                   bd=1, fg='white')
staff_.place(x=195, y=140, width=250)

admin_ = tk.Button(root, text="ADMIN LOGIN", font=('Bahnshcrift', 18, 'bold'), command=login_admin, bg='darkslategrey',
                   bd=1, fg='white')
admin_.place(x=195, y=240, width=250)

exit_ = tk.Button(root, text="EXIT", font=('Bahnshcrift', 13, 'bold'), command=main_destroy, bg='black', bd=0,
                     fg='white')
exit_.place(x=280, y=400, width=95)

# ----------------------- MAIN MENU BAR BUTTONS START HERE -----------------------

menu_top = tk.Menu(root)

# 1. Login menu option
in_preview = tk.Menu(menu_top, tearoff=0)
in_preview.add_command(label='Staff', command=login_staff, font=('Bahnshcrift', 9))
in_preview.add_command(label="Admin", command=login_admin, font=('Bahnshcrift', 9))
menu_top.add_cascade(label='Login', menu=in_preview)

# 2. Help menu option
in_help = tk.Menu(menu_top, tearoff=0)
in_help.add_command(label='About', command=about_win, font=('Bahnshcrift', 9))
in_help.add_command(label='Check Version', command=check_version, font=('Bahnshcrift', 9))
menu_top.add_cascade(label='Help', menu=in_help)

# 3. Exit menu option
menu_top.add_cascade(label='Exit', command=root.destroy)






# ----------------------- END OF ROOT WINDOW AND EVERYTHING -----------------------

root.config(menu=menu_top)
root.mainloop()
