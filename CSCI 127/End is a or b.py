##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: October 19th 2022

words = input("Enter a list of words, separated by a space: ")
wordList = words.split(" ")
endsInCount = 0
length = len(wordList)
for word in wordList:
    if word[-1] == "a" or word[-1] == "b":
        endsInCount += 1

print("number of words:", len(wordList))
print("number of words ending with a or b:", endsInCount)
print("fraction of words starting with a or b: ", round((endsInCount / length), 2))
