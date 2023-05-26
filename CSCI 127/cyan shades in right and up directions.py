##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: September 28th 2022

#---------------------------------------------------

#Modify the program from Lab 3 to show the shades of cyan.

#Your output should look similar to:


#    t = turtle.Turtle()

#    t.penup()
#    t.backward(100)
#    t.left(90)
#    t.backward(100)
#    t.right(??) #you fill in a degree in ??
#    t.pendown()

    #TODO: draw right shade

    #TODO: move to the start direction of up shade

    #TODO: draw up shade
#Warning: for the purpose of grading script, the right shade is drawn before the up shade.

#Hints: you may use one of the following approaches.

#Simplest approach: create two turtles, one to draw the right shade and the other to draw the up shade. By default, each turtle starts from the origin -- coordinates x and y are both zero and faces east.
#Use only one turtle. After drawing the right shade, the turtle moves backward appropriate steps to its start point (you may need to calculate the total distance from the turtle's current position to the start point). You may need to penup, pendown and pensize methods of the turtle before drawing the up shade.
#Use only one turle. After drawing the right shade, the turtle go to the start point. You may need use penup, pendown, and pensize methods of the turtle before drawing the up shade.
#For explanation of turtle commands, read turtle library.

#---------------------------------------------------





import turtle				#Import the turtle drawing package


turtle.colormode(255)		#Allows colors to be given as 0 through 255
t = turtle.Turtle()        #Create a turtle		
t.backward(100)		        #Move her backwards, to give more space to draw

    
for i in range(0,255,10):
     t.forward(10)		#Move forward
     t.pensize(i)		#Set the drawing size to be i (larger each time)
     t.color(0,i,i)		#Set the red channel to be i (brighter each time)

t.penup()
t.backward(255)
t.left(90)


for i in range(0,255,10):
     t.forward(10)		#Move forward
     t.pensize(i)		#Set the drawing size to be i (larger each time)
     t.color(0,i,i)	#Set the red channel to be i (brighter each time)
     t.pendown()
     


