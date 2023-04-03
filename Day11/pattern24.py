x=int(input("Enter Number"))
for i in range(1,x+1):
    if x%2!=0:
        if i==x//2+1:
            print("* "*(x-1))
        else:
            print("*",end="")
            print(" "*(x+(x//2)-1),end="")
            print("*")

    else:
        if i==x//2+1:
            print("* "*(x))
        else:
            print("*",end="")
            print(" "*(x+(x//2)+1),end="")
            print("*")

#Output when no. of stars is odd:
# *         *
# *         *
# *         *
# * * * * * *
# *         *
# *         *
# *         *
#Output when no. of stars is even:
# *             *
# *             *
# *             *
# *             *
# * * * * * * * *
# *             *
# *             *
# *             *