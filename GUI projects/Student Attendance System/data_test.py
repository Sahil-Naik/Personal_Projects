import sqlite3
database = 'staff.db'
table = 'student_att'
conn = sqlite3.connect(database)
c = conn.cursor()


# Creating table 'student_att' inside 'student_attendance' database
# c.execute("""CREATE TABLE student_att(Name text, PRN text, Department text, Division text, Attendance integer, Month text)""")

c.execute("SELECT * FROM staff_login")
#c.execute("INSERT INTO admin_login VALUES('a','a',123)")
print(c.fetchall())



conn.commit()
conn.close()