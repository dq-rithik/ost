li = []
y = 1
while y:
    print("1. Integer\n2.Char\n3.String\n4.float")
    x = int(input("Enter the choice: "))
    if(x == 1):
        a = int(input("Enter the value: "))
        li.append(a)
    if(x == 2):
        a = input("Enter the value: ")
        li.append(a)
    if(x == 3):
        a = str(input("Enter the value: "))
        li.append(a)
    if(x == 4):
        a = float(input("Enter the value: "))
        li.append(a)
    print(li[:])
    y = int(input("Press 1 to contine: "))

