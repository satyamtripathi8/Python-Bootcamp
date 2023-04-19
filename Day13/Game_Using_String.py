import random
x=random.randrange(1,10)
print("You have three attempts either to win or lose....,Best of Luck!")
n=int(input("Enter Number Between 1 to 10: "))
cnt = 1
while(x!=n and cnt<3):
    if(n>x):
        print("Enter small Value")
    else:
        print("Enter greater value")
    n = int(input())
    cnt = cnt + 1


if(cnt < 3):
    print("Mil gaya : ",n,"attempt liya ",cnt)
else:
    print("Haar Gye,Better Luck Next Time!")
