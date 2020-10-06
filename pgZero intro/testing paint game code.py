  
#-----------------------------------------------------------------------------
# Name:        Paint Game
# Purpose:     Get started with pygame zero
#
# Author:      Daniel
# Created:     05-Oct-2020
# Updated:     05-Oct-2020
#-----------------------------------------------------------------------------

WIDTH = 800
HEIGHT = 600
brushLocation = (400,300)
drawEnabled = False
ship = Actor('ship')
ship.pos = 0,0


gameState = ''

def startUp():
    '''Run this to get the program ready to run'''
    global gameState

    gameState == "start"
    
    
def on_key_up(key):
    '''Check to see if a key has been released'''
    global gameState #Make sure you make globals if necessary

    if key == keys.A:
        gameState = 'paint'

def on_mouse_move(pos, rel, buttons):
    global brushLocation
    global drawEnabled
    
    #Save the brush location (x and y) as it updates
    brushLocation = pos
    
    #Check for the left button to be pressed down
    if mouse.LEFT in buttons:
        print("Yay! The button was clicked")
        sounds.eep.play()
        drawEnabled = True
    else:
        drawEnabled = False


def draw():
    global gameState
    if gameState == "start":
        screen.clear()
        screen.fill((0, 0, 0))
        screen.draw.text("Hello, Welcome to my program", (0, 0), green)
        screen.draw.text("Press the secret key", (0, 0), red)
        
    elif gameState =='paint':
        screen.fill((173,216,230))
        global brushLocation
        global drawEnabled
        #screen.clear()
        if drawEnabled == True:
            screen.draw.circle(brushLocation, 3, 'purple')


startUp()
        
        
        
        