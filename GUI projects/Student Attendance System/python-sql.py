import sqlite3
conn = sqlite3.connect('student_attendance.db')
c = conn.cursor()

# Creating table 'student_att' inside 'student_attendance' database
# c.execute("""CREATE TABLE student_att(Name text, PRN text, Department text, Division text, Attendance integer, Month text)""")
# c.execute("INSERT INTO student_att VALUES ('Sam', 'S001', 'Computer', 'A', 16, 'June')")

def insert_student_record(s_name, s_prn, s_dept, s_div, s_att, att_month):
    if len(s_name)==0 or len(s_prn)==0 or len(s_dept)==0 or len(s_div)==0 or len(str(s_att))==0 or len(att_month)==0:
        print("1 or more field are missing!")
    else:
        with conn:
            c.execute("INSERT INTO student_att VALUES (:Name,:PRN,:Department,:Division,:Attendance,:Month)", {
                'Name': s_name,
                'PRN': s_prn,
                'Department': s_dept,
                'Division': s_div,
                'Attendance': s_att,
                'Month': att_month
            })

def view_student_att(s_prn, att_month):
    if att_month.upper() == 'ALL':
        with conn:
            c.execute("Select * FROM student_att WHERE PRN=:PRN", {'PRN': s_prn})
            att_list = c.fetchall()
            for i in att_list:
                print(i)

    else:
        with conn:
            c.execute("Select * FROM student_att WHERE PRN=:PRN AND MONTH=:MONTH", {
                'PRN': s_prn,
                'MONTH': att_month
            })
            print(c.fetchall())

ext = 0
while ext != 1:
    print("1 - Insert student records\n2 - View student record\n3 - Exit")
    user_choice = int(input("Enter your Choice: "))

    if user_choice == 1:
        s_name = input("Enter student name: ")
        s_prn = input("Enter student prn: ")
        s_dept = input("Enter student department: ")
        s_div = input("Enter student division: ")
        s_att = int(input("Enter attendance: "))
        att_month = input("Enter month of attendance: ")

        insert_student_record(s_name, s_prn, s_dept.upper(), s_div.upper(), s_att, att_month.upper())

    elif user_choice == 2:
        s_prn = input("Enter student PRN: ")
        print("Type ALL to get all months.")
        att_month = input("Enter month of attendance: ")
        view_student_att(s_prn, att_month.upper())

    else:
        ext += 1





conn.commit()
conn.close()