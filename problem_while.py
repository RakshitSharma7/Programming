
# Incrementing Loop

# n=int(input("Enter the n: "))
# i=5
# while i<=n:
#     print(i)
#     i+=1

#Decrementing while Loop

# n=int(input("Enter the n: "))
# i=1
# while n>=i:
#     print(n)
#     n-=1


# Question 1

# val = 5
# while 1<= val: # here a aconstant is utilized for voolean condition
#     print(val)
#     1+1 # infinite loop

# Question 2
# val = 5
# while val>=10:  # Condition will become False since 5>=10(false)
#     print("Hello World")
#     val+=10

# Question 3
# val= (3*3)
# while val>1:  # Enters the infinite loop
#     print(val)
#     val+=1

# why for loop is not preferred in this scenario - since here the number of iteration id fixed that is 10 so in for loop we have give the stop

# for i in range(5):
#     n= int(input("Enter the number: "))
#     if n==5:
#         print("Hello World!")
#         break
# print("Program Executed")

# while True:
#     n = int(input("Enter the number: "))
#     if n == 5:
#         print("Hello World!")
#         break
# print("Program Executed")

def printMsg():
    print("Function Entered")
    print("Hello World")
    print("Function Executed")

print("Prog Started")
printMsg()
print("Prog Ended")