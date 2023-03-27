x = int(input())

t = x *2 -1 

sr = 0
er = t-1
sc = 0
ec = t-1


k = 1

x = sr
y = sc
for i in range(x):
    while(y<=ec):
        y+=1
        print(k,end="")
    print()
    y = ec
    sr += 1

    while(x<=er):
        x += 1
        print(k,end="") 
    print() 
    x = er  
    ec -= 1

    while(y>=sc):
        y-=1
        print(k,end="")
    print()
    y = sc
    er -= 1

    while(x >= sr):
        x-=1 
        print(k,end="")
    print()
    x = er
    sc += 1

    k+=1
