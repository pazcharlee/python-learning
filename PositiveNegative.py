#First Assingment back after a couple weeks break
#Refresher

#Check if user input is positive, negative or 0

ans = input("Do you want to enter a number(yes/no): ")

while ans != "no":
    num = int(input("Enter a number: "))
    
    if num > 0 :
        print("Positive")
    elif num < 0 :
        print("Negative")
    else :
        print("Zero")

    ans = input("Do you want to enter another number(yes/no):")
