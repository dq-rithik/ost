import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database ="ostlab"
)

mycursor = mydb.cursor()

sql = '''CREATE TABLE students (regno INT PRIMARY KEY , name VARCHAR(255) , age INT, gender VARCHAR(255), department VARCHAR(255), ph VARCHAR(255),cgpa INT)'''

mycursor.execute(sql)