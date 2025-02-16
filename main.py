# ARITHMETIC OPERATORS
from os import remove
from traceback import print_tb

from win32con import PRINTRATEUNIT_PPM

#+

# print(2++9+5)
# print(+8)
# print(5+9+3+8+9)

# -

# print(9-4)
# print(10-5--4-6)

# *

# print(5*6)
# print(5*3*2)
# print(*6) #Type Error

# **

# print(6**4)
# print(5**6)

# # //
#
# print(8//2)
# print(15//6)
#
#
# print(8/2)
# print(15/6)
# print(100/3)
#
# print(8%2)
# print(15%6)

# print(3**3**3)

# Relational Operator

# print(26>16)

# print(False!=True)

# print((5*6)<(2**6))

# print((5*5)>=(3*7))

# print((3+3+2)<=(-1))

# print((10//2)!= 4 )

# print(True > (False-1))


# Logical Operator

# print(True and True and False)
#
# print((True and False)and (True and True))
#
# print(((5*6)!= 90 )and True)
#
#
# print(False or False or False or True)
#
# print(False or False and(True or False))

# print(((4/1)==(52/13) and (0 or 1 ) or ((True and True ) and False or True) and(((5*6)!= 90 )and True)))


# print(not((True and False and False)or (3>-1)))

# print(not(((45+1) != (90-45)) and ((2**5)< (5**3)) and False))

# a=5 # initialization
# print(a)
# a=10 # re-initialization
# print(a)
# b=20 # initialization
# print(b)
# c=30# initialization
# print(c)
# c=b # re-initialization
# print(c).

# print(d)


# a=10
# b=2
# c=3
# c*=a+b
# print(c)

# x=5
# y=10
# sum=0
# # sum+=x-y
# sum+=x
# print(sum)



# a=10
# b=10
# print("Before Id's : ")
# print("Id of a:",id(a))
# print("Id of b:",id(b))
# print(a is b)
# c=20
# b+=c
# print("After Id's : ")
# print("Id of a:",id(a))
# print("Id of b:",id(b))
# print("Id of c:",id(c))
# print(a is not b)
# print(b is c)

# s="Sky is Blue"
# a="s"
# print(a in s)
# print("z" in s)
# print("a" in a) # no error because variable a is a String which is iterable
# a=10
# b=20
# print(a in b)


# Palindrome

# str= input("Enter the String: ").lower()
#
# s=str[::-1]
#
# if s== str:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# Count the Vowels and Constants

# v=0
# c=0
# str=input("Enter the String: ").lower()
# vowels="aeiou"
#
# for i in str:
#     if i in vowels:
#         v+=1
#     else:
#         c+=1
#
# print("Vowels = ",v,"Constants = ",c)

# REmove the Duplicates in the String

# str = input("Enter the String: ")
# rev=""
# for i in str:
#     if i not in rev:
#         rev = rev + i
#     else:
#         pass
# print(rev)

#  Frequency of the Character

# str = input("Enter the String: ")
# d={}
# s=""
# for i in str:
#     if i not in s:
#         s+=i
#         val = str.count(i)
#         print(i,val)


# Anagrams

# str1= input("Enter the String1: ")
# str2= input("Enter the String2: ")
# # print(sorted(str1))
# v1="".join(sorted(str1))
# v2="".join(sorted(str2))
#
# if v1==v2:
#     print("Given Strings are Anagram")
# else:
#     print("Not a Anagram")

# t=(10,20,30,40,50,60)
# print(t[1:-2])
# print(t[-2:-6])


# LIST WITHIN A TUPLE

# student_info=("Ram",[60,70,80])
# print(student_info)
# name,marks=student_info
# print(name)
# print(marks)

# LIST IS MUTABLE AND TUPLE IS IMMUTABLE

# L=[10,20,30,40]
# print(L)
# print(L[3])
# L[3]=400
# print(L)

# t=(10,20,30,40)
# print(t)
# print(t[3])
# # t[3]=400
# print(t)



# s={10,20,30,40,60,70,50}
# print(s)
# print(type(s))
# s1={}
# print(type(s1))

# for i,num in enumerate(s):
#     print(i,num)

# a=set()
#
# for i in range(5):
#     data=int(input("Enter the Data: "))
#     a.add(data)
# print(a)
#
# a.update((50,60,80))
# print(a)
# a.discard(50)
# print(a)

# s1={1,2,3,4}
# s2={3,4,5,6}
# s3=s1.union(s2)
# print(s3)
# s4=s1.difference(s2)
# print(s4)
# s5=s1.intersection(s2)
# print(s5)
# s6=s2.difference(s1)
# print(s6)
# s7=s1.symmetric_difference(s2)
# print(s7)

def conv(a):
    rev=[]
    for i in a:
        rev.append(i)
    return rev


l = ["aaa", "aaa", "aaa"]
res=[]
grp=[]
flag=False
for i in l:
    x=conv(i)
    s1=sorted(x)
    for j in l:
        s2=sorted(j)
        if s1==s2 and i!=j:
            grp.append(j)
            l.remove(j)
    grp.append(i)
    res.append(grp)
    grp=[]
    l.remove(i)
for i in l:
    res.append([i])
print(res)

# s1={1,2,3,4}
# s2={1,2,3,4}
#
# print(s1.issubset(s2))
# print(s2.issubset(s1))
# print(s1.issuperset(s2))
# print(s2.issuperset(s1))

# s1={1,2,3,4}
# s2={3,4,5,6}
# s3={5,6,7,8}
#
# print(s1.isdisjoint(s2))
# print(s2.isdisjoint(s3))
# print(s3.isdisjoint(s1))

#  FROZEN SET

# s=frozenset([10,20,30,40])
# s1={10,20,30,40}
# print(s)
# print(s1)
#
# s1.add(50)
# print(s1)
# s.add(40)
# print()


#

