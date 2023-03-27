# x=int(input())
# cnt=0
# for i in range(1,x+1):
#     if x%i==0:
#         cnt=cnt+1
# if cnt==2:
#     print("Prime")
# else:
#     print("Composite")

x=int(input())
cnt=0
i=1
while(cnt>=2 and i<=x):
    if x% i ==0:
        cnt+=1
    i=i+1
if cnt==2:
    print("prime")
else:
    print("Composite")
