def perm(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remList = lst[:i] + lst[i + 1:]
        for p in perm(remList):
            l.append([m] + p)
    return l

data = list('abc')
for p in perm(data):
    print(p)