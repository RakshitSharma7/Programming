from IPython.utils.py3compat import no_code

n=int(input("Enter the Number: "))
# 1.
# val=65
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(val),end=" ")
#     print()
#     val+=1

# OR

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(64+i),end=" ")
#     print()

# # 2.
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()

# 3.
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(96+j),end=" ")
#     print()

# 4.
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print(chr(96+j),end=" ")
#     print()
# OR
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(chr(96+j),end=" ")
#     print()

# 5.
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i%2!=0:
#             print(chr(64+j),end=" ")
#         else:
#             print(chr(96+j),end=" ")
#     print()

# 6.
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print(chr(64+j-i+1),end=" ")
#     print()

# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(chr(64+j),end=" ")
#     print()

# 7.
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         if (i%2!=0 and j%2==0) or (i%2==0 and j%i!=0):
#             print(chr(96+j),end=" ")
#         else:
#             print(chr(64+j),end=" ")
#     print()
#
# x=0
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         x += 1
#         if x%2==0:
#             print(chr(96+j),end=" ")
#         else:
#             print(chr(64+j),end=" ")
#     print()

# 8.
# x=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(64+x),end=" ")
#         x+=1
#     print()

# x=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if x%2!=0:
#             print(chr(64+x),end=" ")
#         else:
#             print(chr(96+x),end=" ")
#         x+=1
#     print()


# noc=n
# for i in range(1,n*2):
#     for j in range(1,noc+1):
#         print(chr(64+j),end=" ")
#     if i<n:
#         noc-=1
#     else:
#         noc+=1
#     print()

# noc=1
# for i in range(1,n*2):
#     for j in range(n,noc-1,-1):
#         print(chr(64+j),end=" ")
#     if i<n:
#         noc+=1
#     else:
#         noc-=1
#     print()


# noc=1
# for i in range(1,n*2):
#     for j in range(noc,n+1):
#         print(chr(64+j),end=" ")
#     if i<n:
#         noc+=1
#     else:
#         noc-=1
#     print()


# noc=n
# for i in range(1,n*2):
#     for j in range(1,noc+1):
#         print(chr(64+noc),end=" ")
#     if i<n:
#         noc-=1
#     else:
#         noc+=1
#     print()


# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j<=i:
#             print(chr(64+j),end=" ")
#         else:
#             print(chr(64+i),end=" ")
#     print()

# for i in range(n,1-1,-1):
#     for j in range(n,1-1,-1):
#         if j>=i:
#             print(chr(64+i),end=" ")
#         else:
#             print(chr(64+j),end=" ")
#     print()

# noc=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(64+noc),end=" ")
#         noc+=1
#     print()