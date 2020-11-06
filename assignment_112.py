print("Circle Drawer")


user_name = input("What is your name?")
print("Hello", user_name,".")

color_answer = input("What color would you like your circle to be? Make sure its a color and not something else.")

size = int (input("What would you like the radius size of your circle to be? Make sure its a number and not a word."))
print("Ok")

width = int (input("How wide do you want the pen line to be? Again only a number."))
print("Ok, I will make you a", color_answer, "circle with a radius of", size," and a width of", width,".")

import turtle as trtl

painter = trtl.Turtle()

painter.pensize(width)

painter.pencolor(color_answer)

painter.circle(size,360)
 
wn = trtl.Screen()
wn.mainloop()

