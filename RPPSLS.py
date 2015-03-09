#2/28/2015 python 1 - project 1
#http://www.codeskulptor.org/#user39_tkGVm5EmXK_0.py


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


import random

# 1st helper function
def name_to_number(name):
    # delete the following pass statement and fill in your code below
    # convert name to number using if/elif/else
    if name == 'rock':
        number = 0
    elif name == 'spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print 'ERROR name doesnt = number'
        number = None
    return number    

'''
test first function
number = name_to_number('spock')    
print number
'''

# 2nd helper function
def number_to_name(number):
    # convert number to a name using if/elif/else
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizzard'
    elif number == 4:
        name = 'scissors'
    else:
        print 'ERROR number dosent = name'
        name = None
    return name    
  
'''
test 2nd function
name = number_to_name(9)
print name
'''

# main function
def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print ''
    print ''

    # print out the message for the player's choice
    print 'Player chooses '+ player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,4)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print 'Computer chooses ' + comp_choice
    
    # compute difference of comp_number and player_number modulo five
    # Bonus. Catches input errors
    if comp_number == None:
        print 'ERROR (comp input) - no winners'
        winnbr = None
    elif player_number == None:
        print 'ERROR (player input) - no winners'
        winnbr = None
    else:
        winnbr = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if winnbr == None:
        print ''
    elif winnbr == 1:
        print 'Computer wins! ' #+ str(winnbr)
    elif winnbr == 2:
        print 'Computer wins! ' #+ str(winnbr)
    elif winnbr == 3:
        print 'Player wins! ' #+ str(winnbr)
    elif winnbr == 4:
        print 'Player wins! ' #+ str(winnbr)
    elif winnbr == 0:
        print 'tie' #+ str(winnbr)
    else:
        print 'does not compute'

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
#see what happens if input is incorrect
rpsls("Tom")

# always remember to check your completed program against the grading rubric


