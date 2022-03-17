#WAP to check whether the given number is palindrome or not
n=12321
n1=n
rev=0
for i in str(n):
    r=n%10
    rev=rev*10+r
    n=n//10
if n1==rev:
    print("Number is Palindrome:",rev)
else:
     print("Number is not a Palindrome:",rev)