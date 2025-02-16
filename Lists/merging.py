# WAP TO MERGE THE GIVEN TWO LIST

# Different ways of merging
# l1=[1,3,5,8]
# l2=[10,20,30]
# o/p: [1,3,5,8,10,20,30]

# 1. extend()
# 2. concatenate
# 3. append(): by appending one by one
# 4. insert()

# def createList():
#     l1=[]
#     while True:
#         try:
#             n=int(input("Enter Num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1
# l=createList()
# l1=createList()
# print("LIST 1: ",l)
# print("LIST 2: ",l1)

# 1. EXTEND FUNCTION
# l.extend(l1)
# print(l)


# 2. CONCATENATE "+"
# l2=l+l1
# print(l2)
# print("ID l: ",id(l))
# print("ID l1: ",id(l1))
# print("ID l2: ",id(l2))

# 3. append

# for i in l1:
#     l.append(i)
# print(l)

# 4. INSERT

# for i in l1:
#     l.insert(len(l),i)
# print(l)

# WRITE A PROGRAM TO MERGE THE GIVEN TWO LIST IN ALTERNATIVE INDEX ------(try block)

# L=[1,3,5]
# L1=[2,4,6,8,10,12]
# l3=[]
# flag1=True
# flag2=True
# i=0
# while flag1 or flag2:
#     try:
#         l3.append(L[i])
#     except Exception as e:
#         flag1=False
#     try:
#         l3.append(L1[i])
#     except Exception as e:
#         flag2=False
#     i+=1
# print(l3)



# WRITE A PROGRAM TO MERGE THE GIVEN TWO LIST IN ALTERNATIVE INDEX

# def createList():
#     l1=[]
#     while True:
#         try:
#             n=int(input("Enter Num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1
# l1=createList()
# l2=createList()
# print("List1: ",l1)
# print("List2: ",l2)
# res=[]
# i=0
# j=0
# k=0
# for k in range(len(l1)+len(l2)):
#     if i<len(l1) and k%2==0:
#         res.append(l1[i])
#         i+=1
#         # k+=1
#     elif j<len(l2) and k%2!=0:
#         res.append(l2[j])
#         j+=1
#         # k+=1
#     else:
#         if j<len(l2):
#             res.append(l2[j])
#             j += 1
#             # k += 1
#         elif i<len(l1):
#             res.append(l1[i])
#             i += 1
#             # k += 1
# print("Resultant List: ",res)


# WRITE A PROGRAM TO MERGE THE GIVEN TWO LIST IN ALTERNATIVE INDEX USING INSERT FUNCTION

# def createList():
#     l1=[]
#     while True:
#         try:
#             n=int(input("Enter Num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1
# l1=createList()
# l2=createList()
# print("List1: ",l1)
# print("List2: ",l2)
#
# j=0
# k=1
#
# for j in range(len(l2)):
#     l1.insert(k,l2[j])
#     k+=2
#
# print("Resultant List: ",l1)


# note input in ascending order Output also expected in ascending order

# l1=[]
# l2=[]
# res=[]
# i=0
# j=0
# for k in range(len(l1)+len(l2)):
#     if i<len(l1) and j<len(l2):
#         if l1[i]<l2[j]:
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
# print("Resultant List: ",res)


# GIVEN TWO ASCENDING ORDER 2 LIST MERGE THE LIST DISPLAY THE OUTPUT IN DESCENDING ORDER

# def createList():
#     l1=[]
#     while True:
#         try:
#             n=int(input("Enter Num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1
# l1=createList()
# l2=createList()
# res=[]
# i=len(l1)-1
# j=len(l2)-1
# for k in range(len(l1)+len(l2)):
#     if i>=0 and j>=0:
#         if l1[i]<l2[j]:
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
# print("Resultant List: ",res)


# GIVEN TWO DESCENDING ORDER LIST MERGE IT DISPLAY IN ASCENDING ORDER

# def createList():
#     l1=[]
#     while True:
#         try:
#             n=int(input("Enter Num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1
# l1=createList()
# l2=createList()
# i=len(l1)-1
# j=len(l2)-1
# res=[]
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
# print("Resultant List: ",res)



# GIVEN TWO DESCENDING ORDER LIST MERGE IT DISPLAY IN DESCENDING ORDER

# def createList():
#     l1=[]
#     while True:
#         try:
#             n=int(input("Enter Num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1
# l1=createList()
# l2=createList()
# i=0
# j=0
# res=[]
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
#         i+=1
#     elif j<len(l2):
#         res.append(l2[j])
#         j += 1
# print("Resultant List: ",res)

