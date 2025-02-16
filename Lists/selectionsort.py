def createList():
    l=[]
    while True:
        try:
            n=int(input("Enter Num: "))
            l.append(n)
        except Exception as e:
            return l
l=createList()
# l=[5,3,4,1,2]
#
# def selectionSortAsc(l):
#     actual = len(l) - 1
#     for i in range(len(l) - 1):
#         maxval = -2847483648
#         maxi = -1
#         for j in range(0, len(l) - i):
#             if l[j] > maxval:
#                 maxval = l[j]
#                 maxi = j
#         l[maxi], l[actual] = l[actual], l[maxi]
#         actual -= 1
#     return l
#
# def selectionSortDesc(l):
#     actual = len(l) - 1
#     for i in range(len(l) - 1):
#         minval = 2847483648
#         maxi = -1
#         for j in range(0, len(l) - i):
#             if l[j] < minval:
#                 minval = l[j]
#                 maxi = j
#         l[maxi], l[actual] = l[actual], l[maxi]
#         actual -= 1
#     return l
#
#
# print("Ascending : ",selectionSortAsc(l))
# print("Descending: ",selectionSortDesc(l))


n=len(l)
for i in range(0,n-1):
    actualind=n-i-1
    maxind=-1
    maxval=-2847483648
    for j in range(0,n-i):
        if maxval<l[j]:
            maxval=l[j]
            maxind=j
    l[actualind],l[maxind]=l[maxind],l[actualind]
print(l)