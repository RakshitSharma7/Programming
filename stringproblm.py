# 1
# s="abba"
# temp=s[0]
# count=0
# for i in s:
#     flag = True
#     if i==temp:
#         count+=1
#     else:
#         flag=False
#     if not flag:
#         print(temp, end="")
#         print(count, end="")
#         count=1
#     temp = i
# print(temp, end="")
# print(count, end="")
# 2
# str ="i.like.this.program.very.much"
# rev=""
# l=str.split(".")
# for i in l:
#     rev=i+"."+rev
# print(rev)
from itertools import zip_longest

# 3
# str="abbc"
# l=[]
# pal=[]
# count=0
# for i in range(0,len(str)+1):
#     for j in range(0,len(str)+1):
#         value=str[i:j]
#         if value!="":
#             l.append(value)
#
# for value in l:
#     str=""
#     for i in value:
#         str=i+str
#     if value==str:
#         pal.append(value)
#         count+=1
# print(pal," ",count)


# 4
# str="Welcome to Coding Ninjas"
# l=str.split()
# rev=""
# for i in l:
#     rev=i+" "+rev
# print(rev)

# 5
# asc=65
# str="The quick brown fox jumps over the  dog".lower()
# flag=True
# l=[]
# for i in range(97,123):
#     char=chr(i)
#     if char not in str:
#         flag="False"
#         l.append(char)
#         # break
#
# print(l," ",flag)



# 1
# str="Www.HackerRank.com"
# str="Pythonist 2"
# res=""
# for i in str:
#     if i.isupper():
#         res=res+i.lower()
#     elif i.islower():
#         res=res+i.upper()
#     else:
#         res=res+i
# print(res)

# 2
# str="I am Hackrrank"
# l=str.split()
# res=""
# for i in l:
#     rev=""
#     for k in i:
#         rev=k+rev
#     res=res+" "+rev
# print(res)
#

# 3
# str="pwwkew"
# def substring(str):
#     l = []
#     for i in range(0, len(str) + 1):
#         for j in range(0, len(str) + 1):
#             value = str[i:j]
#             if value != "":
#                 l.append(value)
#     return l
#
# def longestsubstring(sub):
#     longest=""
#     flag=True
#     for i in sub:
#         for k in i:
#             if i.count(k) > 1:
#                 flag=False
#                 break
#             else:
#                 continue
#         if flag:
#             if len(i)>len(longest):
#                 longest=i
#     return True,longest
#
# sub=substring(str)
# flag,value=longestsubstring(sub)
#
# if flag:
#     print(value)
# else:
#     print(value)

# 4
# str="Hello WOrld"
# l=str.split()
# ans=len(l[-1])
# print(ans)


# 5
# str="Manjunath"
# res=""
# l=[]
# for i in str:
#     if i in l and "$" not in l:
#         l.append("$")
#     else:
#         l.append(i)
#
# for i in l:
#     res=res+i
# print(res)


#48-57
# 65-90
# 97-127

# char=input()
# if chr(65)<=char<=chr(90) or chr(97)<=char<=chr(127):
#     print("Alphabets")
# elif chr(48)<=char<=chr(57):
#     print("Digits")

# s="a"
# print(chr(65))

#
# ch=input()
# if 48<=ord(ch)<=57:
#     print("Digits")
# elif 65<=ord(ch)<=90 or 97<=ord(ch)<=127:
#     print("Alphabets")

# l=[1,2,3,4,5,6,7,8,9,10]
# target=12
# ans=[]

# for i in l:
#     for j in l:
#         if i!=j and ( i+j==target and ((i,j) not in ans and (j,i) not in ans)):
#                 ans.append((i,j))
# print(ans)

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==target:
#             ans.append((l[i],l[j]))
# print(ans)

# largest=0
# second=0
# third=0
# for i in l:
#     if i>largest:
#         third=second
#         second=largest
#         largest=i
# print(third)

# l=[10,20,30]
# l1=[60,90,180]
#
# l2=l+l1
# print(l2)
#
# l3=l*2
# print(l3)
#
# a=list(range(10))
# print(a)
#
# b=list(range(10,18))
# print(b)

# a=[10,2,3,4,5,[7,0,8],10]
# print(all(a))

names=["Dhoni","Kohli","Rohit","ABD"]
runs=[70000,18000,45000,36000]
country=["India","India"]
ipl_team=["CSK","RCB"]
l=[]
# for i in range(len(names)):
#     l.append((names[i],runs[i],country[i],ipl_team[i]))
# print(l)

ans=list(zip_longest(names,runs,country,ipl_team,fillvalue="#"))
# for i in ans:
#     l.append(i)
# print(l)
print(ans)
