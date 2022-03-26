x=[3,5,1,2,9,5,6,10]
min=-9999999999
i=0
while(i<len(x)):
    if(min<x[i]):
        min=x[i]
    i=i+1
print(min)
