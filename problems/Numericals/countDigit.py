# Write a program to count the number of digits present in a given number


# num = int(input("Enter the Digit: "))
# count=0
# while num!=0:
#     num=num//10
#     count+=1
#
# print("Number of Digits in a Given num: ",count)



# Write a program to count the number of digits present in a given number using Function


# num =int(input("Enter the Number: "))
# def countDigit(n):
#     count=0
#     if n<0:
#         n=n*-1
#     while n!=0:
#         n//=10
#         count+=1
#     return count
#
# if num<0:
#     num=num*-1
# res=countDigit(num)
# print("Number of Digit: ",res)



# Write a Program to display the count of digits of each individual number in a given range


# sr=int(input("Enter the Start Range: "))
# er=int(input("Enter the End Range: "))
#
# def countDigit(n):
#     count=0
#     # if n<0:
#     #     n=n*-1
#     while n!=0:
#         n//=10
#         count+=1
#     return count
#
# if sr<er:
#     for i in range(sr,er+1):
#         res=countDigit(i)
#         print(i,"Consists of ",res," digit")
# else:
#     print("Invalid Range ")