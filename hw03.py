a=input("Please type anything: ")
b=dict()
for x in a:
    if x not in b:
        b[x]=1
    else:
        b[x]=b[x]+1
for x in b:
    c=b[x]
    print("'",x,"'","：",c)
    