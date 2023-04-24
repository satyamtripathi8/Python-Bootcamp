x=int(input())
for i in range(1,(x+4)):
    if i<=x:
        print(" "*(x-i),end="")
        print("* "*i)
    else:
        print(" "*2*(x//2),end="")
        print("* ")
