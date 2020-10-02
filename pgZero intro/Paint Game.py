#-----------------------------------------------------------------------------
# Name:        New File Generator (newFile.py)
# Purpose:     Generates a new file for use in the ICS3U course
#
# Author:      Mr. Brooks
# Created:     13-Sept-2020
# Updated:     13-Sept-2020
#-----------------------------------------------------------------------------

x = 10
brushLocation = (400,300)
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
    
