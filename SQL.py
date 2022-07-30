import mysql.connector as c

mydb = c.connect(host = "localhost" , user = "root" , passwd = "Sadhguru501$")
cursor = mydb.cursor()
#cursor.execute("create database imp")
#cursor.execute("show databases")
#s = "create table imp.details1(employee_id int(10) , emp_name varchar(80) , emp_mailid varchar(20) , emp_salary int(6) , emp_attendance int(3))"
#q1 = cursor.execute(s)
q2 = cursor.execute("select * from imp.details1")
print(q2)

