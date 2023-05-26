##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: October 18th 2022

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

picture = input("Enter file name: ")
t = float(input("Enter threshhold: "))
ca = plt.imread(picture)   #Read in image
countSnow = 0            #Number of pixels that are almost white
totalPixels = 0


#For every pixel:
for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          #Check if red, green, and blue are > t:
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
               countSnow = countSnow + 1
          totalPixels = totalPixels + 1

percentage = (countSnow / totalPixels) * 100

print("number of white pixels: ", countSnow)
print("percent of white pixels", str(round(percentage,2)) + "%")
