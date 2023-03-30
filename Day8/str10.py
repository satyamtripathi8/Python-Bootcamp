x=input("Enter string: ")
y=x.lower()
for i in range(0,len(x)):
    if x[i]==y[i]:
        # print("True: ",x[i],end="")
        print(chr(ord(x[i])-32),end="")
    else:
        # print("False :",x[i],end="")
        print(chr(ord(x[i])+32),end="")
