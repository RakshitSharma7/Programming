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