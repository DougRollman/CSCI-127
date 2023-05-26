##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: October 12th 2022

import numpy as np
import matplotlib.pyplot as plt
num = int(input("Enter the size: "))
imgoutput = input("Enter output file: ")
img = np.zeros( (num,num,3) )
img[:,1::2,1] = 1.0
img[:,::2,2] = 1.0

#plt.imshow(img)
#plt.show()

plt.imsave(imgoutput, img)

