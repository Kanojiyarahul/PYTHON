#Write a program to find the sum of following series:
#S = 1 + 4 – 9 + 16 – 25 + 36 – … … n terms
n = int(input("Enter number of terms : "))
s = 0
sp = 1
sn = 0
i = 2
while(i <= n):
   if i % 2 == 0:
      sp = sp + i ** 2
      i = i + 1
   else :
      sn = sn + i ** 2
      i = i + 1
print(sp - sn)