n=int(input())
# a=0
# b=1
# if n==1:
#     print(a)
# elif n==2:
#     print(a,b,end=" ")
# else:
#     print(a,b,end=" ")
#     while(n-2>0):
#         c=a+b
#         print(c,end=" ")
#         a=b
#         b=c
#         n=n-1
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(n))