##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: November 3rd 2022

hour = input("Enter hour (in 24 hour time): ")

if int(hour) < 12 and int(hour) >= 0:
    print("Good Morning")
elif int(hour) >= 12 and int(hour) < 17:
    print("Good Afternoon")
elif int(hour) >= 17 and int(hour) <= 24:
    print("Good Evening")
else:
    print("Incorrect hour, please enter a number between 0 and 24")

