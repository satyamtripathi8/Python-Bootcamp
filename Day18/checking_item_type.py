import os
from os import path
import datetime
from datetime import date , time , timedelta
import time 

x = input("Enter existing file name with its extension: ")
if path.isfile(x):
    print("It is File")
elif path.isdir(x):
    print("It is Directory")
else:
    print("Item doesn't exsits")



    
