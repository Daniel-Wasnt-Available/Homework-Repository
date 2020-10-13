#-----------------------------------------------------------------------------
# Name:        actors with images example
# Purpose:     And Example file demoing actors
#
# Author:      Mr. Brooks
# Created:     01-Oct-2020
# Updated:     01-Oct-2020
#-----------------------------------------------------------------------------
''' This code was copy and pasted from github. the error I get is:
Hello from the pygame community. https://www.pygame.org/contribute.html
Traceback (most recent call last):
  File "/Users/danielw/Documents/GitHub/homework-repository-Daniel-Wasnt-Available/pgZero intro/re-testing knight actor code.py", line 15, in <module>
    knight = Actor('knight_m_run_anim_f0')
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
WIDTH = 200
HEIGHT = 200

gameState = ''

#Create the actor object
knight = Actor('knight_m_run_anim_f0')
#Give the actor a place on the screen to be
knight.pos = (100, 100)
#Set the starting image number
knight.frame = 0

def updateKnight():
    global knight
    knight.frame = knight.frame + 1
    
    #What do these lines fix?
    if knight.frame > 3:
        knight.frame = 0
        
    #Assign a new image name based on the updated frame number
    knight.image = 'knight_m_run_anim_f' + str(knight.frame)
    

def on_key_up(key):
    '''Check to see if a key has been released'''
    global gameState #Make sure you make globals if necessary
    global knight
    
    if key == keys.A:
        #Call the animation function
        updateKnight()
        

def draw():
    '''Draw loop for all the graphical elements to display'''
    #Empty the screen for each animation frame
    screen.fill((255, 255, 255))
    #Draw the knight
    knight.draw()