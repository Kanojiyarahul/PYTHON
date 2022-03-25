#6.1-Categorize,which opeartor will give resultant in range and which will give categorical output



#6.2-take 2 input from user and do all arithmetic operations.Display best possible console output on screen
n1=int(input("enter value of n1:"))
n2=int(input("enter value of n2:"))
print("addition is:",n1+n2+56)
print("subtraction is:",n1-n2-12)
print("multiplication is:",n1*n2*5)
print("mod is:",n1%n2%3)
print("division is:",n1/n2/8)

#6.3-take two inputs from user and find from data pool(1,2,3,4,5,6,7,8,9) are those two input present in pool or not
x=int(input("enter x:"))
y=int(input('enter y:'))
list=[1,2,3,4,5,6,7,8,9];
 
if ( x and y in list ):
   print("x,y is  present in given list")
else:
   print("x,y is not present in given list")
 

#6.4-take a input from user and check the identity of that specific input.display best possible console output
user=int(input("enter user:"))
if(type(user) is int):
    print("true")
else:
    print("false")

#6.5-take a number from user as an input,update the value by adding 10, followed by multiplying by 6 and lastly get floor division by 6
no=int(input("enter number here:"))
print(no)
no+=10
print("addition of 10 is:",no)
no*=6
print("multiplication of 6 :",no)
no//=6
print("floor division is:",no)