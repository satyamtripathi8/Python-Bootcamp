x=int(input())
for i in range(x+1):
     print(" "*(x-i),end="")
     print("* "*i)
for i in range(x-1,0,-1):
    print(" "*(x-i),end="")
    print("* "*(i))