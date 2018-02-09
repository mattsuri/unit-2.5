#Matthew Suriawinata
#2/8/18
#germany.py - displays a german flag


from ggame import *

red = Color(0xFF0000, 1) #this is the color red
green = Color(0x00FF00, 1)
blue = Color(0x0000FF, 1)
black = Color(0x000000, 1) 
yellow = Color(0xFCE770, 1)

blackOutline = LineStyle(1, black)


yellowRectangle = RectangleAsset(100, 30, blackOutline, yellow) #(wdith, height, outline, fill)
redRectangle = RectangleAsset(100, 30, blackOutline, red) #(wdith, height, outline, fill)
blackRectangle = RectangleAsset(100, 30, blackOutline, black) #(wdith, height, outline, fill)



Sprite(yellowRectangle, (0,60))
Sprite(redRectangle, (0,30))
Sprite(blackRectangle, (0,0))

App().run() 


