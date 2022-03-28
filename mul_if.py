n1=int(input("enter no1:"))
n2=int(input("enter no2:"))
n3=int(input("enter no3:"))
if n1>n2 or n1>n3:
    print("n1 is greater")
if n2>n3 and n2>n1:
    print("n2 is greater")
if n3>n1 and n3>n2:
    print("n3 is greater")        