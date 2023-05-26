##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: August 30th 2022


##Assignment Details


##Write a program that prompts the user to enter a phrase. Then for each character in the phrase,
##print out character, its ASCII code, and the next two letter in ASCII table.

##prompt user for a phrase
phrase = input("Enter a phrase: ")
print("letter ASCII next_two_letter")

for c in phrase:
    print("%6c %5i %15c"%(c,ord(c),(chr(ord(c)+2))))
    
