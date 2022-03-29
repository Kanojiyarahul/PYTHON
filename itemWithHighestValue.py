item=[{'apple':5},{'banana':8},{'orange':7},{'grapes':4}]
def itemwithhighestvalue(item):
    mx=-999999999
    name=""
    for i in item:
        for j,k in i.items():
            if(k>mx):
                name=j
                mx=k
    return(name,mx)
