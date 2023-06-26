import os
from os import path
import datetime
from datetime import date , time , timedelta
import time 

x = input("Enter file name with its extension: ")
if path.isfile(x):
    print("Item exists")
else:
    print("Item doesn't exists")

    
# print("file exists:" ,str(path.exists("abc.txt")))
