# Write a Program to check weather the year is leap year or not


# year=int(input("Enter the year: "))
#
# if (year % 100 !=0 and year % 4 ==0 ) or  (year % 400 == 0):
#     print("Leap year!")
# else:
#     print("Not a Leap year !!")



# Write a Program to check weather the year is leap year or not using Function

# def checkLeapYear(year):
#     return (year % 100 !=0 and year % 4 ==0 ) or  (year % 400 == 0)

# flag = checkLeapYear(year)
# if flag :
#     print("Leap Year")
# else:
#     print("Not a Leap Year")



# WAP to print all the leap year ub the defined range


# def checkLeapYear(year):
#     return (year%100!=0 and year%4==0) or year%400 == 0
#
# sr = int(input("Enter the Start Year : "))
# er = int(input("Enter the End Year : "))
#
# for i in range(sr,er+1):
#     if sr>er :
#         print("Invalid Range")
#     else:
#         flag=checkLeapYear(i)
#         if flag:
#             print(i,"Is a Leap Year")



# WAP to print all the leap year ub the defined range print seperately leap and non leap year


# def checkLeapYear(year):
#     return (year%100!=0 and year%4==0) or year%400 == 0
#
# sr = int(input("Enter the Start Year : "))
# er = int(input("Enter the End Year : "))
# print("Leap Years: ")
# for i in range(sr,er+1):
#     if sr>er :
#         print("Invalid Range")
#     else:
#         flag=checkLeapYear(i)
#         if flag:
#             print(i)
# print("Non Leap Years: ")
# for i in range(sr,er+1):
#     if sr>er :
#         print("Invalid Range")
#     else:
#         flag=checkLeapYear(i)
#         if not flag:
#             print(i)
