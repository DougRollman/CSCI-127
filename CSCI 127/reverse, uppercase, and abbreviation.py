##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: September 22nd 2022


##--------------------------------------------------------

##Assignment Details

#Enter a phrase, reverse it, then capitalize each letter of the reversed string. Afterwards, get an abbreviation of the last letter of each word, starting from the last word to the first one.

#A sample run of your program should look like:

#input: City Univ of New York

#user reverse: kroY weN fo vinU ytiC
#user reverse upper: KROY WEN FO VINU YTIC
#user abbreviation: CUONY
#Here is another sample run of your program.

#input: Srbkts L Cizyjb

#user reverse: bjyziC L stkbrS
#user reverse upper: BJYZIC L STKBRS
#user abbreviation: SLC


##--------------------------------------------------------

reverse = "" #empty string defined for reverse
inp = input("input: ") # gets input from user
inpsplit = inp.split() # splits input (if multiple words) into a list of words
abb = "" #empty string defined for abbreviation
for i in range(len(inp),0,-1): #nested loop created to iterate backwards through user inp and store it in first char of reverse
    for j in range(1):
        reverse += inp[i - 1]
        
for word in inpsplit: #iterates through list of words and saves first letter to var abb
    abb += word[0]
#print(inpsplit)
#print(len(inpsplit))
print("") # couldnt figure out how to match the sample out put (\n was creating to many lines) was a quick fix, possibly incorrect
print("user reverse:",reverse) #prints reverse of user inp (see comment in respective for loop)
print("user reverse upper:", reverse.upper()) #capitolizes all letters in revers
print("user abbreviation:", abb.upper()) #capitolizes abb (first letter of each word in abbreviated format)


