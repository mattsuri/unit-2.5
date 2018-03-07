#Matthew Suriawinata
#2/7/18
#graphicsDemo.py - Intro to ggame

from ggame import *

red = Color(0xFF0000, 1) #this is the color red
green = Color(0x00FF00, 1)
blue = Color(0x0000FF, 1)
black = Color(0x000000, 1) 
white = Color(0xFFFFFF, 1)
blank = Color(0xFFFFFF, 0)


blackOutline = LineStyle(1, black)
blueOutline = LineStyle(1, blue)

blueRectangle = RectangleAsset(300, 33, blueOutline, blue) #(wdith, height, outline, fill)
blueRectangle2 = RectangleAsset(300, 33, blueOutline, blue) #(wdith, height, outline, fill)


blueTriangle = PolygonAsset([(500,1000), (600,1000), (550,1100)], blueOutline, blank) #endpoints, outline, fill


Sprite(blueRectangle)
Sprite(blueRectangle, (0, 166))



Sprite(blueTriangle)


App().run() 
