#a121_catch_a_turtle_[bf].py
# a121_catch_a_turtle.py
#-----import statements-----(20min)
import turtle as trtl

#-----game configuration----(3hr)
spot_color="pink"
spot_shape="circle"
spot_size=2

#-----initialize turtle-----(1hr)
spot=trtl.Turtle()

spot.shape(spot_shape)
spot.color(spot_color)
spot.shapesize(spot_size)
#-----game functions--------(1hr)


#-----events----------------(4hr)
def spot_clicked(x,y):
 print("hey")
spot.onclick(spot_clicked)


wn = trtl.Screen()
wn.mainloop()