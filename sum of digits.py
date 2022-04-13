#Write a program to find the sum of the digits of a number accepted from the user
num1 = int(input("Enter any number : "))
r=0
s=0
while(num1!=0):
    r = num1 % 10
    s = s + r
    num1 = num1//10
print("Sum of the digits are : " , s)