from string import ascii_letters

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end="")
#     print()

# str="PENTAGON"
#
# for i in range(len(str)):
#     for j in range(i+1):
#         print(str[j],end=" ")
#     print()


# n=int(input("Enter the Number: "))
# n1,n2=0,1
# for i in range(n):
#     for j in range(i+1):
#         print(n2,end=" ")
#         n3=n1+n2
#         n1=n2
#         n2=n3
#     print()

# ****
# ***
# **
# *

# n=4
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print("*",end="")
#     print()

# 4
# n=int(input("Enter the Number: "))
#
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print("*",end="")
#     print()

# 5
# n= int(input("ENter the Num: "))
#
# for i in range(1,n+1):
#     for k in range(i):
#         print(" ",end="")
#     for j in range(n,i-1,-1):
#         print("*",end="")
#     print()

# n= int(input("ENter the Num: "))
#
# for i in range(1,n+1):
#     for k in range(i):
#         print(" ",end="")
#     for j in range(n,i-1,-1):
#         print("*",end=" ")
#     print()


# n= int(input("Enter the Number: "))
# for i in range(1,n+1):
#     for k in range(1,i):
#         print(" ",end="")
#     for j in range(i,n+1):
#         print("*",end=" ")
#     print()

# n=int(input("Enter the Number: "))
# for i in range(1,n+1):
#     for k  in range(n,i,-1):
#         print("",end="")
#     for j in range(1,n*i,2):
#         print("*",end="")
#     print()

# n=int(input("Enter the number: "))
# odd=n*2-1
# # for a in range(1,n):
# #     odd=odd+2
# for i in range(1,n+1):
#     for k in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,odd+1):
#         print("*",end=" ")
#     print()
#     odd-=2


# n=int(input("Enter the number: "))
# odd=1
# for i in range(1,n+1):
#     for k in range(1,i):
#         print(" ",end=" ")
#     for j in range((n*2)-1,odd-1,-1):
#         print("*",end=" ")
#     print()
#     odd+=2

n=4
# for i in range(1,n+1):
#     for j in range(n,n-i,-1):
#         print("*",end="")
#     print()

# for i in range(1,n+1):
#     for k in range(1,n-i+1):
#         print(" ",end="")
#     for j in range(n-i+1,n+1):
#         print("*",end=" ")
#     print()

# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print("*",end="")
#     print()
odd=1
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,odd+1):
        print("*",end=" ")
    print()
    odd+=2