#using list comprehension store all Leap year from 1900 to 2030 in a list
leap_year=[i for i in range(1900,2030) if (i%4==0) and (i%100!=0) or (i%400==0)]
print(leap_year)