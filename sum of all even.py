#Write a program to find the sum of all even numbers 
#that falls between two numbers (exclusive both numbers) 
#entered from the user using while loop.
n1=int(input("enter n1 here :"))
n2=int(input("enter n2 here :"))
if n1>n2:
    while(n1>n2):
        if n2%2==0:
            print(n2)
        n2+=1
else:
    while(n1<n2):
        if n1%2==0:
            print(n1)
        n1+=1