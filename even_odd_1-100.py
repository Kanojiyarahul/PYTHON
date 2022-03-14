#WAP to give all the even and odd number in list from 1-100 using for loop

even=[]
odd=[]
for i in range(1,100):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("even number",even)
print("odd number",odd) 