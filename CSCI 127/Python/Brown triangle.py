
##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: September 20th 2022


##--------------------------------------------------------

##Assignment Details

#Modify the program from Lab 3 to draw a brown turtle (color #964B00 or RGB code 150, 75, 0), stamp after each turn.
#The turtle moves forward by 100 in each round.

##--------------------------------------------------------



import turtle

t = turtle.Turtle()     #creating a turtle and naming it t
t.shape("turtle")       #calling shape function to give t a "turtle" shape       
turtle.colormode(255)   #calling colormode so rgb is able to be defined with integers from 1-255
t.color(150,75,0)       #defining t to have the color brown


for i in range(3):      #for loop that stamps at start, moves foward 100 units and turns 1/3rd of a circle(120 degrees) 3 times

    t.forward(100)
    t.left(120)
    t.stamp()
