x=int(input())
while(x!=0):
    y=x%10
    x=x//10
    print(y,end="")

#second method
while(x!=0):
    y=x%10
    x=x//10
    ans=ans*10+y
print(ans)