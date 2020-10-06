#-----------------------------------------------------------------------------
# Name:        Paint Game
# Purpose:     Get started with pygame zero
#
# Author:      Daniel
# Created:     05-Oct-2020
# Updated:     06-Oct-2020
#-----------------------------------------------------------------------------
WIDTH = 800
HEIGHT = 600
drawX=400
drawY=300
gameState = ''
clear = True
move = True

button1Draw = [drawX, drawY, 100, 50] #[left, top, width, size]
button1Rect = Rect(button1Draw) 
button1Value = True  #Give the button a vale
button1Color = 'green' #Give the buttton a color, can also use (r, g, b) sets
button2Draw = [100, 100, 100, 50] #[left, top, width, size]
button2Rect = Rect(button2Draw) 
button2Color = (255, 255, 255)

def startUp():
    '''Run this to get the program ready to run'''
    global gameState
    global drawY
    global drawX
    global move
    if move == True:
        drawX = drawX + 2
    
    gameState = 'start screen'
    
def on_mouse_up(pos, button):
    '''Pygame Special Event Hook - Runs when the mouse button is released'''
    global gameState
    global button1Color
    global button1Value
    global earase
    
    #screen.draw.text("Start",(WIDTH/2,HEIGHT/2),color="blue")
    if button1Rect.collidepoint(pos): 
        print("Button 1 Clicked!", button1Value)
       
        if  button1Value == True:
            gameState = 'paint'
            screen.clear

    if gameState == 'paint':
            if button1Rect.collidepoint(pos): 
                print("Button 1 Clicked!")
                earase = True


def on_key_up(key):
    '''Check to see if a key has been released'''
    global gameState #Make sure you make globals if necessary
    
    
    if key == keys.E:
        gameState = 'end'

    elif key == keys.C:
        clear == True

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
        screen.draw.filled_rect(button1Rect, button1Color)

    
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
        screen.draw.filled_rect(button2Rect, button2Color)
                
    elif gameState == "end":
        screen.clear()
        screen.fill((255, 182, 193))
        screen.draw.text("Thanks For Plyaing", (300, 300), color="cyan")
        
        gameState == "paint"
    else:
        screen.clear()
        screen.fill((255, 255, 255))
        screen.draw.text("Error, no game state loaded", (25, 30), color="orange")


startUp()