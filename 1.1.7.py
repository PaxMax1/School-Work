#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl
# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  c = turtle_colors.pop()
  t.color(c)
  my_turtles.append(t)



#  
startx = 0
starty = 0
direction = 45

#
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  t.right(direction)     
  t.forward(100)
 
  

#	
  startx = t.xcor()
  starty = t.ycor()
  direction = direction + 45


wn = trtl.Screen()
wn.mainloop()
