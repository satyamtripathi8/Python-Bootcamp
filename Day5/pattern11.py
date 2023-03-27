# x=int(input())
# for i in range(1,x+1):
#     if i==1 or i==x:
#         print("* "*x)
#     else:
#         print("* ",end="")
#         print(" "*2*(x-2),end="")
#         print("* ")


x = int(input())
for i in range(x):
    for j in range(x):
        if i == 0 or j == 0 or i == (x-1) or j == (x-1):
            print("* ",end="")
        else:
            print(" "*2,end="")
    print()