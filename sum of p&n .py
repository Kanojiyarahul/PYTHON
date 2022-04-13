sp = 0
sn = 0
n=1
while (n!=0):
     n = int(input("Enter any number  : "))
     if n > 0 :
       sp = sp + n
     else:
       sn = sn + n
print("Sum of all the positive numbers is  : ", sp)
print("Sum of all the negative numbers is  : ", sn)