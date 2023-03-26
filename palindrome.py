x=int(input())
a=x
ans = 0
while(x!=0):
    y=x%10
    x=x//10
    ans=ans*10+y
print(ans)
if(ans==a):
    print("Palindrome")
else:
    print("Not palindrome")