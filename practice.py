# Perfect Number
from itertools import count

# n=int(input("Enter the Number: "))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("Yes")
# else:
#     print("No")


#  Using Function

# n=int(input("Enter the Number: "))
# def perfectNumber(n):
#     sum = 0
#     for i in range(1, n):
#         if n % i == 0:
#             sum += i
#     return sum==n
#
# flag=perfectNumber(n)
# if flag:
#     print("Perfect Number")
# else:
#     print("Not Perfect Number")


# User Defined Range

# sr=int(input("Enter the Starting Range: "))
# er=int(input("Enter the Ending Range: "))
#
# def perfectNumber(n):
#     sum = 0
#     for i in range(1, n):
#         if n % i == 0:
#             sum += i
#     return sum==n
#
# for i in range(sr,er+1):
#     if sr>er:
#         print("Invalid Range")
#     else:
#         flag=perfectNumber(i)
#         if flag:
#             print(i,"is Perfect Number")


# LCM

# n1=int(input("Enter the Number1: "))
# n2=int(input("Enter the Number2: "))

# flag=True
# i=2
# while flag:
#     if i%n1==0 and i%n2==0:
#         flag=False
#         break
#     i=i+1
# print(i)

# Using Function

# n1=int(input("Enter the Number1: "))
# n2=int(input("Enter the Number2: "))
#
# def lcm(x,y):
#     flag = True
#     i = 1
#     while flag:
#         if i % x == 0 and i % y == 0:
#             return i
#         i = i + 1
#
# res=lcm(n1,n2)
# print(res)


#using FOR Loop

# n1=int(input("Enter the Number1: "))
# n2=int(input("Enter the Number2: "))
#
# if n1>n2:
#     grt=n1
# else:
#     grt=n2
#
# for i in range(grt,(n1*n2)+1):
#     if i%n1==0 and i%n2==0:
#         res=i
#         break
#
# print(res)




# GCD

# n1=int(input("Enter the Number1: "))
# n2=int(input("Enter the Number2: "))
# ans=-1
# if n1>n2:
#     smallest=n2
# else:
#     smallest=n1
#
# for i in range(1,(smallest//2)+1):
#     if n1%i==0 and n2%i==0:
#         ans=i
#
# print(ans)

# Using Function

# n1=int(input("Enter the Number1: "))
# n2=int(input("Enter the Number2: "))
#
# def gcd(x,y):
#     ans = -1
#     if n1 > n2:
#         smallest = n2
#     else:
#         smallest = n1
#     for i in range(1, (smallest // 2) + 1):
#         if n1 % i == 0 and n2 % i == 0:
#             ans = i
#     return ans
#
# res=gcd(n1,n2)
# print(res)


# EvenOdd

# sr=int(input("ENter the Number: "))
# er=int(input("Enter the Number: "))
#
# def evenOdd(n):
#     return n%2==0
#
# if sr<er:
#     for i in range(sr, er + 1):
#         flag = evenOdd(i)
#         if flag:
#             print("Even")
#     for i in range(sr, er + 1):
#         flag = evenOdd(i)
#         if not flag:
#             print("Odd")
#
# else:
#     print("Invalid Range")


# Count DIgits

# sr= int(input("Enter the Start Range: "))
# er=int(input("Enter the End Range: "))
#
# def countDigit(n):
#     count = 0
#     while n != 0:
#         count += 1
#         n = n // 10
#     return count
#
# if sr>er:
#     print("Invalid")
# else:
#     for i in range(sr, er + 1):
#         ans = countDigit(i)
#         print(ans)



#ArmStrong Number

# sr=int(input("Enter the Number: "))
# er=int(input("Enter the End: "))
#
#
# def countDigit(n):
#     count = 0
#     while n != 0:
#         count += 1
#         n = n // 10
#     return count
#
# def checkArmstrong(n):
#     temp=n
#     ans = 0
#     while n != 0:
#         rem = n % 10
#         ans = ans + (rem ** pow)
#         n = n // 10
#     return temp==ans
#
# if sr>er:
#     print("Invalid ")
# else:
#     for i in range(sr,er+1):
#         pow = countDigit(i)
#         ans = checkArmstrong(i)
#         if ans:
#             print(i,"Armstrong")


# n=int(input("ENter the Year: "))
#
# def checkLeap(n):
#     return n%400==0 or (n%100!=0 or n%4==0)
#
# flag=checkLeap(n)
# if flag:
#     print("Leap")
# else:
#     print("Not Leap")


