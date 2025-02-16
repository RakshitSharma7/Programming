# Write a Program to check a given number is ARMSTRONG Number or Not.

# n=int(input("Enter the Number: "))
# temp=n
# def countDigit(n):
#     count = 0
#     while n!=0:
#         n=n//10
#         count+=1
#     return count
#
# pow=countDigit(n)
# asn=0
# while n!=0:
#     rem=n%10
#     asn=asn+rem**pow
#     n=n//10
# if temp==asn:
#     print("ArmStrong Number")
# else:
#     print("Not ArmStrong")




# Write a Program to check a given number is ARMSTRONG Number using Function

# n=int(input("Enter the Number: "))
# def countDigit(n):
#     count = 0
#     while n!=0:
#         n=n//10
#         count+=1
#     return count
#
# def checkArmstrong(n,pow):
#     temp=n
#     asn = 0
#     while n != 0:
#         rem = n % 10
#         asn = asn + rem ** pow
#         n = n // 10
#     return asn == temp
#
# pow = countDigit(n)
# flag=checkArmstrong(n,pow)
# if flag:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")




