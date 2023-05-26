
##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: November 7th 2022

import math
import turtle




def drawPantegon(t, length, numEdges):
   if numEdges > 0:
       #wn = turtle.Screen()
       t.forward(length)
       t.left(72)
       drawPantegon(t, length, numEdges-1)
       #wn.exitonclick()
def cornerPantegon(t, length):
   if length >= 25:
       #wn = turtle.Screen()
       drawPantegon(t, length, 5)
       length = int(length / 2)
       cornerPantegon(t, length)
       #wn.exitonclick()
        
def nestedPantegon(t, length):
    if length >= 25:
        #wn = turtle.Screen()
        drawPantegon(t, length, 5)
        t.forward(length/2)
        t.left(36)
        nestedPantegon(t, length* math.sin(54/180 * math.pi))
        #wn.exitonclick()

doug = turtle.Turtle()
drawPantegon(doug, 100, 5)
cornerPantegon(doug, 100)
nestedPantegon(doug, 100)

