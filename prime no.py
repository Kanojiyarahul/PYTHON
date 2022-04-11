#wap to check whether a number is prime or not using while loop.
##num = int(input("Enter a number ( greater than 1):"))  
##f = 0
##i = 2
##while i <= num / 2:
##    if num % i == 0:
##        f=1
##        break
##    i=i+1
##    
##if f==0:
##    print("The entered number is a PRIME number")
##else:
##    print("The entered number is not a PRIME number")

def primeno(n):
    
    while n>=0:
        if n%2==0:
            return (f"{n}not a prime")
        else:
            return (f"{n}prime")
        
