#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl


wn = trtl.Screen()
wn.screensize(canvwidth = .75, canvheight=.75)

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
#creates turtle on the left side of the screen
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)
#creates turtles at the top of the screen
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

steps = 0
while steps < 50:
    steps = steps + 1
    for t in horiz_turtles:
        t.forward(10)
    for t in vert_turtles:
        t.forward(10)
    
    for h in horiz_turtles:
        for v in vert_turtles:
            xdistance = abs(h.xcor()-v.xcor())
            ydistance = abs(h.ycor()-v.ycor())
            if xdistance < 20 and ydistance < 20:
                #stop turtles
                h.fillcolor("grey")
                h.backward(15)
                if xdistance < 10 and ydistance < 10:
                    t.forward(16)
                v.fillcolor("grey")
                v.backward(300)
                if xdistance > 40 and ydistance > 40:
                    t.forward(8)


wn.mainloop()
