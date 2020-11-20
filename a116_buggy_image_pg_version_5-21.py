#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
spider_legs = 8
spider_leg_length = 70
leg_angle = 380 / spider_legs
print("Leg Angle =", leg_angle)
spider.pensize(5)
number_of_legs= 0
while (number_of_legs < spider_legs):
  spider.goto(0,0)
  spider.setheading(leg_angle*number_of_legs)
  spider.forward(spider_leg_length)
  number_of_legs = number_of_legs + 1
  print("Leg Angle*Number Of Legs=", leg_angle*number_of_legs)
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
