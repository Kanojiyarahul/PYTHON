s1=float(input("enter no 1:"))
s2=float(input("enter no 2:"))
s3=float(input("enter no 3:"))
s4=float(input("enter no 4:"))
if (s1>s2 and s1>s3 and s1>s4):
    print("s1 is greater")
elif (s2>s3 and s2>s1 and s2>s4):
    print("s2 is greater")
elif (s3>s1 and s3>s2 and s3>s4):
    print("s3 is greater")
elif (s4>s1 and s4>s2 and s4>s3):
    print("s4 is greater")
else:
    print("all no are not equal")
