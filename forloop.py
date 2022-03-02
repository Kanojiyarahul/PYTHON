for x in range(0,20):
    if(x%4==0):
        pass
    print(x,end=', ')
else:
    print("loop finished")

#str
str="hello"
for val in str:
    print(val)

#str1
str1="hello"
for val in range(len(str1)):
    print(str[val])

#list
list=[3,5,7,9,11,13]
for val in list:
    print(val)

#list1
list1=[1,"hello",34,"debug",78]
for i in list1:
    print(i)

#dict
dict={"apple":10,"bananana":20,"grapes":30}
for val in dict:
    print(dict[val])