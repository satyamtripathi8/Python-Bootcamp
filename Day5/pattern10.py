x=int(input())
for i in range(1,x+1):
    print("* "*(i),end="")
    print(" "*4*(x-i),end="")
    print("* "*(i))
for i in range(x,0,-1):
    print("* "*(i),end="")
    print(" "*4*(x-i),end="")
    print("* "*(i))