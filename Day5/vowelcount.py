x=input()
cnt=0
cons=0
space=0
for i in x:
    if (i== "A" or i=="I" or i=="E" or i=="O" or i=="U" or i=="a" or i=="i" or i=="e" or i=="o" or i=="u"):
        cnt=cnt+1
    elif(i==" "):
        space=space+1
    else:
        cons=cons+1
print("NO. of Vowels = ",cnt)
print("No. of consonants = ",cons)
print("No. of words = ",space+1)
print("No. of charcters = ",cnt+cons)
