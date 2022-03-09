jan=int(input("enter date:"))
feb=int(input("enter date:"))
mar=int(input("enter date:"))
apr=int(input("enter date:"))
may=int(input("enter date:"))
if jan==31 and jan!=30:
    print("jan is having 31 days")
elif feb==28 and feb==30 and 31:
    print("feb s having 28 days")
elif mar==31 and mar!=30:
    print("mar is havng 31 days")
elif apr==30 and apr!=31:
    print("apr is having 30 days")
elif may==31 and may!=30:
    print("may is having 31 days")
else:
    print("months having random days count")     