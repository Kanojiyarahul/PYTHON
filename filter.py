###filter
##marks =[66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 92, 85]
##def student(score):
##    return score>80
##passing=list(filter(student,marks))
##print(passing)
        

#filter
rep=("demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP")
palindrome=list(filter(lambda x: x==x[::-1],rep))
print(palindrome)
