x=int(input())
a=1
for i in range(1,x+1):
    p = a
    for j in range(1,i+1):
        print(p,end=" ")
        if p==0: #p=1 if p==0 else 0
            p=1
        else:
            p=0
    print()
    if a==0:
        a=1
    else:
        a=0

