##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: September 20th 2022


#-----------------------------------------------------------------------------------------------


#Assignment 07. upper and lower case

#Using the string commands introduced in Lab 2, write a Python program that prompts the user
#for a full name in the format of first name first and last name last,separated by a space.
#Use split method of string to extract last name and first name, then change last name to upper
#case using upper method of string. Print the full name in the format of last name first, first
#name followed, separated by comma. Enter user name, change it to lower case letters, followed by
#"@hunter.cuny.edu"
#-----------------------------------------------------------------------------------------------

name = input("Enter name in format firstName lastName: ") #prompts user for input(name) and saves it under variable name
last_first = name.split(" ") #splits the users name at the space 
print(last_first[1].upper() + ",", last_first[0]) #the last name is capitalized and printed first followed by the first name unchanged

email = input("Enter user name of email: ") #prompts user for input for email username
print(email.lower()+ "@hunter.cuny.edu") #converts email to lowercase and adds @hunter.cuny.edu
