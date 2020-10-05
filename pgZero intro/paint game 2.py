  
#-----------------------------------------------------------------------------
# Name:        Paint Game
# Purpose:     Get started with pygame zero
#
# Author:      Daniel
# Created:     05-Oct-2020
# Updated:     05-Oct-2020
#-----------------------------------------------------------------------------

gameState = ''
clear = True
def startUp():
    '''Run this to get the program ready to run'''
    global gameState

    gameState = 'start screen'
    

def on_key_up(key):
    '''Check to see if a key has been released'''
    global gameState #Make sure you make globals if necessary
    
    if key == keys.A:
        gameState = 'paint'
        screen.clear
    
    elif key == keys.E:
        gameState = 'end'

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
    '''Draw loop for all the graphical elements to display'''

    if gameState == "start screen":
        screen.clear()
        screen.fill((255, 255, 255))
        screen.draw.text("Hello, Welcome to my program", (25, 30), color="orange")
        screen.draw.text("Press A to start painting", (25, 70), color="red")

        
    elif gameState == "paint":
        global brushLocation
        global drawEnabled
        global clear
        screen.draw.text("Press E to leave", (25, 70), color="red")
        if clear == True:
            screen.clear
            screen.fill((173,216,230))
        if drawEnabled == True:
            screen.draw.circle(brushLocation, 3, 'purple')
            clear = False
            
    elif gameState == "end":
        screen.clear()
        screen.fill((255, 182, 193))
        screen.draw.text("Thanks For Plyaing", (300, 300), color="cyan")

    else:
        screen.clear()
        screen.fill((255, 255, 255))
        screen.draw.text("Error, no game state loaded", (25, 30), color="orange")


startUp()