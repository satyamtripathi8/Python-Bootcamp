x=int(input())
a=y=x
cnt=0
ans=0
while(x!=0):
    x=x//10
    cnt=cnt+1
for i in range(1,cnt+1):
    b=a%10
    a=a//10
    ans+=b**cnt
print(ans)
if(y==ans):
    print("Armstrong")
else:
    print("Not Armstrong")
