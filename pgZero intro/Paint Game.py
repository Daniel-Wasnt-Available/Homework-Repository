#-----------------------------------------------------------------------------
# Name:        New File Generator (newFile.py)
# Purpose:     Generates a new file for use in the ICS3U course
#
# Author:      Mr. Brooks
# Created:     13-Sept-2020
# Updated:     13-Sept-2020
#-----------------------------------------------------------------------------
WIDTH = 700
HEIGHT = 600
x = 10
red = (255,0,0)
green = (0,200,0)
brushLocation = (400,300)
BOX = Rect((300, 500), (100, 50))

def on_mouse_move(pos, rel, buttons):
    global brushLocation
    brushLocation = pos
    print(buttons)


def draw():
    global brushLocation
    import random
    #screen.clear()
    x == random.randint(5,20)
    screen.draw.circle(brushLocation,x,'red')
    screen.draw.filled_rect(BOX, (0,200,0))
    screen.draw.text("Exit",centery=530,right=365)
#still trying to make a button
#def on_mouse_down(BOX):
    #screen.draw.text("HI",centery=250,right=300)
    
