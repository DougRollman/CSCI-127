##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: October 18th 2022


binary = input("Enter a string with 0 or 1 only: ")
num = 0
for i in range((len(binary)-1),0,-1):
    if binary[i] != "0" and binary[i] != "1":
        print("Letter",binary[i],"is not allowed in binary string")
        break
for i in range((len(binary)-1),0-1,-1):
    print("i =", i)
    if binary[i] == "1":
        print(binary[i], "times 2 to the power of",((len(binary)-1) - i), "=")
        num += int(binary[i]) * ( 2 ** ((len(binary)-1) - i))

print("num =", num)

        
