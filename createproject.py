import tkinter as tk
from tkinter.font import Font
from tkinter import *
import random
import requests
from bs4 import BeautifulSoup

# Set Up Tkinter Root
root = tk.Tk()
root.title("Amazon Guessing Game")

# Grab HTML with BS4
data = BeautifulSoup(requests.get('http://imfeelingprimey.com').text, features="lxml")
  
# Find product list from I'm Feeling Primey HTML and add them to a python list
data1 = data.find('ul')
products = []
for li in data1.find_all("li"):
    products.append(li.text)

# Generate a usable random product from the product list and clean up the string and set Tkinter Vars
def genbothproducts():
	product1gen()
	product2gen()
	global product1split
	global product2split
	global price1split
	global price2split
	product1splitstart = str(product1).split(" #", 1)
	product2splitstart = str(product2).split(" #", 1)
	product1split = str(product1splitstart[0]).split("         ", 1)
	product2split = str(product2splitstart[0]).split("         ", 1)
	strvarproduct1.set(str(product1split[1]))
	strvarproduct2.set(str(product2split[1]))
	price1split = str(product1).split("reviews   ", 1)
	price2split = str(product2).split("reviews   ", 1)
	price1.set(str(price1split[1]))
	price2.set(str(price2split[1]))

# Reset labels, reset button commands, restart tkinter and generate products
correcttxt="hai bkguvtuhjcurTYVASTYAVSYUCVUYA DYASOY SA"
def restart():
	price1Label.config(fg='white')
	price2Label.config(fg='white')
	correctLabel.config(fg='white')
	product1button.config(command=choice1)
	product2button.config(command=choice2)
	root.update
	genbothproducts()

# Generate Product 1
def product1gen():
	global product1
	product1 = (random.choice(products))
	# Filter products without prices
	if "$" not in str(product1):
		product1gen()
	# Filter products that have multiple prices
	if " - $" in str(product1):
		product1gen()

#Generate Product 2
def product2gen():
	global product2
	product2 = (random.choice(products))
	# Filter products without prices
	if "$" not in str(product2):
		product2gen()
	# Filter products that have multiple prices
	if " - $" in str(product2):
		product2gen()

# Initialize Tkinter stringvars
strvarproduct1 = tk.StringVar()
strvarproduct2 = tk.StringVar()
price1 = tk.StringVar()
price2 = tk.StringVar()
scorevar = tk.StringVar()
# And initialize score value for stringvar to use
global score
score = 0

# First product generation
genbothproducts()

# Left button's command
def choice1():
	global choice
	choice = 1
	calcchoice()

# Right button's command
def choice2():
	global choice
	choice = 2
	calcchoice()

# Calculate if your choice was right
def calcchoice():
	# Make prices visible
	price1Label.config(fg='gold')
	price2Label.config(fg='gold')
	correctLabel.config(fg='blue')
	# Subtract cleaned up prices (subtract left option price from right option price)
	calc = int(float(((str((price1split[1])).replace('$','')).replace(' ','')).replace(',',''))) - int(float((((str(price2split[1])).replace('$','')).replace(' ','')).replace(',','')))
	product1button.config(command=restart)
	product2button.config(command=restart)
	root.update
	global choice
	global score
	# If answer is positive, choice 1 is right. If answer negative, choice 2 is right.
	# Change score accordingly, if the product prices are the same and calculation is equal to 0 do nothing to score.
	if calc > 0 and choice == 1:
		score = score + 1
		correctLabel.config(text = "Correct!", fg="green")
	elif calc < 0 and choice == 2:
		score = score + 1
		correctLabel.config(text = "Correct!", fg="green")
	elif calc < 0 and choice == 1:
		score = 0
		correctLabel.config(text = "Incorrect...", fg="red")
	elif calc > 0 and choice == 2:
		score = 0
		correctLabel.config(text = "Incorrect...", fg="red")
	# Update Tkinter score value so that it reflects on the GUI
	scorevar.set(str(score))

# Create frames for each widget on the gui
gameFrame = tk.Frame(root)
imageFrame1 = tk.Frame(root)
imageFrame2 = tk.Frame(root)
price1Frame = tk.Frame(root)
price2Frame = tk.Frame(root)
frameList = [gameFrame, price1Frame, price2Frame]

# Initialize frames to be visible
for frame in frameList:
	frame.grid(row=0, column=0, sticky='news')
	frame.configure(bg='white')

# Raise frames so that they aren't at the bottom of the window
def raiseFrame(frame):
	frame.tkraise()

# Fonts for buttons, title, and other text
titleFont = Font(family="Arial", size="48")
labelFont = Font(family="Arial", size="24")
buttonFont = Font(family="Arial", size="20")
helpfont = Font(family="Ariel", size="36")

# Labels
titleLabel = tk.Label(gameFrame, text="$ Which Costs More? $", font=titleFont, fg='green', bg='light green')
titleLabel.grid(row=1, column=1, columnspan=5)
instructionLabel = tk.Label(gameFrame, text="Click on the product that you think costs more!", bg='white', font=helpfont )
instructionLabel.grid(row=2, column=1, columnspan=5)
# Updatable Price Labels
price1Label = tk.Label(gameFrame, textvariable= price1, font=helpfont, bg='white', fg='white')
price1Label.grid(row=4, column=1)
price2Label = tk.Label(gameFrame, textvariable= price2, font=helpfont, bg='white', fg='white')
price2Label.grid(row=4, column=5)
#Updatable Correct/Incorrect Label
correctLabel = tk.Label(gameFrame, text= "", font=helpfont, bg='white', fg='green')
correctLabel.grid(row=10, column=1, columnspan=5)
# Updatable Score Label
scoreLabel = tk.Label(gameFrame, textvariable= scorevar, font=helpfont, bg='white', fg='cyan')
scoreLabel.grid(row=4, column=3)

# Buttons
restartButton = tk.Button(gameFrame, command=restart, text="Refresh", font = buttonFont)
restartButton.grid(row=5, column=3)
# Product buttons
product1button = tk.Button(gameFrame, command=choice1, font=buttonFont, textvariable=strvarproduct1, width=40)
product1button.grid(row=5, column=1)
product2button = tk.Button(gameFrame, command=choice2, font=buttonFont, textvariable=strvarproduct2, width=40)
product2button.grid(row=5, column=5)

# Initialize the window
raiseFrame(gameFrame)
root.mainloop()
