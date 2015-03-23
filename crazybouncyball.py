import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
time = 1

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-0.0 / 60.0,  0.0 / 60.0]

# define event handlers
def draw(canvas):
    global WIDTH
    global HEIGHT
    global vel
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        ball_pos[0] = BALL_RADIUS
        vel[0] = - vel[0]
    elif ball_pos[0] >= (WIDTH-1)-BALL_RADIUS:  
        ball_pos[0] = (WIDTH-1)-BALL_RADIUS
        vel[0] = -vel[0]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_pos[1] = BALL_RADIUS
        vel[1] = - vel[1]
    elif ball_pos[1] >= (HEIGHT-1)-BALL_RADIUS:  
        ball_pos[1] = (HEIGHT-1)-BALL_RADIUS
        vel[1] = -vel[1]   
    slower()
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    print vel, time
    
def slower():
    global vel
    vel[0]+=float(-vel[0]*.01)  
    vel[1]+=float(-vel[1]*.01)

def keydown(key):
            
    if key == simplegui.KEY_MAP["left"]:
        vel[0] -= 10
    elif key == simplegui.KEY_MAP["right"]:
        vel[0] += 10
    elif key == simplegui.KEY_MAP["down"]:
        vel[1] += 10
    elif key == simplegui.KEY_MAP["up"]:
        vel[1] -= 10      
        
'''def keyup(key):
    global vel
       
    if key == simplegui.KEY_MAP["left"]:
        vel[0] -= time
    elif key == simplegui.KEY_MAP["right"]:
        vel[0] += time
    elif key == simplegui.KEY_MAP["down"]:
        vel[1] += time
    elif key == simplegui.KEY_MAP["up"]:
        vel[1] -= time          
'''


# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
#frame.set_keydown_handler(keyup)

# start frame
frame.start()
