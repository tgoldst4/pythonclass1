# 3/4/2015 mini project 2 python 1
#http://www.codeskulptor.org/#user39_6Pski2PC6f_2.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math



# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global nbr_range, count, secret_num
    print "New game. Range is from " + str(nbr_range)
    print "Number of remaining guesses is " + str(count)
    print""
        # remove this when you add your code    
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global nbr_range, count, secret_num
    secret_num = random.randint(0,100)
    nbr_range = "0 to 100"
    count = 7
    new_game()
    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global nbr_range, count, secret_num
    secret_num = random.randint(0,1000)
    nbr_range = "0 to 1000"
    count = 10
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    global count, secret_num
    
    #catch input err
    try:
        float(guess)
    except ValueError:
        print "invalid guess"
        return
          
    print "Guess was " + guess
    
    #test secret nbr
    #print "secret # is " + str(secret_num)
    if secret_num > float(guess) and count >1:
        count -= 1
        print "Number of remaining guesses is " + str(count)
        print "Higher"
        print""
    elif secret_num < float(guess) and count > 1:
        count -= 1
        print "Number of remaining guesses is " + str(count)
        print "Lower"
        print""
    elif secret_num == float(guess) and count >0: 
        print "Correct"
        print""
        range100() #remove this if you want to use the play again butt
    else:
        print "Game Over. You Lose"
        print ""
        range100()
        
  
       
    # remove this when you add your code
def quitt():
    print "Goodbye"
    quit()

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_input("Enter a guess",input_guess, 200)
frame.add_button("Range is (0, 100)", range100, 200)
frame.add_button("Range is (0, 1000)", range1000, 200)

frame.add_button("Play Again", range100,100)
frame.add_button("Quit", quitt, 100)
# call new_game 
frame.start()
range100()

# always remember to check your completed program against the grading rubric
