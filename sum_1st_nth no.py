
#WAP to print the sum of  1st nth natural numbers using while loop

n=int(input("enter number:"))
sum=0
x=1
while(x<=n):
    sum=sum+x
    x=x+1
print("sum of natural num:",sum)