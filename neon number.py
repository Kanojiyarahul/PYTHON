#WAP to check whether the given number is Neon or not
num = int(input("Enter a number :"))
sq=num*num
sum= 0

while sq>0:

    sum =sum + sq%10
    sq = sq//10

if (num == sum ):
    print("Neon Number")
else:
    print("Not a Neon Number")
