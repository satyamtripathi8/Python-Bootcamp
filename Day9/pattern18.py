x=int(input())
# for i in range(1,x+1):
#     print(" "*(x-i),end="")
#     print((chr(64+i)+" ")*i,end="")
#     print()
    
for i in range(1,x+1):
    for j in range(x-i,0,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print(chr(64+i)+" ",end="")
        
    print()