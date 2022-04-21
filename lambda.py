###LAMBDA
##my_list=[1,3,5,7,9,10]
##double=list(map(lambda x: (x*2),my_list))
##print(double)


###lamda
##my_list=[1,3,5,7,9,10]
##my_list2=[2,4,6,7,9,5]
##double=list(map(lambda x: (x+15),my_list))
##double1=list(map(lambda x,y: (x*y),my_list,my_list2))
##print(double)
##print(double1)

###lambda
##mylist=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##mylist.sort(key=lambda x:x[1])
##print(mylist)                     

###lambda
##mylist=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
##result=sorted(mylist,key=lambda x: x['make'])
##print(result)
##
###lambda
##og=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##even_numbers=list(filter(lambda x: (x%2==0),og))
##odd_numbers=list(filter(lambda x: (x%2==1),og))
##
##print("even:",even_numbers)
##print("odd:",odd_numbers)

num=int(input("enter no:"))
double=(lambda x: x*2,num)
print(double)
