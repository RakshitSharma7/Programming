# 1.ArmStrong Number    ---> Done
# 2.CountDigit     ---> Done
# 3.EvenOdd     ---> Done
# 4.LeapYear
# 5.Palindrome
# 6.PrimeNumber

# 1. ArmStrong

# n=int(input("Enter the Number: "))
# temp=n
# Count the Digit

# s=input("Enter the Roman: ")
# total=0
# n=len(s)
# roman_map={
#             'I' : 1,
#             'V' : 5,
#             'X' : 10,
#             'L' : 50,
#             'C' : 100,
#             'D' : 500,
#             'M' : 1000
#         }
# for i in range(n):
#     if i<n-1 and roman_map[s[i]] < roman_map[s[i+1]]:
#         total-=roman_map[s[i]]
#     else:
#         total+=roman_map[s[i]]
# print(total)