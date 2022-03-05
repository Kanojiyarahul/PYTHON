 


#STRONG
def strong(n):
    total=0
    n1=n
    while n!=0:
        rem=n%10
        f=1
        for i in range(1,rem+1):
            f=f*i
        total=total+f
        n=n//10
    if n1==total:
        return ("armstrong number")
    else:
        return("not an armstrong number")


#REVERSE
def reverse(n):
    rev=0
    a=""
    while(n!=0):
        
        rem=n%10
        rev=(rev*10)+rem

        n=n//10
    a=a+str(rev)
    b=int(a)
    return(b)



#PRIMENO
def primeno(n):
    for i in range(2,n):
        if n%i==0:
            return("not a prime no")
        else:
            return("prime no")
        


#PALINDROME
def palindrome(n):
    rev=0
    a=""
    n1=n
    while(n!=0):
        
        rem=n%10
        rev=(rev*10)+rem

        n=n//10
    a=a+str(rev)
    b=int(a)
    if b==n1:
        return(f"{n1} is palindrome")
    else:
        return(f"{n1} is not a palindrome")






#NEON
def neon(n):
    
    s=n*n
    rem=0
    while s>0:
        rem=rem+s%10
        s=s//10
    if n==rem:
        return("neon number")
    else:
        return("not a neon number")



#FIBONACCI
    def fibo(n):
        x=0
        y=1
        i=1
        a=""
        while(i<=n):
            a=a+str(x)+"\n"
            z=x+y
            x=y
            y=z
            i=i+1
        return a
    print(fibo(10))




#FACTORIAL
def factorial(n):
        
    
    f=1
    for i in range (1,n+1):
        f=f*i
    return(f"factorial of {n} is {f}")
    

#ARMSTRONG
def amstrong(n):
    d=0
    n1=n
    rev=0
    n2=n1
    while(n!=0):
            
        n=n//10
        d=d+1
    while(n1!=0):
        rem=n1%10
        rev=rev+(rem**d)
        n1=n1//10
    if rev==n2:
        return(f"{n2} is an amstrong number")
    else:
        return(f"{n2} is not an amstrong number")



#TABLE
def table(n):
    a=""
    

    for i in range(1,11):
        a=a+str(n*i,"\n")
    return (a)

    print(a)
        
        
        
    
    
        

    
