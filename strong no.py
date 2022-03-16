#WAP to check whether the given number is Strong or not
n=145
n1=n
total=0
while(n!=0):
    rem=n%10
    f=1
    for i in range(1,rem+1):
        f=f*i
    total=total+f
    n=n//10
if(n1==total):
    print(f"{n1} is an trong no")
else:
        print(f"{n1} is not an strong no")