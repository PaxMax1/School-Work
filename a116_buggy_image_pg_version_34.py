#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()

ladybug_legs = 6
ladybug_leg_length = 50
leg_angle = 240 / ladybug_legs
ladybug.pensize(5)
number_of_legs= 0


#   This is to draw the spiders legs
while (number_of_legs < ladybug_legs / 2):
  ladybug.goto(0,-30)
  ladybug.setheading(leg_angle*number_of_legs - 45)
  ladybug.forward(ladybug_leg_length)
  number_of_legs = number_of_legs + 1
  print("Leg Angle*Number Of Legs=", leg_angle*number_of_legs)

number_of_legs = 0

while (number_of_legs < ladybug_legs / 2):
  ladybug.goto(0,-30)
  ladybug.setheading(leg_angle*number_of_legs - 45 + 180)
  ladybug.forward(ladybug_leg_length)
  number_of_legs = number_of_legs + 1
  print("Leg Angle*Number Of Legs=", leg_angle*number_of_legs)

ladybug.penup()
ladybug.goto(0,0)
ladybug.pendown()
ladybug.setheading(0)
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()
