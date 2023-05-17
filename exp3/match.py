dict1 = {1:'a',2:'b',3:'c',4:'d',5:'e'}
dict2 = {1:'a',2:'c',3:'g',4:'d',5:'e'}

for i in dict1.items():
    for j in dict2.items():
        if i == j:
            print(i)
1