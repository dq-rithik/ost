tup = ((1,2,3),(4,5,6),(7,8,9))
li = []
for i in tup:
    sum = 0
    for j in i:
        sum += j
    li = sum
    print(li)
