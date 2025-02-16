# RECURSION

# def printNum1(n):
#     if n>4:
#         return
#     print(n)
#     printNum1(n+1)
#
#
# printNum1(1)


# WAP to print the N Natural Numbers

# def printNumIncr(start,end):
#     if start>end:
#         return
#     print(start)
#     printNumIncr(start+1,end)
#
# n= int(input("Enter the Number: "))
# printNumIncr(1,n)




# Print the N natural number is Reverse order
# def printNumIncr(start,end):
#     if start>end:
#         return
#     printNumIncr(start+1,end)
#     print(start)
# n= int(input("Enter the Number: "))
# printNumIncr(1,n)

# Print the N natural number O/P----> 12344321
# def printNumIncr(start,end):
#     if start>end:
#         return
#     print(start)
#     printNumIncr(start+1,end)
#     print(start)
# n= int(input("Enter the Number: "))
# printNumIncr(1,n)


# Print the N natural number O/P----> 43211234
# def printNumIncr(start,end):
#     if start>end:
#         return
#     print(end)
#     printNumIncr(start,end-1)
#     print(end)
# n= int(input("Enter the Number: "))
# printNumIncr(1,n)


# Questions:
# 1. perfect number


# 2. GCD or HCF.
# 3. LCM




# WAP to Print the Fibbonacci Series till the nth Position

# Using Recursion

# def fibbo(n1,n2,pos):
#     if pos==0:
#         return
#     print(n1)
#     fibbo(n2,(n1+n2),pos-1)
#
# n=int(input("Enter the Position: "))
# fibbo(0,1,n)

# Using Loop

# pos=int(input("Enter the Number: "))
# n1=0
# n2=1
# while pos!=0:
#     print(n1)
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     pos-=1

#
# def fibbo(n1,n2,pos,n):
#     if pos==n:
#         return
#     print(n1)
#     fibbo(n2,(n1+n2),pos+1,n)
#
# n=int(input("Enter the Position: "))
# fibbo(0,1,0,n)