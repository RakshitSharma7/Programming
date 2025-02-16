# Perfect Number

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
