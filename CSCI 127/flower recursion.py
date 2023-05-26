##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: November 7th 2022


import turtle

def flowerRecursion(turt, number):
    wn = turtle.Screen()
    if number > 0:
       turt.forward(100)
       turt.left(105)
       turt.forward(52)
       turt.left(105)
       turt.forward(100)
       turt.right(170)
       flowerRecursion(turt, number-1)
    wn.exitonclick()


def main():
    #call flowerRecursion function to draw a flower
    doug = turtle.Turtle()
    flowerRecursion(doug, 9)
    
if __name__ == '__main__':
   main()


        
