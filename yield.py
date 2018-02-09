#Matthew Suriawinata
#2/9/18
#yield.py - Displays yield sign


from ggame import *

red = Color(0xFF0000, 1) #this is the color red
green = Color(0x00FF00, 1)
blue = Color(0x0000FF, 1)
black = Color(0x000000, 1) 
white = Color(0xFFFFFF, 1)

blackOutline = LineStyle(1, black)
whiteOutline = LineStyle(1, white)

redRectangle = RectangleAsset(200, 100, blackOutline, red) #(wdith, height, outline, fill)


whiteTriangle = PolygonAsset([(0,0), (120,0), (60,90)], whiteOutline, white) #endpoints, outline, fill


redTriangle = PolygonAsset([(0,0), (240,0), (120,180)], whiteOutline, red) #endpoints, outline, fill
text = TextAsset("Yield", fill=black, style="bold 16pt Times") #Texxt, other options


Sprite(redTriangle)
Sprite(whiteTriangle, (60,30))
Sprite(text, (95, 60))




App().run() 



