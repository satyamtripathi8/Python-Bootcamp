x=int(input())
sum=1
for i in range(1,x+1):
    sum *=i
print(sum)
#2
def factorial(n):
    ans=1
    for i in range(1,n+1):
        ans*=i
    print(ans)
#3
import math
print(math.factorial(5))