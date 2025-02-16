def countDigit(n,count):
    if n==0:
        return count
    return countDigit(n//10,count+1)

def armstrong(n,pow,asn,temp):
    if n==0:
        return asn == temp
    rem=n%10
    # asn=asn+(rem**pow)
    # n=n//10
    return armstrong(n//10,pow,asn+(rem**pow),temp)


n=int(input("Enter the Number: "))
res=countDigit(n,0)
flag=armstrong(n,res,0,n)
if flag:
    print("Armstrong")
else:
    print("Not Armstrong")