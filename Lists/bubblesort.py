def createList():
    l=[]
    while True:
        try:
            n=int(input("Enter Num: "))
            l.append(n)
        except Exception as E:
            break
    return l
# l=[5,4,3,2,1]

def bubblesortasc(l,n):
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                l[j + 1], l[j] = l[j], l[j + 1]
    return l

def bubblesortdesc(l,n):
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if l[j] < l[j + 1]:
                l[j + 1], l[j] = l[j], l[j + 1]
    return l

l=createList()
n=len(l)
print("Ascending : ",bubblesortasc(l,n))
print("Descending : ",bubblesortdesc(l,n))
