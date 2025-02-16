n=int(input("Enter the Number: "))
# for i in range(1,n+1):
    # for j in range(1,n+1):
    #     if j==1 or j==n or i==1 or i==n:
    #         print("*",end=" ")
    #     else:
    #         print(" ",end=" ")
    # print()

# if n%2==0:
#     n=n+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==n or i==1 or i==n or j==i or j==n-i+1 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# if n%2==0:
#     n=n+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==n or j==i or j==n-i+1 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# if n%2==0:
#     n=n+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if  i==1 or i==n or j==i or j==n-i+1 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# Triangle Hollow Patterns

# for i in range(1,n+1):
#     # for k in range(n,i,-1):
#     #     print(" ",end="")
#     for j in range(1,i+1):
#         if j==i or j==1 or i==n :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(1,n+1):
#     for k in range(n,i,-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         if j==i or j==1 or i==n :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         if j==1 or i==1 or j==n-i+1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(1,n+1):
#     for k in range(n,n-i+1,-1):
#         print(" ",end="")
#     for j in range(1,n-i+2):
#         if i ==1 or j==n-i+1 or j==1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# odd=1
# for i in range(1,n+1):
#     for j in range(1,odd+1):
#         if j==odd or j==1 or i==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     odd+=2

# 13
# odd=1
# for i in range(1,n+1):
#     for k in range(n*2-1,odd,-1):
#         print(" ",end="")
#     for j in range(1,odd+1):
#         if i==n or j==odd or j==1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#     odd+=2

# 14
# odd=n*2-1
# for i in range(1,n+1):
#     for k in range(n*2-1,odd,-1):
#         print(" ",end="")
#     for j in range(1,odd+1):
#         if i==1 or j==1 or j==odd:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#     odd-=2

# 15
# odd=n*2-1
# for i in range(1,n+1):
#     for k in range(n*2-1,odd,-1):
#         print(" ",end=" ")
#     for j in range(1,odd+1):
#         if i==1 or j==1 or j==odd:
#             print("*  ",end=" ")
#         else:
#             print("   ",end=" ")
#     print()
#     odd-=2

# 16
# odd=1
# for i in range(1,n*2):
#     for j in range(1,odd+1):
#         if j==1 or j==odd:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     if i<n:
#         odd+=1
#     else:
#         odd-=1

# 17
# odd=1
# for i in range(1,n*2):
#     for k in range(n,odd,-1):
#         print(" ",end=" ")
#     for j in range(1,odd+1):
#         if j==1 or j==odd:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     if i<n:
#         odd+=1
#     else:
#         odd-=1

# 18
# odd=n
# for i in range(1,n*2):
#     for j in range(1,odd+1):
#         if i==1 or j==odd or j==1 or i==n*2-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     if i<n:
#         odd-=1
#     else:
#         odd+=1

# 18==> glasshour
odd=n
for i in range(1,n*2):
    for k in range(n,odd,-1):
        print(" ",end=" ")
    for j in range(1,odd+1):
        if i==1 or j==odd or j==1 or i==n*2-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i<n:
        odd-=1
    else:
        odd+=1

# 19
# noc=1
# nor=n*2-1
# for i in range(1,n*2):
#     for j in range(1,n*2):
#         if j==noc or j==nor or j==1 or j==n*2-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     if i<n:
#         noc+=1
#         nor-=1
#     else:
#         noc-=1
#         nor+=1
#
#
# noc=n
# nor=n
# for i in range(1,n*2):
#     for j in range(1,n*2):
#         if j==noc or j==nor:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     if i<n:
#         noc-=1
#         nor+=1
#     else:
#         noc+=1
#         nor-=1
