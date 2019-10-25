# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration----
turtleshape = "turtle"
turtlesize = 5
turtlecolor = "purple"

score = 0

timer = 5

#-----initialize turtle-----
carl = trtl.Turtle(shape=turtleshape)
carl.color(turtlecolor)
carl.shapesize(turtlesize)
carl.speed(0)

score_board = trtl.Turtle()

counter = trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(300,275)
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----game functions--------
def carl_clicked(x,y):
    print("Carl was clicked.")
    change_position()
    update_score()
   
def change_position():
    carl.penup()
    carl.ht()
    if not timer_up:
      carlx = random.randint(-400,500)
      carly = random.randint(-300,300)
      carl.goto(carlx,carly)
      carl.st()

score_board.ht()
score_board.penup()
score_board.goto(-370,270)
font_setup = ("Verdana", 30,)
score_board.write(score, font=font_setup)

def update_score():
    global score
    score += 1
    print(score)
    score_board.clear()
    score_board.write(score, font=font_setup)

timer = 5
counter_interval = 1000
timer_up = False

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----events----------------
wn = trtl.Screen()
wn.bgcolor("yellow")
carl.onclick(carl_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()