x=input()
#satyam

str=""
for i in x:
    cnt=0
    for j in x:
        if i==j:
            cnt=cnt+1
    if i not in str:
                str +=i
                print(i,"--",cnt)
            
    
    
    





    
