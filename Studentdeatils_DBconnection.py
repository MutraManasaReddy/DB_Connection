import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Manasa@123",
    database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
print("create successfully")

mycursor.execute("SHOW DATABSE")
for x in mycursor:
    print(x)


#create student table
mycursor.execute("CREATE TABLE student(name VARCHAR(222), rollno VARCHAR(200), school_name VARCHAR(333))")
mycursor.execute("SHOW TABLE")
for x in mycursor:
    print(x)

# insert the values
sql = "INSERT INTO STUDENT(name, rollno, school_name) VALUES(%s,%s,%s)"
val = ("manasa","10","Dehli public school")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record insert")

mycursor.execute("SELETE * FROM STUDENT")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

sql = ("UPDATE STUDENT SET rollno = '20' WHERE rollno = 'rollno 200 ") 
mycursor.execute(sql)
mydb.commit()
print(mycursor.execute,"update record")


sql = ("DELETE STUDENT WHERE rollno = '20'")
mycursor.execute(sql)
mydb.commit()
print(mycursor.execute,"delete record")


 