# Check The Palindrome using Recursion

def palindrome(n,rev,temp):
    if n==0:
        return rev == temp
    rev=(rev*10)+n%10
    return palindrome((n//10),rev,temp)


n= int(input("Enter the Number: "))
flag=palindrome(n,0,n)
if flag:
    print("Palindrome")
else:
    print("Not Palindrome")
