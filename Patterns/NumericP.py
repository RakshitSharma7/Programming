n=int(input("Enter the Number: "))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n-i+1,end=" ")
#     print()


# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print()

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n-j+1,end=" ")
#     print()

# a=n*n
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(a,end=" ")
#         a-=1
#     print()

# count=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(count,end=" ")
#         count+=1
#     print()


# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<j:
#             print(i,end=" ")
#         else:
#             print(j,end=" ")
#     print()

# for i in range(n,1-1,-1):
#     for j in range(n,1-1,-1):
#         if i>j:
#             print(j,end=" ")
#         else:
#             print(i,end=" ")
#     print()

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>j:
#             print(i,end=" ")
#         else:
#             print(j,end=" ")
#     print()

# for i in range(n,1-1,-1):
#     for j in range(n,1-1,-1):
#         if i>j:
#             print(i,end=" ")
#         else:
#             print(j,end=" ")
#     print()

# incre=1
#
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i%2!=0:
#             print(incre,end=" ")
#         else:
#             decre=n*i+1
#             decre -= j
#             print(decre,end=" ")
#         incre+=1
#     print()

# incre=1
#
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i%2!=0:
#             print(incre,end=" ")
#             decre=incre
#         else:
#             print(decre,end=" ")
#             decre-=1
#         incre+=1
#     print()
#     decre+=n



# x=64
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(x+i),end=" ")
#     print()

# a=['silent','ncdln','listen','abbcd']
#
# for i in a:
#     for j in a:
#         if i==j:
#             pass
#         else:
#             s1=i.split()
#             s2=j.split()
#             l1=s1.sort()
#             l2=s2.sort()
#             # str1=""
#             # str2=""
#             # for k in l1:
#             #     str1=str1+k
#             # for l in l2:
#             #     str2=str2+l
#             if l1==l2:
#                 print("Anagrams of given List",i,"and",j )



# n=int(input("Enter the Number: "))
# odd=1
# decre=1
# for i in range(1,n+1):
#     for j in range(1,odd+1):
#         if i>=j:
#             print(j,end=" ")
#             decre=j
#         else:
#             decre-=1
#             print(decre,end=" ")
#     print()
#     odd+=2

# odd=1
# for i in range(1,n+1):
#     count = i
#     for j in range(1,odd+1):
#         if j<i:
#             print(j,end="")
#         else:
#             print(count,end="")
#             count-=1
#     odd+=2
#     print()

# incre=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if i%2!=0:
#             print(incre,end=" ")
#             decre=incre
#         else:
#             print(decre,end=" ")
#             decre-=1
#         incre+=1
#     print()
#     decre+=i+1


for i in range(0,n):
    num=1
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(0,i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)

    print()