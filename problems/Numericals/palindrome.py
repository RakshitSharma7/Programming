# Write a Program to check given number is Palindrome or Not


# n=int(input("Enter the Number: "))
# temp=n
# rev=0
# while n!=0:
#     rem=n%10
#     n=n//10
#     rev=(rev*10) +rem
# if rev == temp:
#     print("Palindrome")
# else:
#     print("Not Palindrome")



#  Write a Program to check given number is Palindrome or Not Using function

# n=int(input("Enter the Number: "))
# def checkPalindrome(n):
#     temp = n
#     rev = 0
#     while n != 0:
#         rem = n % 10
#         n = n // 10
#         rev = (rev * 10) + rem
#     return rev==temp
#
# flag=checkPalindrome(n)
# if flag:
#     print("Palindrome")
# else:
#     print("Not Palindrome")



# Write a Program to check given number is Palindrome or Not in defines range

# sr=int(input("Enter the Starting Range: "))
# er=int(input("Enter the End Range: "))
# def checkPalindrome(n):
#     temp = n
#     rev = 0
#     while n != 0:
#         rem = n % 10
#         n = n // 10
#         rev = (rev * 10) + rem
#     return rev==temp
#
# for i in range(sr,er+1):
#     if sr>er:
#         print("Invalid Range")
#     else:
#         flag=checkPalindrome(i)
#         if flag:
#             print(i,"Palindrome")




#  Write a Program to check given number is Palindrome or Not , print list seperately


# sr=int(input("Enter the Starting Range: "))
# er=int(input("Enter the End Range: "))
# def checkPalindrome(n):
#     temp = n
#     rev = 0
#     while n != 0:
#         rem = n % 10
#         n = n // 10
#         rev = (rev * 10) + rem
#     return rev==temp
# print("Palindrome")
# for i in range(sr,er+1):
#     if sr>er:
#         print("Invalid Range")
#     else:
#         flag=checkPalindrome(i)
#         if flag:
#             print(i)
# print("Not Palindrome")
# for i in range(sr,er+1):
#     if sr>er:
#         print("Invalid Range")
#     else:
#         flag=checkPalindrome(i)
#         if not flag:
#             print(i)
