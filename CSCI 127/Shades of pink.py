##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: September 29th 2022


import turtle				#Import the turtle drawing package


turtle.colormode(255)		#Allows colors to be given as 0 through 255
t = turtle.Turtle()             #Create a turtle		
t.backward(100)		        #Move her backwards, to give more space to draw

    
for i in range(0,255,10):
     t.forward(10)		#Move forward
     t.pensize(i)		#Set the drawing size to be i (larger each time)
     t.color(i,0,i)
    
for i in range(255,0, -10):
     t.forward(10)		#Move forward
     t.pensize(i)		#Set the drawing size to be i (larger each time)
     t.color(i,0 ,i)
