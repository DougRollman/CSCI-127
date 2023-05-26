##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu 

import random

def intCheck():
    number = int(input("Enter only 1-6: " ))
    while number < 0 or number > 6:
        print("Input needs to be in 1-6. Re-enter:")
        number = int(input("Enter only 1-6: " ))
    return number
def userCompGame():
    computer = random.randrange(1,6)
    number = intCheck()
    total = computer + number
    print("user: ", number)
    print("computer: ", computer)
    if computer == number:
        print("draw")
    elif total == 3:
        print("user wins")
    elif total == 6:
        print("user wins")
    elif total == 7:
        print("user wins")
    elif total == 8:
        print("user wins")
    else:
        print("computer wins")

def main():
    userCompGame()

if __name__ == '__main__':
    main()
