#WAP to list out all the leap years from 1900-2030 using for loop

for i in range(1900,2030):
    if (i%4==0) and (i%100!=0) or (i%400==0):
        print("leap year :",i)