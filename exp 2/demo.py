demo = [1,2,5,10,20,50,100,200,500,2000]

a = int(input("Enter the amount: "))
demo.reverse()
sum = 0
rem = a
for i in demo:
   n = 0
   if i<=a and rem != 0:
        n = rem//i
        sum += (n)*i
        rem = a - sum
        print(str(i) + "*" + str(n))