# Implementation of classic arcade game Pong
#Travis 3/22/15 python 1 class
#http://www.codeskulptor.org/#user39_mrXeadaGHl_0.py

import simplegui
import random
import math
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
PAD_WIDTH = 8
PAD_HEIGHT = 80
'''paddles are 60 length'''
paddle1_pos=[[0,HEIGHT/2-30],[0,HEIGHT/2+30],[PAD_WIDTH, HEIGHT/2+30], [PAD_WIDTH,HEIGHT/2-30]] 
paddle2_pos=[[WIDTH,HEIGHT/2-30],[WIDTH,HEIGHT/2+30],[WIDTH-PAD_WIDTH, HEIGHT/2+30], [WIDTH-PAD_WIDTH,HEIGHT/2-30]]
ball_pos=[WIDTH/2,HEIGHT/2]
'''15R is half paddle length'''
ball_radius=5 
paddle2_vel=0
paddle1_vel=0
top1=0
top2=0
ball_vel = [-0.0 / 60.0,  0.0 / 60.0]
scoreleft=0
scoreright=0



# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]
    ball_vel = [direction,random.randint(-5,-1)]
    ball_radius=5

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global scoreleft, scoreright, top1, top2  # these are ints
    #calls spawn ball
    spawn_ball(random.choice([-1,1]))
    paddle1_vel=0
    paddle2_vel=0
    scoreleft=0
    scoreright=0
    top1=0
    top2=0
    paddle1_pos=[[0,HEIGHT/2-30],[0,HEIGHT/2+30],[PAD_WIDTH, HEIGHT/2+30], [PAD_WIDTH,HEIGHT/2-30]] 
    paddle2_pos=[[WIDTH,HEIGHT/2-30],[WIDTH,HEIGHT/2+30],[WIDTH-PAD_WIDTH, HEIGHT/2+30], [WIDTH-PAD_WIDTH,HEIGHT/2-30]]


def draw(canvas):
    global scoreright,scoreleft, ball_radius,  top1,top2,score1, score2
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel, HEIGHT, paddle1_vel, paddle2_vel
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, ball_radius,2,'red','white')
    # update paddle's vertical position, keep paddle on the screen
    # paddle keeps moving while keys are held down and stops when key release
    top1+=paddle1_vel
    top2+=paddle2_vel
    paddle1_pos=[[0,HEIGHT/2-30+top1],[0,HEIGHT/2+30+top1],[PAD_WIDTH, HEIGHT/2+30+top1], [PAD_WIDTH,HEIGHT/2-30+top1]] 
    paddle2_pos=[[WIDTH,HEIGHT/2-30+top2],[WIDTH,HEIGHT/2+30+top2],[WIDTH-PAD_WIDTH, HEIGHT/2+30+top2], [WIDTH-PAD_WIDTH,HEIGHT/2-30+top2]]

    if list(paddle1_pos[0])[1] < 0:
        paddle1_pos=[[0,0],[0,60],[PAD_WIDTH, 60], [PAD_WIDTH,0]] 
        top1 = -(200-30)
        paddle1_vel=0
    elif list(paddle1_pos[1])[1] > HEIGHT:  
        paddle1_pos=[[0,400-60],[0,400],[PAD_WIDTH, 400], [PAD_WIDTH,400-60]] 
        top1 = (200-30)   
        paddle1_vel=0
    elif list(paddle2_pos[0])[1] < 0:
        paddle1_pos=[[WIDTH,0],[WIDTH,60],[WIDTH-PAD_WIDTH, 60], [WIDTH-PAD_WIDTH,0]] 
        top2 = -(200-30)
        paddle2_vel=0
    elif list(paddle2_pos[1])[1] > HEIGHT:  
        paddle1_pos=[[WIDTH,400-60],[WIDTH,400],[WIDTH-PAD_WIDTH, 400], [WIDTH-PAD_WIDTH,400-60]] 
        top2 = (200-30)    
        paddle2_vel=0
    
    # draw paddles
    canvas.draw_polygon( paddle1_pos, 1,'white', 'white')
    canvas.draw_polygon( paddle2_pos, 1,'white', 'white')
    
    # determine whether paddle and ball collide
    # paddle hits increase velocity of ball each time
    if ball_pos[0]-ball_radius <= PAD_WIDTH:
        if ball_pos[1]-ball_radius >= list(paddle1_pos[0])[1] and ball_pos[1]+ball_radius <= list(paddle1_pos[1])[1]:
            ball_vel[0]= - ball_vel[0]
            ball_pos[0]=PAD_WIDTH+ball_radius
            faster()
            print "hit left"
        else:
            scoreright +=1
            spawn_ball(1)
    elif ball_pos[0]+ball_radius >= WIDTH-PAD_WIDTH:
        if ball_pos[1]-ball_radius >= list(paddle2_pos[0])[1] and ball_pos[1]+ball_radius <= list(paddle2_pos[1])[1]:
            ball_vel[0]= - ball_vel[0]
            ball_pos[0]=WIDTH-PAD_WIDTH-ball_radius
            faster()
            print "hit right"
        else:
            scoreleft+=1
            spawn_ball(-1)
  
    elif ball_pos[1] <= ball_radius:
        ball_pos[1] = ball_radius
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT-1)-ball_radius:  
        ball_pos[1] = (HEIGHT-1)-ball_radius
        ball_vel[1] = -ball_vel[1]   
    
    # draw scores
    canvas.draw_text("Score P1:"+str(scoreleft), (60,20),20,'red')
    canvas.draw_text("Score P2:"+str(scoreright), (WIDTH-150,20),20,'red')
    
def faster():
    global ball_vel
    ball_vel[0]+=float(ball_vel[0]*.5)  
    ball_vel[1]+=float(ball_vel[1]*.5)   
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    #p1
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 5
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 5   
    #p2
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 5
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 5   
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
   
     #p1
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0 
    #p2
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0  
    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
new = frame.add_button('Restart',new_game)

# start frame
new_game()
frame.start()
