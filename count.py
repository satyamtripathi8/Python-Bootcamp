x = input()
d={}
for i in x:
    a= x.count(i)
    if i not in d.keys():
        d[i]=a
        
print(d)