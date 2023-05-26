##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: November 1st 2022


import matplotlib.pyplot as plt
import numpy as np
print("Enter 1 to get upper right corner")
print("Enter 2 to get middle portion")
choice = input("Your choice:")

if choice == "1":
    inputFile = input("Enter input file name:")
    outputFile = input("Enter output file name:")
    img = plt.imread(inputFile)
    height = img.shape[0]              #Get height
    width = img.shape[1]               #Get width
    img2 = img[:int(height/2), int(width/2):]
    #plt.imshow(img2)
    #plt.show()
    plt.imsave(outputFile, img2)

elif choice == "2":
    inputFile = input("Enter input file name:")
    outputFile = input("Enter output file name:")
    img = plt.imread(inputFile)
    height = img.shape[0]              #Get height
    width = img.shape[1]               #Get width
    img2 = img[int(height/4):height - int(height/4), width//4:width - width//4]
    #plt.imshow(img2)
    #plt.show()
    plt.imsave(outputFile, img2)
else:
    print("wrong choice")
