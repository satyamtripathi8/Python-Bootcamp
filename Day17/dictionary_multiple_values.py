a=int(input("How many books: "))
d={}
for i in range(a):
    b=input("Enter book id")
    n=input("Enter name of book")
    q=input("enter quantity")
    p=input("enter price")
    d[b]=n,q,p
print(d)