a = input("Enter the sentence: ")
b = input("Enter the word to replaced: ")
c = input("Enter the new word: ")

arr = a.split(" ")
b = b.strip()
c = c.strip()
for i in arr:
    if i == b:
        i = c
    elif i == c:
        i = b
    print(i ,end=" ")
