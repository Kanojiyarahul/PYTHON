while(True):
    
    print("welcome to my calculator\n")
    print("my menu")
    print("1: addition")
    print("2: subtraction")
    print("3; multiplication")
    print("4: division")
    print("5: power")
    print("6: modulus")
    print("7: Exit")
    

    c = input("enter your selection:")
    

     
        
    if(c=="1"):    
        x=int(input("enter x value:"))
        y=int(input("enter y value:"))
        print(x,"+",y,"=",x+y)
    elif (c=="2"):
        x=int(input("enter x value:"))
        y=int(input("enter y value:"))
        print(x,"-",y,"=",x-y)
    elif (c=="3"):
        x=int(input("enter x value:"))
        y=int(input("enter y value:"))
        print(x,"*",y,"=",x*y)
    elif (c=="4"):
        x=int(input("enter x value:"))
        y=int(input("enter y value:"))
        print(x,"/",y,"=",x/y)
    elif (c=="5"):
        x=int(input("enter x value:"))
        y=int(input("enter y value:"))
        print(x,"**",y,"=",x**y)
    elif (c=="6"):
        x=int(input("enter x value:"))
        y=int(input("enter y value:"))
        print(x,"%",y,"=",x%y)
    elif (c=="7"):
         d=input("are you sure, you want to exit?(Y/N)")
         
         
         if(d=="Y"):
             break
         elif(d=="N"):
             continue
            
    else:
    
        print("invalid input")
    
else:
    print("invalid selection")
