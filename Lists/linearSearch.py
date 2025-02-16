# WAP TO IMPLEMENT THE LINEAR SEARCH ON A GIVEN LIST TO FIND THE TARGET ELEMENT
from jedi.inference.value.iterable import ListComprehension

# def createList():
#     l1=[]
#     while True:
#         try:
#             n=int(input("Enter Num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1

# def linearSearch(l,target):
#     for i in range(0, len(l)):
#         if l[i] == target:
#             return True
#     return False

# l=createList()
# target=int(input("Enter the Number to be Searched: "))
# flag=linearSearch(l,target)
#
# if flag:
#     print("Target Element Found ")
# else:
#     print("Target Element Not Found ")


# WAP TO IMPLEMENT THE LINEAR SEARCH ON A GIVEN LIST TO FIND THE TARGET ELEMENT INDEX VALUE

# def createList():
#     l1=[]
#     while True:
#         try:
#             n=int(input("Enter Num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1

# def linearSearch(l,target):
#     for i in range(0, len(l)):
#         if l[i] == target:
#             return i
#     return -1

# l=createList()
# target=int(input("Enter the Number to be Searched: "))
# flag=linearSearch(l,target)
# if flag!=-1:
#     print("Element Found at: ",flag)
# else:
#     print("Element Not Found ")


# WAP TO REVERSE THE GIVEN ARRAY

# def createList():
#     l1=[]
#     while True:
#         try:
#             n=int(input("Enter Num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1
#
# def reverse(l,start,end):
#     while start < end:
#         l[start],l[end]=l[end],l[start]
#         start += 1
#         end -= 1
#     return l
#
# l=createList()
# print("Reversed List: ",reverse(l,0,len(l)-1))



# WAP TO FIND THE DUPLICATES ,NON-DUPLICATES AND UNIQUE VALUES USING DICTIONARY

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
# dict={}
# for i in range(len(l)):
#     if l[i] not in dict.keys():
#         dict[l[i]]=1
#     else:
#         dict[l[i]]=dict[l[i]]+1
#
# nondup=[]
# dup=[]
# unique=[]
# for i in range(len(dict)):
#     key=list(dict.keys())
#     if dict[key[i]]>=1:
#         nondup.append(key[i])
#     if dict[key[i]]>1:
#         dup.append(key[i])
#     else:
#         unique.append(key[i])
#
# print("Duplicates: ",dup)
# print("Non Duplicates: ",nondup)
# print("Unique: ",unique)

# OR------------------

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
# dict={}
# nondup=[]
# dup=[]
# unique=[]
# for i in range(len(l)):
#     if dict.get(l[i]) is None:
#         dict[l[i]]=1
#     else:
#         dict[l[i]]=dict[l[i]]+1
#
# for key,val in dict.items():
#     nondup.append(key)
#     if val>1:
#         dup.append(key)
#     else:
#         unique.append(key)
#
# print("Duplicates: ",dup)
# print("Non Duplicates: ",nondup)
# print("Unique: ",unique)

# WAP TO ACCEPT A DYNAMIC LIST FROM THE USER AND DISPLAY THE FOLLOWING :
# 1.MAXIMUM VALUE 2. INDEX OF MAXIMUM VALUE 3.MINIMUM VALUE 4.INDEX OF MINIMUM VALUE

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
#
# max=-2147483648
# maxindex=-1
# min=2147483648
# minindex=-1
# for i in range(len(l)):
#     if l[i]>max:
#         max=l[i]
#         maxindex=i
#     if l[i]<min:
#         min=l[i]
#         minindex=i
#
# print("List: ",l)
# print("Maximum Value: ",max)
# print("Maximum Value Index: ",maxindex)
# print("Minimum Value: ",min)
# print("Minimum Value Index: ",minindex)

# SORTCOLORS ON LEETCODE