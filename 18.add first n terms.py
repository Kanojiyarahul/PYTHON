#wap to add first n terms of foll series using a while loop
n=int(input("enter any number:"))
sum=0
fact=1
i=1
while(i<n):
    fact=fact*i
    sum=sum+i/fact
    i=i+1
print("sum is :", sum)
