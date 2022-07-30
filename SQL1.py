import mysql.connector as p

mydb = p.connect(host="localhost" ,  user= "root" , passwd ="Sadhguru501$")
cursor = mydb.cursor()
cursor.execute("insert into imp.details1 values(101 , 'Uday' , 'uday@123' , 1000 , 30)")
mydb.commit()
cursor.execute("select * from imp.details1")
for i in cursor.fetchall():
    print(i)