# WAP TO DISPLAY THE SUM OF ALL THE VALUES IN A GIVEN ARRAY

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
# def arraySum(l):
#     sum=0
#     for i in l:
#         sum+=i
#     return sum

# l=createList()
# res=arraySum(l)
# print(res)

# WAP TO DISPLAY THE DIFFERENCE OF PRODUCT AND SUM OF ALL THE VALUES IN A GIVEN ARRAY

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
# def diffProductSum(l):
#     sum=0
#     prod=1
#     for i in l:
#         sum+=i
#         prod*=i
#     return prod-sum
#
# l=createList()
# res=diffProductSum(l)
# print(res)


# WAP TO REVERSE THE GIVEN LIST USING RECURSION

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
#     if start>end:
#         return l
#     l[start],l[end]=l[end],l[start]
#     return reverse(l,start+1,end-1)
#
# l=createList()
# print("Reversed List: ",reverse(l,0,len(l)-1))

# WAP TO ROTATE A CUSTOMIZED LIST TOWARDS THE LEFT SIDE K NUMBER OF TIMES
# constraints
# 1<=len(arr)<= 10**5
# 1<= arr[i] <= 10**5
# 0<=k<=10**5

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
#
# def reverse(l,start,end):
#     if start>end:
#         return l
#     l[start],l[end]=l[end],l[start]
#     return reverse(l,start+1,end-1)
#
# l=createList()
# k=int(input("Enter the Number of Rotation: "))
# reverse(l,0,len(l)-1)
# reverse(l,0,k-1)
# reverse(l,k,len(l)-1)
# print(l)

# l=[40,30,20,10]

# for i in range(1,len(l)):
#     key=l[i]
#     j=i-1
#     while j>=0 and key<l[j]:
#         l[j+1]=l[j]
#         j-=1
#     l[j+1]=key
#
# print(l)

# m=3
# n=3
# nums1=[1,2,3,0,0,0]
# nums2=[2,5,6]
# i=0
# j=0
# for k in range(m+n):
#     if i<m and j<n:
#         if nums1[i]>nums2[j]:
#             nums1.insert(k,nums2[j])
#             j+=1
#             nums1.pop(-1)
#                     # k+=1
#         else:
#             i+=1
#                     # k+=1
#     elif i<m:
#         i+=1
#                 # k+=1
#     elif j<n:
#         nums1.insert(k,nums2[j])
#         nums1.pop(-1)
#         j+=1
# print(nums1)


# WAP TO DISPLAY ALL THE SUB ARRAYS OF THE GIVEN INPUT ARRAY WITHOUT USING ANY INBUILT-FUNCTION

# ARR=[1,2,3,4,5]

# SUB-ARRAY : [1,2],[2,3,4],[4,5]
# SUB-SEQUENCE : [1,5],[2,4],[1,3,4]


# def createList():
#     l1=[]
#     while True:
#         try:
#             n=int(input("Enter Num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1
# L=createList()
# res=[]
# for i in range(len(L)):
#     for j in range(i+1,len(L)+1):
#         if L[i:j] not in res and L[i:j]!=[]:
#             res.append(L[i:j])
# print(res)


# def createList():
#     l1=[]
#     while True:
#         try:
#             n=int(input("Enter Num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1
# L=createList()
# for i in range(len(L)):
#     res=[]
#     for j in range(i,len(L)):
#         res.append(L[j])
#         print(res)

