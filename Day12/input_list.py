li=[]
x=int(input("How many elements you want: "))
for i in range(x):
    y=int(input())
    li.append(y)
print(li)
li1=[]
a=int(input("How many elements you want: "))
for i in range(a):
    y=int(input())
    li1.append(y)
print(li1)
list=li+li1
print(list)
