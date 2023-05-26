##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: September 20th 2022


##--------------------------------------------------------

##Assignment Details

##Write a program that prompts the user to enter a word and then prints out the
##word with each letter shifted right by 13. That is, 'a' becomes 'n', 'b'
##becomes 'o', ... 'y' becomes 'l', and 'z' becomes 'm'.

##Assume that all inputted words are in lower case letters: 'a',...,'z'.


##--------------------------------------------------------


user_inp = input("Enter an all-small-letter string: ") #get input from user and stores it under variable user_inp
key = int(input("Enter a non-negative int to shift: "))#the key used to shift on the ceasar cipher
code = "" #defining variable that will eventually hold the coded message

for i in range(len(user_inp)): #loop set to the legnth of the users input so it will iterate as many times as there are characters
      letter = user_inp[i] #temp variable for each letter in the array of the users inp, will be used to encode each letter
      code += chr((ord(letter) + key - 97) % 26 + 97)#finds the ascii equivalent of the letter, adds the  amount set by the key and mods by 26 so it will return to the beginning of the alpha bet for letters that go beyond z

print(code)
