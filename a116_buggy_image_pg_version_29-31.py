#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used

#   This is to draw the spiders body

spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)


#  This draws the spidders head
spider.goto(0,-25)
spider.pensize(10)
spider.circle(10)

#   This is to configure the spiders legs

spider_legs = 8
spider_leg_length = 70
leg_angle = 240 / spider_legs
print("Leg Angle =", leg_angle)
spider.pensize(5)
number_of_legs= 0


#   This is to draw the spiders legs
while (number_of_legs < spider_legs / 2):
  spider.goto(0,20)
  spider.setheading(leg_angle*number_of_legs - 45)
  spider.forward(spider_leg_length)
  number_of_legs = number_of_legs + 1
  print("Leg Angle*Number Of Legs=", leg_angle*number_of_legs)

number_of_legs = 0

while (number_of_legs < spider_legs / 2):
  spider.goto(0,20)
  spider.setheading(leg_angle*number_of_legs - 45 + 180)
  spider.forward(spider_leg_length)
  number_of_legs = number_of_legs + 1
  print("Leg Angle*Number Of Legs=", leg_angle*number_of_legs)

# Draw eyes
spider.penup()
spider.pencolor("white")
spider.fillcolor("white")
spider.goto(-10,-25)
spider.pendown()
spider.begin_fill()
spider.circle(3)
spider.end_fill()
spider.penup()
spider.goto(10,-25)
spider.pendown()
spider.begin_fill()
spider.circle(3)
spider.end_fill()

spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()
