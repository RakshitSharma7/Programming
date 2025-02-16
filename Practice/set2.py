# Question 1
n=int(input("Enter the Number: "))
s="1"
n=n//2
while (n)!=0:
    rem=n%2
    s = s + str(rem)
    n = n // 2
print(s)

# Question 2

def leftRightAngled(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

def invertedrightangled(n):
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            print(" ", end=" ")
        for j in range(1, n - i + 1):
            print("*", end=" ")
        print()

def pyramid(n):
    for i in range(1,n+1):
        for k in range(1,n-i+1):
            print(" ",end="")
        for j in range(1,i+1):
            print("@",end=" ")
        print()

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n=int(input("Enter the Number: "))
p=prime(n)

if n%2!=0 and p:
    leftRightAngled(n)
elif n%2!=0 and n%3==0:
    invertedrightangled(n)
elif n%2==0:
    pyramid(n)



