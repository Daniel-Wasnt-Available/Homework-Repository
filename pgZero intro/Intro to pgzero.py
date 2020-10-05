#-----------------------------------------------------------------------------
# Name:        Hurt alien.py
# Purpose:     trying pygame zero features
#
# Author:      Daniel
# Created:     2-oct-2020
# Updated:     2-oct-2020
#-----------------------------------------------------------------------------
alien = Actor('alien')
alien.topright = 0, 10

WIDTH = 500
HEIGHT = alien.height + 400

def draw():
    screen.clear()
    alien.draw()
def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        sounds.eep.play()
        alien.image = 'alien_hurt'
    if alien.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")

def set_alien_normal():
    alien.image = 'alien'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)
    
