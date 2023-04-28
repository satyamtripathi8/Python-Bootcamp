li=[7,8,5,3,5,9,0,1,12,23,45,56]
print(li)
x=int(input("Element you want to search"))
for i in range(len(li)):
    if li[i]==x:
        print("Found")
        break
    
        