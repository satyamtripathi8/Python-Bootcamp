li=[2,1,2,1,3,4,3]

#1 method

# string=" "
# for i in li:
#     cnt=0
#     for j in li:
#         if i==j:
#             cnt +=1
#     if cnt==1:
#              string += str(i)
# print(string)

#2 method

# for i in li:
#     if li.count(i)==1:
#         print(i)

#3 method
# ans=0
# for i in li:
#     ans=ans^i
# print(ans)

#4 method

li.sort()
n=len(li)
i=1
while (i<n):
    if li[i]==li[i-1]:
        i+=2
    else:
        print(li[i])
        break
if i == n:
    print(li[n-1])
    