##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: September 15th 2022

import turtle

#copied from "https://huntercsci127.github.io/f22/lab1.html" in order to prevent window from stalling
wn = turtle.Screen()

##create turtle

t = turtle.Turtle()
t.pensize(5)
t.shape("circle")

#TODO: finish the rest code
#hint: you may use color method of turtle.
#The distance for a long line is 300.
#The distance for a short line is 100.

##creating a function that excepts color as an argument allowing me to reuse the code easily
def turtle_sprint(color):
        #initial long stretch (color is set and turtle moves foward 300 units)
        t.color(color)
        t.forward(300)
        #short loop to handle the 2 - 100 unit movements
        for i in range(2):
            t.right(90)
            t.forward(100)
        #turn right at the end of the sequence
        t.right(90)

##the actual program        
turtle_sprint("green")
turtle_sprint("blue")
turtle_sprint("cyan")
turtle_sprint("red")

wn.exitonclick()
