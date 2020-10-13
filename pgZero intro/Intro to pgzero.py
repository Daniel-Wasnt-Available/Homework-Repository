#-----------------------------------------------------------------------------
# Name:        Hurt alien.py
# Purpose:     trying pygame zero features
#
# Author:      Daniel
# Created:     2-oct-2020
# Updated:     2-oct-2020
#-----------------------------------------------------------------------------
''' This is what my error says for this code
Hello from the pygame community. https://www.pygame.org/contribute.html
Traceback (most recent call last):
  File "/Users/danielw/Documents/GitHub/homework-repository-Daniel-Wasnt-Available/pgZero intro/Intro to pgzero.py", line 9, in <module>
    alien = Actor('alien')
  File "/Users/danielw/Library/Python/3.7/lib/python/site-packages/pgzero/actor.py", line 88, in __init__
    self.image = image
  File "/Users/danielw/Library/Python/3.7/lib/python/site-packages/pgzero/actor.py", line 103, in __setattr__
    return object.__setattr__(self, attr, value)
  File "/Users/danielw/Library/Python/3.7/lib/python/site-packages/pgzero/actor.py", line 218, in image
    self._orig_surf = self._surf = loaders.images.load(image)
  File "/Users/danielw/Library/Python/3.7/lib/python/site-packages/pgzero/loaders.py", line 115, in load
    key = self.cache_key(self, name, args, kwargs)
TypeError: cache_key() takes 3 positional arguments but 5 were given
'''
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
    
