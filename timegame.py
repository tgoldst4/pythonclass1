#http://www.codeskulptor.org/#user39_NazZ21ZcF3_1.py

# python 1 3/11/15
# template for "Stopwatch: The Game"
import simplegui
import math

# define global variables
t = 0.0 #tenth of a sec
fail=0
success=0
msm="00:00.0" # minutes seconds milliseconds
millis=0 #integer tenth of a second
timestamp="A" #no cheaters
tries=0 #count the number of trie instead of win lose
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D &score
def format(t):
    global millis,msm
    minutes = int(t//60)
    seconds = int(t//1)-minutes*60
    millis = int(10*(t-math.trunc(t))) 
    
    if seconds <10:
        seconds="0"+str(seconds)
    if minutes <10:
        minutes="0"+str(minutes)
    msm= str(minutes)+ ":"+str(seconds)+"."+str(millis)
     
# define event handlers for buttons; "Start", "Stop", "Reset"
def fxstart():
    global timestamp
    timestamp="0"
    timer.start()
      
def fxstop():
    global timestamp,msm
    if timestamp==msm or timestamp =="A":
        return
    else:
        timer.stop()
        game()
    
def game(): 
    global tries, fail,success, millis,timestamp,msm
    tries +=1
    if millis==0.0:
        success+=1
        timestamp=msm
    else:
        fail+=1
        timestamp=msm

def fxreset():
    global tries,t, fail, success,timestamp,msm
    t=0
    format(t)
    fail=0
    success=0
    timestamp="0"
    tries = 0
    timestamp=msm
    #reset doesnt stop watch, traditional
    timer.stop()#allows reset to stop watch
    
# define event handler for timer with 0.1 sec interval
def fxtimer():
    global t
    t += .1
    format(t)    

# define draw handler
def draw(canvas):
    global t, fail, msm, success
    canvas.draw_text(str(msm), [15,60],20,"white")
    canvas.draw_text("score: "+str(success)+"/"+str(tries), [20,10],15,"brown")
    
# create frame
frame = simplegui.create_frame("Timer", 100,100)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start",fxstart,100)
frame.add_button("Stop",fxstop,100)
frame.add_button("Reset",fxreset,100)
timer = simplegui.create_timer(100,fxtimer)

# start frame
frame.start()


