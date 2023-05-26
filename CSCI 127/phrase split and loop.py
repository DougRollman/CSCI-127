
##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: October 2nd 2022


#Write a program that asks the user for a message and then prints the message out, one fewer word a line until there is only one word, then continue to add one word a line until becoming the original message.

#A sample run of your program should look like:

#Enter a phrase: how are you?
#how are you?
#how are
#how
#how are
#how are you?
#Hint: See Lab 2 or Lecture 2 notes. Use split method to break the original message by a a list of words. Then use for-loop to display partial of the list. To display a list of words as a string, use ' '.join(list_of_words). For example,
#
#lst = ['a', 'bc', 'd', 'e']
#print(' '.join(lst[:2])) 
#display the first 2 elements of lst, joined by a space, 
#that is, display
#a bc


phrase = input("Enter a phrase: ")
arr = phrase.split()

#same result
#for j in range(len(arr),0, -1):
#     print(' '.join(arr[0:j]))

for j in range(len(arr),0, -1):
     print(' '.join(arr[0:j]))
for i in range(1, len(arr)):
    print(' '.join(arr[0:i+1]))
