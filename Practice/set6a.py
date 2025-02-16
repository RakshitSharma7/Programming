# n=int(input("Enter the number: "))
#
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()
from math import floor

#  QUESTION 2
# n=int(input("Enter the number: "))
# c=1
# odd=1
# for i in range(1,n+1):
#     v=i
#     for k in range(n,i,-1):
#         print(" ",end=" ")
#     for j in range(1,odd+1):
#         if v>1:
#             print(v,end=" ")
#             v-=1
#             c = v
#         else:
#             print(c,end=" ")
#             c+=1
#     print()
#     odd+=2


# QUESTION 3
# n=int(input("Enter the Number: "))
# noc=1
# for i in range(1,n*2):
#     for k in range(n,noc,-1):
#         print(" ",end="")
#     for j in range(1,noc+1):
#         if j==noc or j==1:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1


# QUESTION 4

# n=int(input("Enter the Number: "))
#
# for i in range(1,n+1):
#     for k in range(n,i,-1):
#         print(" ",end=" ")
#     for j in range(1,n+1):
#         if i%2!=0:
#             print(j,end=" ")
#         else:
#             print(n-j+1,end=" ")
#     print()


# a = int(input())
# b = int(input())


# def squares(a, b):
#     count=0
#     sr=int(a**0.5)
#     er=int(b**0.5)
#     if sr < a**0.5:
#         sr+=1
#     for i in range(sr,er+1):
#         count+=1
#     return count
#
# ans = squares(a, b)
# print(ans)

# ans=a+b
# print(ans)

#
# def encryption(s):
#     s1=""
#     for i in s:
#         if i!=" ":
#             s1+=i
#     row=int(len(s1)**0.5)
#     col=row+1
#     z=row
#     if row*col < len(s1):
#         row+=1
#     ini=0
#     li=[]
#     for i in range(row):
#         li.append(s1[ini:col])
#         ini=col
#         col+=col
#     sub = ""
#     ele = 0
#     index = 0
#     for i in range(len(s1)+z):
#         if ele < row:
#             sub += li[ele][index]
#             ele += 1
#         else:
#             index += 1
#             ele = 0
#             sub += " "
#     return sub
#
#
# #
# s=input("ENter the String: ")
# ans=encryption(s)
# print(ans)
# l=["have","anic","eday"]
# r=3
# c=4
# res=[]
#
# print(sub)

def kangaroo(x1, v1, x2, v2):
    # If the second kangaroo is ahead and has a greater velocity, they will never meet
    if v1 <= v2 and x1 < x2:
        return "NO"

    # Check if they meet at the same position
    if (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    else:
        return "NO"


ans=kangaroo(0,2,5,6)
print(ans)