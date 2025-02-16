# WAP to check whether the given number is a prime number or not  ----> Important


# n= int(input("Enter the num: "))
# flag=True
#
# if n<=1:
#     print("Not a Prime Number!!")
# else:
#     for i in range(2, (n//2)+1):
#         if n % i == 0:
#             flag = False
#             break
#
#     if flag:
#         print("Prime Number")
#     else:
#         print("Not Prime Number")



# WAP to check whether the given number is a prime number Using Function  ----> Important


# num=int(input("Enter the Number: "))
# def checkPrime(n):
#     if n<=1:
#         return False
#     else:
#         for i in range(2, (n//2)+1):
#             if n % i == 0:
#                 return False
#         return True
#
# flag=checkPrime(num)
# if flag:
#     print("Prime Number ")
# else:
#     print("Not Prime Number ")



# WAP to check whether the given number is a prime number in user defined Range
#
# sr=int(input("Enter the Starting Range: "))
# er=int(input("Enter the Ending Range: "))
# def checkPrime(n):
#     if n<=1:
#         return False
#     else:
#         for i in range(2, (n//2)+1):
#             if n % i == 0:
#                 return False
#         return True
#
# for i in range(sr,er+1):
#     if sr>er or sr<=1:
#         print("Invalid Range")
#         break
#     else:
#         flag=checkPrime(i)
#         if flag:
#             print(i,"Prime Number")




# WAP to check whether the given number is a prime number in user defined Range Separately

# sr=int(input("Enter the Starting Range: "))
# er=int(input("Enter the Ending Range: "))
# def checkPrime(n):
#     if n<=1:
#         return False
#     else:
#         for i in range(2, (n//2)+1):
#             if n % i == 0:
#                 return False
#         return True
# print("Prime Numbers")
# for i in range(sr,er+1):
#     if sr>er or sr<=1:
#         print("Invalid Range")
#         break
#     else:
#         flag=checkPrime(i)
#         if flag:
#             print(i)
# print("NonPrime Numbers")
# for i in range(sr,er+1):
#     if sr>er or sr<=1:
#         print("Invalid Range")
#         break
#     else:
#         flag=checkPrime(i)
#         if not flag:
#             print(i)

