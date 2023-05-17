import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "123",
    database = "ostlab"
)

while True:
    cursor = mydb.cursor()
    print("\n1.Insert\n2.Delete\n3.Display\n4.Exit")
    ch = int(input("\nEnter the choice: "))
    if ch == 1:
        reg = int(input("\nEnter the Register Number: "))
        name = input("Enter the Name: ")
        age = input("Enter the Age: ")
        gender = input("Enter Gender: ")
        department = input("Enter the Department: ")
        ph = input("Enter the Phone Number: ")
        cgpa = input("Enter the CGPA: ")
        sql = "insert into students values(%s,%s,%s,%s,%s,%s,%s)"
        val = (reg,name,age,gender,department,ph,cgpa)
        cursor.execute(sql,val)
        mydb.commit()
        print("Inserted Successfully!")
        print()

    elif ch == 2:
        a = int(input("Enter the Register number: "))
        sql = "delete from students where regno = %s"
        value = (a,)
        cursor.execute(sql,value)
        mydb.commit()
        print("Record deleted!")
    
    elif ch == 3:
        cursor.execute("select * from students")
        res = cursor.fetchall()
        print("Records\n")
        for i in res:
            print(i)
    elif ch == 4:
        cursor.close()
        mydb.close()
        break
    else:
        print("Wrong input!")