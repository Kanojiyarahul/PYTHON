n=int(input("enter no :"))
r=0
rn=0
while(n!=0):
    r=n%10
    rn=rn*10+r
    n=n//10
print("Reverse number is : ", rn)


