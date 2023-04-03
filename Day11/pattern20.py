x=int(input())
c=1
for i in range(0,x):
    c+=1
    print(1)
    print(c,end=" ")
    for j in range(x-1,0,-1):
        print((c+(j)),end=" ")
print()