x=int(input())
for i in range(0,x):
    if i==((x//2)):
        print("* "*x,)
    else:
        if x%2==0:
            print(" "*(2*(x//2)-1),end="")
            print("*")
        else:
            print(" "*(2*(x//2)),end="")
            print("*")
