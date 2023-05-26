##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: October 11th 2022

import numpy as np
import matplotlib.pyplot as plt


imgoutput = input(" Enter output file name: ")
img = np.ones( (30,30,3) )
img[:, :, 2 ] = 0 #yellow background - set blue channel to 0
img[5:8, 5:25, 0 ] = 0 # red channel set to zero
img[5:8, 5:25, 1 ] = 0 # green channel set to zero
img[5:8, 5:25, 2 ] = 1 # blue channel set to one
img[8:25, 13:16, 0 ] = 0 # red channel set to zero
img[8:25, 13:16, 1 ] = 1 # green channel set to one
img[8:25, 13:16, 2 ] = 0 # blue channel set to zero
plt.imsave(imgoutput, img)
#plt.imshow(img)
#plt.show()


