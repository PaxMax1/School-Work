#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()
apple_letter = "A"

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def draw_apple(active_apple):
  global apple_letter
  active_apple.pu()
  active_apple.shape(apple_image)
  wn.tracer(False)
  active_apple.setx(rand.randint(-175,175))
  active_apple.sety(rand.randint(0,100))
  apple_letter = letters[rand.randint(0,25)]
  active_apple.sety(active_apple.ycor()-30)
  active_apple.shape(apple_image)
  active_apple.color("white")
  active_apple.write(apple_letter, align="center",font=("Arial",40, "bold"))
  active_apple.sety(active_apple.ycor()+30)
  active_apple.showturtle()
  wn.tracer(True)
  wn.update()

def drop_apple():
  apple.pu()
  apple.clear()
  apple.sety(-150)
  apple.hideturtle
  draw_apple(apple)

def typea():
  if apple_letter == "A":
    drop_apple

def typeb():
  if apple_letter == "B":
    drop_apple

def typec():
  if apple_letter == "C":
    drop_apple

def typed():
  if apple_letter == "D":
    drop_apple

def typee():
  if apple_letter == "E":
    drop_apple

def typef():
  if apple_letter == "F":
    drop_apple

def typeg():
  if apple_letter == "G":
    drop_apple

def typeh():
  if apple_letter == "H":
    drop_apple

def typei():
  if apple_letter == "I":
    drop_apple

def typej():
  if apple_letter == "J":
    drop_apple

def typek():
  if apple_letter == "K":
    drop_apple

def typel():
  if apple_letter == "L":
    drop_apple

def typem():
  if apple_letter == "M":
    drop_apple

def typen():
  if apple_letter == "N":
    drop_apple

def typeo():
  if apple_letter == "O":
    drop_apple

def typep():
  if apple_letter == "P":
    drop_apple

def typeq():
  if apple_letter == "Q":
    drop_apple

def typer():
  if apple_letter == "R":
    drop_apple

def types():
  if apple_letter == "S":
    drop_apple

def typet():
  if apple_letter == "T":
    drop_apple

def typeu():
  if apple_letter == "U":
    drop_apple

def typev():
  if apple_letter == "V":
    drop_apple

def typew():
  if apple_letter == "W":
    drop_apple

def typex():
  if apple_letter == "X":
    drop_apple

def typey():
  if apple_letter == "Y":
    drop_apple

def typez():
  if apple_letter == "Z":
    drop_apple

#-----function calls-----
draw_apple(apple)

wn.onkeypress(type, "A")
wn.onkeypress(type, "B")
wn.onkeypress(type, "C")
wn.onkeypress(type, "D")
wn.onkeypress(type, "E")
wn.onkeypress(type, "F")
wn.onkeypress(type, "G")
wn.onkeypress(type, "H")
wn.onkeypress(type, "I")
wn.onkeypress(type, "J")
wn.onkeypress(type, "K")
wn.onkeypress(type, "L")
wn.onkeypress(type, "M")
wn.onkeypress(type, "N")
wn.onkeypress(type, "O")
wn.onkeypress(type, "P")
wn.onkeypress(type, "Q")
wn.onkeypress(type, "R")
wn.onkeypress(type, "S")
wn.onkeypress(type, "T")
wn.onkeypress(type, "U")
wn.onkeypress(type, "V")
wn.onkeypress(type, "W")
wn.onkeypress(type, "X")
wn.onkeypress(type, "Y")
wn.onkeypress(type, "Z")

wn.listen()

wn.mainloop()
