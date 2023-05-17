f1 = open("sample.txt",'r')
f2 = open("new.txt",'w')

for i in f1:
    f2.write(i)
f2.close()
f3 = open("new.txt",'r')
print(f3.read())
