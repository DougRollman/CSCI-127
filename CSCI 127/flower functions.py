
##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: November 15th 2022



import turtle			#Import the turtle drawing package


def petal(color, angle):
    
    turtle.colormode(255)
    doug = turtle.Turtle(visible=False)
    doug.left(angle)
    if color == "red":
        for i in range(0,255,10):
            doug.forward(10)	#Move forward
            doug.pensize(i)
            doug.color(i,0,0)
    elif color == "green":
        for i in range(0,255,10):
            doug.forward(10)	#Move forward
            doug.pensize(i)
            doug.color(0,i,0)
    elif color == "blue":
        for i in range(0,255,10):
            doug.forward(10)	#Move forward
            doug.pensize(i)
            doug.color(0,0,i)
    elif color == "yellow":
        for i in range(0,255,10):
            doug.forward(10)	#Move forward
            doug.pensize(i)
            doug.color(i,i,0)
    elif color == "purple":
        for i in range(0,255,10):
            doug.forward(10)	#Move forward
            doug.pensize(i)
            doug.color(i,0,i)
    elif color == "cyan":
        for i in range(0,255,10):
            doug.forward(10)	#Move forward
            doug.pensize(i)
            doug.color(0,i,i)
    else:
         for i in range(0,255,10):
            doug.forward(10)	#Move forward
            doug.pensize(i)
            doug.color(0,i,0)

     
def flower(color, num):
    i = 0
    count = 360 / num
    angle = 0
    while angle < 360:
        petal(color, angle)
        angle += count
            


def main():
    flower("green", 9)
    #flower("red" , 6)
    #flower("blue", 3)

main()
    








