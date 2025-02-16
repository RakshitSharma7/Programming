# WAP TO CONVERT LOWER CASE TO UPPERCASE WITHOUT USING INBUILT FUNCTION



# str=input("ENter the String: ")
#
# def toUpper(str):
#     res = ""
#     for i in range(len(str)):
#         if ord(str[i]) >= 97 and ord(str[i]) <= 122:
#             res += chr(ord(str[i]) - 32)
#         else:
#             res += str[i]
#     return res
#
# def toLower(str):
#     res = ""
#     for i in range(len(str)):
#         if ord(str[i]) >= 65 and ord(str[i]) <= 90:
#             res += chr(ord(str[i]) + 32)
#         else:
#             res += str[i]
#     return res
#
# def toSwapCase(str):
#     res=""
#     for i in str:
#         if 'a'<=i<='z':
#             res+=chr(ord(i)-32)
#         elif 'A'<=i<='Z':
#             res+=chr(ord(i)+32)
#         else:
#             res+=i
#     return res
#
#
# print("New String (to Upper): ",toUpper(str))
# print("New String (to Lower): ",toLower(str))
# print("New String (to SwapCase): ",toSwapCase(str))

# Reversal Of String

# Type---1

# str=input("Enter the String: ")
# def reverseStr1(str):
#     res = ""
#     for i in range(len(str) - 1, 0 - 1, -1):
#         res = res + str[i]
#     return res
#
# ans=reverseStr1(str)
# print("Reversed String: ",ans)


# Type ------2

# def reverseStr2(str):
#     res = ""
#     for i in range(len(str)):
#         res = str[i] + res
#     return res
#
# str=input("Enter String: ")
# ans=reverseStr2(str)
# print("Reversed String: ",ans)


# def reverseStr3(str,n,rev):
#     if n==len(str):
#         return rev
#     rev=str[n]+rev
#     return reverseStr3(str,n+1,rev)
#
#
# def reverseStr4(str,n,rev):
#     if n<0:
#         return rev
#     rev=rev+str[n]
#     return reverseStr4(str,n-1,rev)
#
# str=input("Enter String: ")
# ans=reverseStr4(str,len(str)-1,"")
# print("Reversed String (Decrementing Recursion)",ans)
# ans=reverseStr3(str,0,"")
# print("Reversed String (Incrementing Recursion)",ans)



# str1="red rose is good"+" "
# res=""
# ans=""
# for i in range(len(str1)):
#     if str1[i]==" ":
#         ans=res+" "+ans
#         res=""
#     else:
#         res+=str1[i]
#
# print(ans)


# def reverseStr5(str):
#     l = list(str)
#     i, j = 0, len(str) - 1
#     while i <= j:
#         l[i], l[j] = l[j], l[i]
#         i += 1
#         j -= 1
#     nstr=""
#     for i in l:
#         nstr+=i
#     return nstr
# str=input("Enter String: ")
# ans=reverseStr5(str)
# print(ans)

# WAP to reverse each individual word

# def reverse(s):
#     i = 0
#     nword = ""
#     nsent = ""
#     while i < len(s):
#         if s[i] != " ":
#             nword = s[i] + nword
#         elif nword != "":
#             if nsent == "":
#                 nsent += nword
#             else:
#                 nsent = nsent + " " + nword
#             nword = ""
#         i += 1
#     return nsent

# s=input("Enter String: ")+" "
# ans=reverse(s)
# print(ans)




# def reverseWord(s):
#     i = 0
#     nword = ""
#     nsent = ""
#     while i < len(s):
#         if s[i] != " ":
#             nword = nword + s[i]
#         elif nword != "":
#             if nsent == "":
#                 nsent += nword
#             else:
#                 nsent = nword+" "+nsent
#             nword = ""
#         i += 1
#     return nsent
#
# s=input("ENter String: ")+" "
# ans=reverseWord(s)
# print(ans)


# 557
# 151

# HackerRank
# Reverse String 4
# String Reverse Words


# print(chr(48))