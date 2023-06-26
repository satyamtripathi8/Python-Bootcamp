import os
from os import path


x = input("Enter file name with its extension: ")
if path.isfile(x):
    print("It is File")
elif path.isdir(x):
    print("It is Directory")
else:
    print("Item doesn't exsits")



    
