x=input()
#satyam
cnt=0
s= set()
for i in x:
    for j in x:
        if i==j:
            cnt=cnt+1
            s.add(i)
    print(cnt)
    cnt=0
print(s)
print(len(s))


    
