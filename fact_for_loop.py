#WAP to calculate the factorial of number using for loop

n=int(input("enter number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial of  no:",fact)
    
