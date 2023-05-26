##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: October 2nd 2022


import numpy 
import matplotlib.pyplot as plt 

imginput = input("Enter name of the input file: ")
imgoutput = input("Enter name of the output file: ")
img = plt.imread(imginput)

#show original png image
#plt.imshow(img)
#plt.show()

#copy img to img2
img2 = img.copy()


#ie, set these two channel to be zero.
img2[:, :, 0] = 0 #set red channel to be zero


#wont display because of gradescope
#plt.imshow(img2)
#plt.show()

#save the img2 to users input from imgoutput
plt.imsave(imgoutput, img2)
