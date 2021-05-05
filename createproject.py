import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
import random
from PIL import Image,ImageTk

#IMPORTANT Gui must have 2 image buttons, that refer to product1.png product2.png, space for both product names and hidden prices and title at the top saying "which costs more"
#must be able to reset gui to play another round

# Declare Root
root = tk.Tk()
root.title("Amazon Guessing Game")
# Define Frames
gameFrame = tk.Frame(root)
imageFrame1 = tk.Frame(root)
imageFrame2 = tk.Frame(root)
price1Frame = tk.Frame(root)
price2Frame = tk.Frame(root)
frameList = [gameFrame, imageFrame1, imageFrame2, price1Frame, price2Frame]

# Configure all Frames
for frame in frameList:
	frame.grid(row=0, column=0, sticky='news')
	frame.configure(bg='white')
root.wm_geometry("1413x500")
gameFrame.winfo_height=500
gameFrame.winfo_width=1000
root.configure(bg="white")
# Product Descriptions
productdescription1 = "hi"
productdescription2 = "hi"

# Price Variables
price1="price1"
price2="price2"

# Frame Raise Function
def raiseFrame(frame):
	frame.tkraise()


# Move To Reg Function
def moveToproduct1():
	raiseFrame(imageFrame1)


def moveToproduct2():
	raiseFrame(gameFrame)

def dummy():
        print("hi")

# Fonts
titleFont = Font(family="Arial", size="48")
labelFont = Font(family="Arial", size="24")
buttonFont = Font(family="Arial", size="20")
helpfont = Font(family="Ariel", size="36")

'''
#Define Image
product1buttonimage=Image.open("200pixref.jpg")
product1buttonimageph=ImageTk.PhotoImage(product1buttonimage)
product2buttonimage=Image.open("200pixref.jpg")
product2buttonimageph=ImageTk.PhotoImage(product2buttonimage)
'''

# Labels
titleLabel = tk.Label(gameFrame, text="$ Which Costs More? $", font=titleFont, fg='green', bg='light green')
titleLabel.grid(row=1, column=1, columnspan=5)
instructionLabel = tk.Label(gameFrame, text="Click on the product that you think costs more!", bg='white', font=helpfont)
instructionLabel.grid(row=2, column=1, columnspan=5)
price1Label = tk.Label(gameFrame, text= price1, font=helpfont, bg='white', fg='gold')
price1Label.grid(row=4, column=1)
price2Label = tk.Label(gameFrame, text= price2, font=helpfont, bg='white', fg='gold')
price2Label.grid(row=4, column=5)

# Buttons
image2Button = tk.Button(imageFrame2, command=dummy, font=buttonFont, text= productdescription2)
image2Button.grid(row=5, column=5, padx=20, pady=20 )
image1Button = tk.Button(imageFrame1, command=dummy, font=buttonFont, text= productdescription1)
image1Button.grid(row=7, column=2,)
restartButton = tk.Button(gameFrame, command=dummy, text="Restart", font = buttonFont)
restartButton.grid(row=5, column=3)
moveToimage1Button = tk.Button(gameFrame, command=dummy, font=buttonFont, text=productdescription1, width=40)
moveToimage1Button.grid(row=5, column=1)
moveToimage2Button = tk.Button(gameFrame, command=dummy, font=buttonFont, text=productdescription1, width=40)
moveToimage2Button.grid(row=5, column=5)

# Window Launch
raiseFrame(gameFrame)
root.mainloop()
