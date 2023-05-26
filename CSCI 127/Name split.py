
##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: October 2nd 2022


##--------------------------------------------------------

##Assignment Details

#Enter a list of names separated by semicolon. Display each name in a line, started by the first letter of first name, followed by a dot, a space, and last name.

#A sample run of your program should look like:

#Enter a list of names, separated by semicolon: George Washington;James Adam;Thomas Jefferson;James Madison;James Monroe
#G. Washington
#J. Adam
#T. Jefferson
#J. Madison
#J. Monroe

##--------------------------------------------------------

userinp = input("Enter a list of names, separated by semicolon: ")
lst = userinp.split(";")
for i in range(len(lst)):
    tempstr = lst[i]
    tempname = tempstr.split(" ")
    firstname = tempname[0]
    initial = firstname[0]
    print(initial + ". " + tempname[1])

