x=int(input())
for i in range(x+1):
    print(" "*(x-i),end="")
    print("* "*i,end="")
    print("  "*(x-i),end="")
    print("* "*i)