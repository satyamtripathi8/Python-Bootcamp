x=int(input())
for i in range(1,x+1):
    if i==1:
        print("* "*x)

    else:
        print(" "*(i),end="")
        print("*",end="")
        print(" "*(x-i),end="")
        print(" *")