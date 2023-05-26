##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: August 30th 2022


## Original Psuedo Code
## Repeat 9 times: 
##            Walk forward 100 steps
##            Turn left 105 degrees 
##            Walk forward 52 steps 
##            Turn left 105 degrees 
##    	      Walk forward 100 steps 
##            Turn right 170 degree
##

import turtle
#copied from "https://huntercsci127.github.io/f22/lab1.html" in order to prevent window from stalling
wn = turtle.Screen()


##create a turtle
f = turtle.Turtle()

##translation of psuedo code listed at top
for i in range(9):
    #Walk forward 100 steps
    f.forward(100)
    #Turn left 105 degrees 
    f.left(105)
    #Walk forward 52 steps 
    f.forward(52)
    #Turn left 105 degrees
    f.left(105)
    #Walk forward 100 steps 
    f.forward(100)
    #Turn right 170 degree
    f.right(170)

#added to leave window at shapes conclusion
wn.exitonclick()
