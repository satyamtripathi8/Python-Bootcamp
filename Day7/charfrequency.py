# x=input()
# cnt=0
# s={}
# for i in x:
#     for j in x:
#         if i==j:
#             cnt=cnt+1
#             s.add(i)
#     print(i, cnt,"- Times")
#     print(len(s))
#     cnt=0
x=input()
cnt=0
s={}
for i in range(1,len(x)+1):
    for j in x:
        if x[i]==j:
            cnt=cnt+1
            s.add(x[i])
    print(x[i], cnt,"- Times")
    print(len(s))
    cnt=0