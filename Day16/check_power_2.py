x=int(input())
# if x==0:
#     print("Not possible")
# else:    
#     while(x%2==0):
#         x=x//2
# if(x==1):
#     print("true")
# else:
#     print("False")

# Using Recursion
def check(n):
    if n==1:
        print("True")
    if n==0 or n%2!=0:
        print("False")
    return check(n//2)
print(check(x))