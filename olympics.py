#Matthew Suriawinata
#2/9/18
#olympics.py - displays olympics rings


from ggame import *

red = Color(0xFF0000, 1) #this is the color red
green = Color(0x00FF00, 1)
blue = Color(0x0000FF, 0)
blue2 = Color(0x0000FF, 1)
black = Color(0x000000, 1) 
yellow = Color(0xffff00, 1)

blackOutline = LineStyle(20, black)
blueOutline = LineStyle(20, blue2)
redOutline = LineStyle(20, red)
yellowOutline = LineStyle(20, yellow)
greenOutline = LineStyle(20, green)



blackCircle = CircleAsset(50, blackOutline, blue) #radius, outline, fill
redCircle = CircleAsset(50, redOutline, blue) #radius, outline, fill
yellowCircle = CircleAsset(50, yellowOutline, blue) #radius, outline, fill
greenCircle = CircleAsset(50, greenOutline, blue) #radius, outline, fill
blueCircle = CircleAsset(50, blueOutline, blue) #radius, outline, fill




Sprite(blueCircle, (0, 0))
Sprite(yellowCircle, (80, 80))
Sprite(redCircle, (300, 0))
Sprite(greenCircle, (220, 80))
Sprite(blackCircle, (150, 0))


App().run() 



