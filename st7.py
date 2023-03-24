a=input()
b=a.lower()
count=0
for i in range(0,len(a)):
    if a[i]==b[i]:
        count=count+1

print(count)
print(a.islower())  # if all charcters are in lower case return true otherwise return false(isupper(),isdigit(),isalpha(),isalnum())
#ASCII - A(65)-Z(90);a(97)-z(122);space=32;0(48)-9(57)
#second method
cnt=0
for i in a:
    if i>='a' and i<='z':
        cnt=cnt+1
print(cnt)


