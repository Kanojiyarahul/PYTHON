#Write a program to display all the numbers which are divisible by 13 but not by 3 between 100 and 500.(exclusive both numbers)
i = 101
while(i < 500):
    if i % 13 == 0 and i % 3 != 0:
      print(i)
    i = i + 1