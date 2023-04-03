x=int(input("Enter Number"))
for i in range(1,x+1):
    if i==1 or i==x:
        print("* "*x)
    else:
        if x%2==0:
            print(" "*(2*x//2-1),end="")
            print("*")
        else:
            print(" "*(2*x//2-1),end="")
            print("*")

#Output when no. of stars is odd:
# * * * * * * * * * * * 
#           *
#           *
#           *
#           *
#           *
#           *
#           *
#           *
#           *
# * * * * * * * * * * *

#Output when no. of stars is even:
# * * * * * * * * * * 
#          *
#          *
#          *
#          *
#          *
#          *
#          *
#          *
# * * * * * * * * * *