x=int(input("No. of Rows: "))
y=int(input("No. of Columns: "))
list=[]
for i in range(x):
    li=[]
    print("Enter" ,i," row:")
    for j in range(y):
        a=int(input())
        li.append(a)
    list.append(li)
print(list)