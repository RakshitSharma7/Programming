def createList():
    l=[]
    while True:
        try:
            n=int(input("Enter Num: "))
            l.append(n)
        except Exception as e:
            break
    return l

def insertionsortasc(l,n):
    for i in range(0, n - 1):
        for j in range(i + 1, 0, -1):
            if l[j] < l[j - 1]:
                l[j - 1], l[j] = l[j], l[j - 1]
    return l

def insertionsortdesc(l,n):
    for i in range(0, n - 1):
        for j in range(i + 1, 0, -1):
            if l[j] > l[j - 1]:
                l[j - 1], l[j] = l[j], l[j - 1]
    return l

l=createList()
n=len(l)
print("Ascending Sort: ",insertionsortasc(l,n))
print("Descending Sort: ",insertionsortdesc(l,n))