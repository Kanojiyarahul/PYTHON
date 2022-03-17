#wap to print fabonacci for loop series.
n=int(input("Enter the Range Number: "))
val1 = 0
val2 = 1
i=0
for i in range(0,n+1):
    sum=val1+val2
    print(val1)
    val1=val2
    val2=sum
    i+=1
 