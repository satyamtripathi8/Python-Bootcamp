x=int(input())
for i in range(1,x+5):
    if i<=x+1:
        print(" "*2*(x-i+1),end="")
        print("* "*(2*i-1))
    else:
        print(" "*(x*2),end="")
        print("* ")