# WAP to Reverse the Number

def reverse(n,rev):
    if n==0:
        return rev
    rev=(rev*10)+n%10
    return reverse((n//10),rev)

n= int(input("Enter the Number: "))
res=reverse(n,0)
print(res)
