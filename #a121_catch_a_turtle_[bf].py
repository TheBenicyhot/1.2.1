#a121_catch_a_turtle_[bf].py
# a121_catch_a_turtle.py
#-----import statements-----(20min)
import turtle as trtl
import random as rand 
#-----game configuration----(3hr)
spot_color="pink"
spot_shape="circle"
spot_size=2
score=0
def update_score():
 global score # gives this function access to the score that was created above
 score += 1
 print(score)
#-----initialize turtle-----(1hr)
spot=trtl.Turtle()
spot.penup()
spot.shape(spot_shape)
spot.color(spot_color)
spot.shapesize(spot_size)
score_writer=trtl.Turtle()
#-----game functions--------(1hr)

def spot_clicked(x,y):
 change_position()



def change_position():
 new_xpos=rand.randint(1,400)
 new_ypos=rand.randint(1,300)
 spot.goto(new_xpos,new_ypos)
 update_score()
score_writer.goto(400.300)
#-----events----------------(4hr)

spot.onclick(spot_clicked)


wn = trtl.Screen()
wn.mainloop()