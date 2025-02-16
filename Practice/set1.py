# Question 1
asc=100
dsc=999
n=999
print("Ascending Order: ")
while asc<=n:
    print(asc,end=" ")
    asc+=1
n=100
print()
print("Descending Order: ")
while dsc>=n:
    print(dsc, end=" ")
    dsc-=1

# Question 2

n=int(input("Enter the Number: "))
if n>0:
    i=(n*2)-1
    print("The odd number in the position", n, " is ", i)
else:
    print("Invalid ")