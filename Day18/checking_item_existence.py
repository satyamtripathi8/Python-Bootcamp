import os
from os import path
import datetime
from datetime import date , time , timedelta
import time 

x = input("Enter file name with its extension: ")
if path.exists(x) is True:
    print("file exists")
else:
    print("file doesn't exists")
print("file exists:" ,str(path.exists("abc.txt")))
