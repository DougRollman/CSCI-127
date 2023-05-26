##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: October 11th 2022

print("(a) convert centimeters to feet")
print("(b) convert centimeters to feet and inches")
print("(c) convert feet and inches to centimeters")
choice = input("Enter a or b or c: ")
if choice == "a" or choice == "b":
    num = int(input("Enter height in centimeters: "))
elif choice == "c":
    num = input("Enter height in feet and inches, separated by a space: ")
else:
    print("Wrong choice, please enter only a or b or c.")

if choice == "a":
    num = num / 30.48
    temp = str(num)
    int_decimal = temp.split(".")
    decimal = int_decimal[1]
    integer = int_decimal[0]
    num = integer + "." + decimal[0:2]
    print("height is", float(num), "inches")
elif choice == "b":
    total_inches = num / 2.54
    feet = int(total_inches / 12)
    inches = int(total_inches % 12)
    if inches == 0:
        print("height is", feet, "feet")
    else:
        print("height is", feet, "feet and", inches, "inches")
else:
    legnth = num.split(" ")
    feet = int(legnth[0])
    inches = int(legnth[1])
    num = (feet * 30.48) + (inches * 2.54)
    print("height is", round(num), "cm")



