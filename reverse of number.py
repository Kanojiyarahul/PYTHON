num=int(input("enter no:"))
rev=0
while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
     
print("\n reverse of entered num is = %d" %rev)