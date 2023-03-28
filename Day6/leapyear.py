x=int(input("Enter Year"))
if (x%100==0):
    if(x%400==0):
        print("Leap year")
    else:
        print("Not leap Year")
elif(x%4==0):
    print("Leap year ")
else:
    print("Not leap year")