x=int(input())
for i in range(1,x+1):
    print((chr(64+i)+" ")*i,end="")
    print("* "*(x-i))