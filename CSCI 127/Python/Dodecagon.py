##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: August 30th 2022

import turtle
#copied from "https://huntercsci127.github.io/f22/lab1.html" in order to prevent window from stalling
wn = turtle.Screen()

#create a turtle
t = turtle.Turtle()

#number of sides for shape
n = 12

#for loop to create shape using n for number of sides
for i in range(n):
    #size reduced from 100 to allow dodecagon to fit on screen
    #size further reduced from 80 to allow dodecagon to fit on screen
    t.forward(60)
    t.left(360/n)
    
    
#added to leave window at shapes conclusion
wn.exitonclick()
