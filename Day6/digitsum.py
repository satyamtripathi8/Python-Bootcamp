x=int(input())
ans=0
while(x!=0):
    y=x%10
    x=x//10
    ans+=y
print(ans)