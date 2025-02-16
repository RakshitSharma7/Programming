n=int(input("Enter the Number: "))
odd=n+1
for i in range(1,n*2):
    for j in range(1,n+2):
        if i==1 or j==1 or j==odd:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i < n:
        odd-=1
    else:
        odd+=1
