import string
alphabet = list(string.ascii_lowercase)

f = open("sample.txt",'w')
x = 0
for i in alphabet:
    if x % 3 == 0:
        f.write("\n")
    f.write(i)
    x  +=1
f.close()

fo = open("sample.txt",'r')
print(fo.read())