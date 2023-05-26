##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu   


#TODO: make sure that user only input choice 1-3.
def validFeedback():
    #TODO: print prompt "1. too small   2. too big  3. just right"

    print("1: too small   2: too big   3: just right")

    #Ask user to input feedback as an integer in 1-3,
    #the input prompt MUST be "Enter choice 1-3: " 
    #if you want to see choice chosen in gradescript.
    
    feedback = int(input("Enter choice 1-3: "))
    if feedback == 1:
        boolean = True
    elif feedback == 2:
        boolean = True
    elif feedback == 3:
        boolean = True
    else:
        boolean = False
    while boolean == False:
        feedback = int(input("Enter choice 1-3: "))
        if feedback == 1:
            boolean = True
        elif feedback == 2:
            boolean = True
        elif feedback == 3:
            boolean = True
        else:
            boolean = False
    return feedback

def guessGame():
    start = 0
    end = 100

    print("Pick an integer in [" + str(start) + ", " + str(end) + "] in your mind.")

    #TODO: set guess to be mid of start and end
    guess = (start + end) // 2
    #TODO: set variable numGuesses to be 1 
    numGuesses = 1
    print("Guess " + str(numGuesses) + ": is it " + str(guess) + "?")

    #TODO: call validFeedback function, put its return to feedback
    feedback = validFeedback()
    #user does not choose "3. just right" yet
    while feedback is not 3: 
        if feedback is 1: #too small
           start = guess 
        else: 
            end = guess

        #TODO: put the mid point of start and end to guess
        guess = (start + end) // 2
        #TODO: increase numGuesses by 1
        numGuesses = 1
        if start == end:
           print("Guess " + str(numGuesses) + ": the answer must be", guess)
           #TODO: leave the current function 
           #by calling return statement, 
           #since we find the answer
           #and finish guess game now. 

        print("Guess " + str(numGuesses) + ": is it " + str(guess) + "?")
        
        #TODO: call validFeedback function, 
        #put its return to feedback
        feedback = validFeedback()

    #TODO: now we are outside the loop, the number is guessed
    #print out Congratulations and what the value of guess is.
    print("Congratulations! The answer is ", guess)

def main():
    guessGame()
    
if __name__ == '__main__':
   main()
