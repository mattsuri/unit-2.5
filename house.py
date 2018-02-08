#Matthew Suriawinata
#2/8/18
#house.py - displays a house


from ggame import *

red = Color(0xFF0000, 1) #this is the color red
green = Color(0x00FF00, 1)
blue = Color(0x0000FF, 1)
black = Color(0x000000, 1) 
yellow = Color(0xFCE770, 1)

blackOutline = LineStyle(1, black)

redTriangle = PolygonAsset([(0,120), (120,120), (60,0)], blackOutline, red) #endpoints, outline, fill
yellowRectangle = RectangleAsset(120, 100, blackOutline, yellow) #(wdith, height, outline, fill)
yellowRectangle2 = RectangleAsset(30, 60, blackOutline, yellow) #(wdith, height, outline, fill)
blackCircle = CircleAsset(5, blackOutline, black) #radius, outline, fill

Sprite(redTriangle)
Sprite(yellowRectangle, (0,120))
Sprite(yellowRectangle2, (45,160))
Sprite(blackCircle, (60, 185))

App().run() 