##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: November 1st 2022


def main():
    userInput_string = input("Enter a string: ")
    userInput_char = input("Enter a char: ")
    count = 0
    for i in userInput_string:
        if i == userInput_char:
            count += 1
    print("number of '" + userInput_char + "' in " + '"' + userInput_string + '" is', count)
    return

main()
