x=int(input())
if x%2==0:
    for i in range(1,x+1):
        if(i==1):
            print("* "*x)
        else:
            print(" "*(x//2+x//2-1),end="")
            print("*")
else:
    for i in range(1,x+1):
        if(i==1):
            print("* "*x)
        else:
            print(" "*(x//2+x//2),end="")
            print("*")

#Output when no. of stars is even:

# * * * * * * 
#      *
#      *
#      *
#      *
#      *
#Output when no. of stars is odd:
# * * * * * * * 
#       *
#       *
#       *
#       *
#       *
#       *