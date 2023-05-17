import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "123",
    database = "ostlab"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM students"
mycursor.execute(sql)
res = mycursor.fetchall()

for x in res:
    print(x)