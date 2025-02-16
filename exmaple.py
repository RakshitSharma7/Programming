# n=int(input())
# temp=n
# rev=0
# while n!=0:
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10
#
# if rev==temp:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# def isPalinrome(n):
#     temp = n
#     rev = 0
#     while n != 0:
#         rem = n % 10
#         rev = rev * 10 + rem
#         n = n // 10
#     return rev==temp

# n = int(input())
# while n!=0:
#     sum = 0
#     for i in range(1, n+1):
#         flag = isPalinrome(i)
#         if flag:
#             sum += i
#     print(sum)
#     n = int(input())


# Input Using List

l=[10,30,50,100,0]
for j in l:
    if j!=0:
        sum = 0
        for i in range(1, j + 1):
            flag = isPalinrome(i)
            if flag:
                sum += i
        print(sum)
#
