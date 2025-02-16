# QUESTION 1

# def createList():
#     l1=[]
#     while True:
#         try:
#             n=int(input("Enter Num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1
# l1=[100, 99, 88, 77, 55, 44, 22, 11]
# l2= [89, 76, 54, 32, 10, 1]
# res=[]
# i=0
# j=0
# for k in range(len(l1)+len(l2)):
#     if i<len(l1) and j<len(l2):
#         if l1[i]>l2[j]:
#             res.append(l1[i])
#             i+=1
#         else:
#             res.append(l2[j])
#             j+=1
#     elif i<len(l1):
#         res.append(l1[i])
#         i += 1
#     elif j<len(l2):
#         res.append(l2[j])
#         j += 1
#
# print("Result: ",res)

# USING WHILE  LOOP

# def createList():
#     l1=[]
#     while True:
#         try:
#             n=int(input("Enter Num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1
# l1=[100, 99, 88, 77, 55, 44, 22, 11]
# l2= [89, 76, 54, 32, 10, 1]
# res=[]
# i=0
# j=0
#
# while i<len(l1) and j<len(l2):
#     if l1[i]>l2[j]:
#         res.append(l1[i])
#         i+=1
#     else:
#         res.append(l2[j])
#         j+=1
#
# while i<len(l1) or j<len(l2):
#     if i<len(l1):
#         res.append(l1[i])
#         i += 1
#     else:
#         res.append(l2[j])
#         j += 1
#
# print("Result: ",res)





# QUESTION 2

# def createList():
#     l1=[]
#     while True:
#         try:
#             n=int(input("ENter Num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1
# # l1=createList()
# # l2=createList()
# l1=[100, 99, 88, 77, 55, 44, 22, 11]
# l2= [89, 76, 54, 32, 10, 1]
# res=[]
# i=len(l1)-1
# j=len(l2)-1
# for k in range(len(l1)+len(l2)):
#     if i>=0 and j>=0:
#         if l1[i]>l2[j]:
#             res.append(l2[j])
#             j-=1
#         else:
#             res.append(l1[i])
#             i-=1
#     elif i>=0:
#         res.append(l1[i])
#         i -= 1
#     elif j>=0:
#         res.append(l2[j])
#         j -= 1
#
# print("Result : ",res)


# USING WHILE LOOP

# def createList():
#     l1=[]
#     while True:
#         try:
#             n=int(input("ENter Num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1
# # l1=createList()
# # l2=createList()
# l1=[100, 99, 88, 77, 55, 44, 22, 11]
# l2= [89, 76, 54, 32, 10, 1]
# res=[]
# i=len(l1)-1
# j=len(l2)-1
# while i>=0 and j>=0:
#     if l1[i]>l2[j]:
#         res.append(l2[j])
#         j-=1
#     else:
#         res.append(l1[i])
#         i-=1
# while i>=0 or j>=0:
#     if i>=0:
#         res.append(l1[i])
#         i -= 1
#     elif j>=0:
#         res.append(l2[j])
#         j -= 1
#
# print("Result : ",res)


#  QUESTION 3

# def createList():
#     l=[]
#     while True:
#         try:
#             n=int(input("Enter Num: "))
#             l.append(n)
#         except Exception as e:
#             break
#     return l
# l1=createList()
# l2=createList()
# # l1 = [1, 22, 23, 45, 56, 67]
# # l2 = [82, 67, 53, 35, 20, 6, 4, 2, 0]
# res=[]
# i=0
# j=len(l2)-1
# for k in range(len(l1)+len(l2)):
#     if i<len(l1) and j>=0:
#         if l1[i]>l2[j]:
#             res.append(l2[j])
#             j-=1
#         else:
#             res.append(l1[i])
#             i+=1
#     elif i<len(l1):
#         res.append(l1[i])
#         i += 1
#     elif j>=0:
#         res.append(l2[j])
#         j -= 1
# print("Result : ",res)


#  using WHILE LOOP

def createList():
    l=[]
    while True:
        try:
            n=int(input("Enter Num: "))
            l.append(n)
        except Exception as e:
            break
    return l
# l1=createList()
# l2=createList()
l1 = [1, 22, 23, 45, 56, 67]
l2 = [82, 67, 53, 35, 20, 6, 4, 2, 0]
res=[]
i=0
j=len(l2)-1
while i<len(l1) and j>=0:
    if l1[i]>l2[j]:
        res.append(l2[j])
        j-=1
    else:
        res.append(l1[i])
        i+=1
while i<len(l1) or j>=0:
    if i<len(l1):
        res.append(l1[i])
        i += 1
    elif j>=0:
        res.append(l2[j])
        j -= 1
print("Result : ",res)
