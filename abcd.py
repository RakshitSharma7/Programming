# 1.Armstrong   ------------>
# 2.Count DIGITS    --------->
# 3. EvenODd    ---------->
# 4. GCD LCM    ---------->
# 5. Leap Year  ------------->
# 6. Palindrome ------------->
# 7. Perfect Number ---------->
# 8.Prime Number    ----------->
from itertools import count
from os import remove

from typing_extensions import assert_never

# REcurssion
# 1. ARMSTRONG ------->
# 2. FACTORIAL -------->
# 3. NATURAL -> a. SUM OF N NUMBERS  b.SUM OF DIGITS  c. COUNT DIGIT ------------>
# 4. PALINDROME -------->
# 5. REVERSENUMBER -------->
# 6. HAPPY NUMBER  -------->
# 7. FIBONACCI NUMBER  --------->

# def maxArea(height):
#     start = 0
#     end = len(height) - 1
#     area=[]
#     maxi=0
#     if end>start:
#         while start < end:
#             mini=min(height[start],height[end])
#             d=end-start
#             area.append(mini*d)
#             start+=1
#         print(area)
#         for i in area:
#             if maxi<i:
#                 maxi=i
#     return maxi
#
#
# height = [8,7,2,1]
# ans=maxArea(height)
# print(ans)
# [3,3,5,5,6,7]
# l=[1,3,-1,-3,5,3,6,7,8,9]
# out=[]
# n=int(input("Enter the Range: "))
# s=0
# while s<len(l)-n+1:
#     max=-10
#     for i in range(s,s+n):
#         if l[i]>max:
#             max=l[i]
#     out.append(max)
#     s+=1
# print(out)

# l=[1,1,1,1,1]
# out=[]
# n=int(input("ENter the number: "))
# start=0
# i=0
# while start<n:
#     out.append([l[i],l[i+1]])
#     start+=1
# print(out)

# def check(nums):
#     l = nums
#     start = 0
#     n1 = len(l) - 1
#     flag = True
#     if len(nums) == 1 or len(nums) == 2:
#         return True
#     while start <= n1:
#         for i in range(n1):
#             if l[i] > l[i + 1]:
#                 flag = False
#                 break
#         if flag:
#             return True
#         n = len(l) - 1
#         temp = l[n]
#         while n > 0:
#             l.pop(n)
#             l.insert(n, l[n - 1])
#             n -= 1
#         l[0] = temp
#         start += 1
#     return False
#
# ans=check([9,1,3,4])
# # print(ans)
# n=3
# l=[1,1,1]
# k=3
# sub=[]
# res=[]
# for i in range(n):
#     for j in range(i+1,n+1):
#         sub.append(l[i:j])
# for i in sub:
#     sum=0
#     for v in i:
#         sum+=v
#     if sum==k:
#         res.append(i)
#


# n=int(input("Enter the Number: "))
#
# def countDigit(n):
#     count=0
#     while n != 0:
#         count += 1
#         n = n // 10
#     return count
#
# def checkArm(n,count):
#     sum=0
#     temp=n
#     while n != 0:
#         rem = n % 10
#         sum = sum + (rem ** count)
#         n //= 10
#     return temp==sum
#
# pow=countDigit(n)
# flag=checkArm(n,pow)
#
# if flag:
#     print("ArmSTrong Num")
# else:
#     print("Not ArmsTrong")



n=int(input("Enter the Number: "))
noc=n*2
for i in range(1,n+1):
    for j in range(1,n*2+2):
        if (i==1 and j!=n+1) or (i==n and j<n+1 and j!=n+1) or j==1 or j==n or j==noc:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    noc-=1

