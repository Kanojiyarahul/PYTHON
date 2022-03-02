fact=1
for i in range(1,10,1):
    fact=fact*i
    print(fact)

attempt=3
for count in range(1,4,1):
    usrnm=input("enter usrnm:")
    pwd=input("enter pwd:")
    if usrnm=="admin" and pwd=="admin123":
        print("login successfull")
        break
    else:
        print("login failed","remaining attempt:",attempt-count)