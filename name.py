#Matthew Suriawinata
#2/9/18
#graphicsDemo.py - Intro to ggame

from ggame import *

colorCode= input("Input a hex color code: ")
name = input("Enter your name: ")



pickedColor = Color(colorCode, 1) 



blackOutline = LineStyle(1, black)

redRectangle = RectangleAsset(1000, 1000, blackOutline, pickedColor) #(wdith, height, outline, fill)

text = TextAsset(name , fill=black, style="bold 100- pt Times") #Texxt, other options

Sprite(redRectangle)

Sprite(text, (300,300))

App().run() 



