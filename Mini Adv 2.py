#-----------------------------------------------------------------------------
# Name:        Cosmic Getaway.py
# Purpose:     Mini Adventure Game
#
# Author:      Daniel W
# Created:     23-Sept-2020
# Updated:     25-Sept-2020
#-----------------------------------------------------------------------------
#I think this project deserves a 4+ because ...
#
#Features Added:
#  Firstly the game came out 4 times better than I thought I was capable of making
#  Did some research on how to add a typing affect (I only added this for the story line section because it took a lot more code)
#  A really long time editing ascii art, I removed symbols that broke the code, like x's
#  I also had some wierd problems with printing ascii, some lines didn't match, if you look are some of the ascii in my code
#  they will look strange and out of place but I had to do it so in the shell it prints normally.
#  I spent a lot of time after class to work on this (Not like homework tho because I really enjoyed it)
#  Tried adding something unique, in this game at the start one of the rules was, if you get abducted, you dont know anything.
#  So I added some code that if the player lost all their lives and get abducted they have a chance to get back in the game
#  by telling the aliens, they don't know anything.
#  When the characters chat in ascii they will recall what the player enterd as their name.
#  for example in the first alien encounter the player name is known as a rare species, also your friend will blame you for forgetting gas...
#  Depending on wheater you get the answer right or not the output/reaction of the aliens and stuff will change
#  Incorporated a no so helpful 911 operator who is on the phone with you to add some humour and make things intresting.
#-----------------------------------------------------------------------------
lives = 3


def loadingScreen(): #Yes...another student who has also added in a loading screen. But just one time for the start o.O
    import random
    import time

    loading = 0

    while loading <= 100:
        print (str(loading)+'% loaded')
        loading += random.randint (4,11)
        time.sleep(0.2)
    print ('Game Loaded...')
    time.sleep(5)
    print("Just kidding, you need 1% more... ")
    time.sleep(3)
    print("100%...")
    time.sleep(3)
    print("======================101%======================")
    time.sleep(3)
    print("There we go")
    return

    
def welcomeScreen():
    import time
    if lives == 3:
        time.sleep(6)
        print("so now you decide to call 911, but...")
        time.sleep(3)
        print("*static * white noise 'something is interupting our radio sign'- *buzz, 'hello?' *bzzzz")
        time.sleep(4)
        name = input("Hello Earthling, What's your name? -->")
    print("\r\n")
    print (" Hey Look! There are           That looks like a "+name+" ")
    print ('''  some nice specimens         I've heard they are very rare!
    down there! Commander     We will surly be promoted
    Ekteils will be proud!     if we can catch this one!
                     \  _.-'~~~~'-._   /
                .      .-~ \__/  \__/ ~-.         .
                   .-~   (oo)  (oo)    ~-.
                   (_____//~~\\//~~\\______)
             _.-~`                         `~-._
            /O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O\     *
            \___________________________________/
                       \-------------/
               .  *     \___________/
    ''')


def firstRiddle():
    print("Here is your first riddle")
    print('''
George Smith was murdered on Sunday evening. There were 5 other people in his house: Mr. Smith's wife, his personal cook, a butler, a housemaid, and a gardener. They all told Detective Stevens what they were doing that evening:

Mrs. Smith was reading a book near a fireplace.
The cook was making breakfast.
The butler was giving instructions to workers in the living room.
The housemaid was washing the dishes.
The gardener was watering plants in the greenhouse.
Right after all the conversations, the detective arrested the murderer. Who was the killer?

Choices: Mrs.Smith, The Cook, The Butler, The Housemaid, or The Gardener?
''')
    
def secondRiddle():
    print("\r\n")
    print("Great to hear from you!")
    print("Here is your second riddle, you got this!")
    print('''
Can you name three consecutive days without using the words Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?
''')
    
def thirdRiddle():
    print("\r\n")
    print("I see those legs are still working eh? Ok here's your next riddle:")
    time.sleep(3)
    print("What occurs once in a minute, twice in a moment, and never in one thousand years?")
    time.sleep(4)
    print("hint: look in the sentence")
    
def fourthRiddle():
    print("\r\n")
    print("WOW! how are you still going? I'm not that I don't want you to be alive but damn!")
    time.sleep(3)
    print("alright here's your last riddle I belive in you now")
    time.sleep(2)
    print("Not that I didn't bealive in you before but I honestly thought you'd be dead...")
    time.sleep(3)
    print("Okok anyways, good luck")
    time.sleep(2)
    print('''On the first day of the school year, a geography teacher was murdered.
    The police had 4 suspects: the gardener, the math teacher, the coach, and the school principal.
    They all had alibis:
    The gardener was cutting bushes.
    The math teacher was holding a mid-year test.
    The coach was playing basketball.
    The principal was in his office.
    ''')

import time

if lives == 3:
    input("Are Your Ready To Play?")
    loadingScreen()
    print ("-------------------------Welcome to Cosmic Getaway-------------------------")
    print ('''
    Goals:
    -Your goal in this game is to solve a series of riddles
    and ultimately escape from the aliens chasing you.
    -You start with 3 lives and you lose one for every wrong answer
    Rule: Don't get abducted
    p.s. if you get abducted.... you don't know anything

     -------------------------Good Luck!-------------------------
        ''')
    name = input("Looks like we have another runner. What's your name? -->")
    print("\r\n")
#This story line section use to be a function
#but I had a lot of trouble putting it in the function, like indent errors, name errors, so I just put it in the main code
import sys
from time import sleep
print("     =========================Story Line=========================")
lineone = "Date: September 20, 2019"

for char in lineone:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()
print("\r\n")

linetwo = "You and a friend are headed to Neveda for the Area 51 Raid"

for char in linetwo:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
print("\r\n")

linethree = "Being the genius that you are, you forgot to fuel the car when you left"

for char in linethree:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
print("\r\n")
    
linefour = "Half way into the Neveda Desert you run out of gas..."

for char in linefour:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
print("\r\n")
linefive = "Why did you forget to fuel the car?..."

for char in linefive:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
print("\r\n")
time.sleep(3)
input("Umm, I'm still wating for your answer... -->")
print('''
        .       .            .           .
   .       *             .         .
                 .                      .
   .       .       .'          .
                  '.              *        .
      .   '        .'     .              .
  __        .    .'          ______        __
    |          o'           |      |      |  |
    |                       |      |      |  |
    |                       |      |   ___|  |_
  __|_______________________|__..--~~~~        ~--.
  ''')
print("                                       You're a gunius "+name+"")
print ('''                     /               \  Only a total
                    /        |        \  *smartguy like YOU,
                   /                    would run out of gas in
                  /   ____   |           the MIDDLE OF NOWHERE,
                 /   /  __)         ___ at THREE IN THE MORNING!
                /    \(~oo   |     (___)  /
               /     _\_-/_       (_o o_) __
              /     /  \/  \ |    (_\O/_)(\ \ 
''')

welcomeScreen()
input("THEY ARE AFTER YOU!! NOW RUN OR RUN:")
firstRiddle()
answer = input("Who is the killer? -->")
if answer == ("The Cook") or answer == ("the cook") or answer ==("cook") or answer ==("Cook") :
    print("\r\n")
    print("AMAZING, you got the first riddle right! Keep Going!")
    print("Explination: The murder was committed in the evening. But The Cook said he was making breakfest")
    print("You still have 3 lives left")
    time.sleep(6)
    print(''' 
    Dang It! How did                 Looks like this one is smarter
    they figure that one out?!       than the rest, better rewards!
                     \  _.-'~~~~'-._   /
                .      .-~ \__/  \__/ ~-.         .
                   .-~   (oo)  (oo)    ~-.
                   (_____//~~\\//~~\\______)
             _.-~`                         `~-._
            /O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O\     *
            \___________________________________/
                       \-------------/
               .  *     \___________/
    
''')
else:
    lives = lives - 1
    print("\r\n")
    print ("Oh no, The correct answer was The Cook, you have "+str(lives)+" lives left")
    print("Explination: The murder was committed in the evening. But The Cook said he was making breakfest")
    time.sleep(6)
    print(''' 
    Ahaha, I knew that one           Maybe they aren't as smart
    would work. Everytime!           as I thought.
                     \  _.-'~~~~'-._   /
                .      .-~ \__/  \__/ ~-.         .
                   .-~   (oo)  (oo)    ~-.
                   (_____//~~\\//~~\\______)
             _.-~`                         `~-._
            /O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O\     *
            \___________________________________/
                       \-------------/
               .  *     \___________/
    
''')
    print("\r\n")
input("*radio radio, checking on your status. How are you doing?")
secondRiddle()
print ("What is your answer?(please use all lowercase, without commas, and add spaces)")
answertwo = input(" p.s. we aren't in first grade...spelling counts. -->")
if answertwo == ("yesterday today tomorrow"):
    print("\r\n")
    print("Fantastic! What's your IQ? 200?")
    print("Oh no...")
    print("behind you")
    print("LOOK BEHIND YOUR!")
    input("TELL YOUR FRIEND TO RUN!:")
    print("Nah it's too late, you should keep running tho...")
    time.sleep(3)
    print('''
          .                            *
                    _.-'~~~~'-._
      .          .-~ \__/  \__/ ~-.         .
               .-~   (oo)  (oo)    ~-.
              (_____//~~\\//~~\\______)
         _.-~`                         `~-._
        /O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O\
        
        \___________________________________/
                   \-------------/
                    \___________/
                     :|. | ' ."
                     | |. '. |:| Zzuzz!
    "Ohmygosh! Ey    | :  |:. ;|
   so umm the guy    . | : .|  :
 on the phone says   | . | : .||
 I should run..GL!   : |. | . ::  Zzuzz!
        \    ___     |.: |. :. |
            /  _)    | :|___ |:|
           |  (~o   (\.|(___)  /)
           _\/_/_     \\(_O O_)//   Zzuzz!
          /      \   .\(_\O/_)/:
         / /    \ \  :|\/\_/\/ |
         \ |    | /  | .(_ _): |
          \|____|/   .| /   \ |:
           |_  _|    | /_____\.| !!!EEEEKKKK!!!
           | |  |    : .| | | .
           | |  |    .  | | | ||
           |_|__|    | :|_|_| .:
           [__[__)   .: <_|_> .|
''')
    
else:
    print("\r\n")
    lives = lives - 1
    print("That was a hard riddle, dang it even I didn't know")
    print("Unfortunatly you now have "+str(lives)+" lives left")
    print("keep going, your next ridd-")
    print("Oh no...")
    print("behind you")
    print("LOOK BEHIND YOUR!")
    input("TELL YOUR FRIEND TO RUN!:")
    print("Nah it's too late, you should keep running tho...")
    time.sleep(3)
    print('''
          .                            *
                    _.-'~~~~'-._
      .          .-~ \__/  \__/ ~-.         .
               .-~   (oo)  (oo)    ~-.
              (_____//~~\\//~~\\______)
         _.-~`                         `~-._
        /O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O\
        
        \___________________________________/
                   \-------------/
                    \___________/
                     :|. | ' ."
                     | |. '. |:| Zzuzz!
    "Ohmygosh! Ey    | :  |:. ;|
   so umm the guy    . | : .|  :
 on the phone says   | . | : .||
 I should run..GL!   : |. | . ::  Zzuzz!
        \    ___     |.: |. :. |
            /  _)    | :|___ |:|
           |  (~o   (\.|(___)  /)
           _\/_/_     \\(_O O_)//   Zzuzz!
          /      \   .\(_\O/_)/:
         / /    \ \  :|\/\_/\/ |
         \ |    | /  | .(_ _): |
          \|____|/   .| /   \ |:
           |_  _|    | /_____\.| !!!EEEEKKKK!!!
           | |  |    : .| | | .
           | |  |    .  | | | ||
           |_|__|    | :|_|_| .:
           [__[__)   .: <_|_> .|
''')
time.sleep(5)
print("Welp...I mean you never really liked that friend anyways right?")
time.sleep(3)
print("Hey look, telling people your friend got abducted by aliens isn't a bad story eh?")
time.sleep(3)
input("Ohhh c'mon, stop standing there and KEEP RUNNING! -->")

#third riddle
thirdRiddle()
answerthree = input("Alright buddy, what's your gusse? -->")
if answerthree == ("m") or answerthree == ("M"):
    print("You are on a roll")
    print("Congrats, you still have "+str(lives)+" lives left")
    print("Hey it looks like the aliens are chasing you on foot now")
    print("oh look... one of them is waving?")
    print('''
"Hello there hooman
 we just need to borrow
 you for 'science'"
    \
  .--.   |V|
     /    \ _| /
     q .. p \ /
      \--/  //
     __||__//
    /.    _/
   // \  /
  //   ||
  \   /  \  
   )\|    |
  / || || |
  |/\| || |
     | || |
     \ || /
   __/ || \__
  \____/\____/
''')
    print("awww, I think they're nice aliens. ")
    input("want to go towards them and negotiate a deal?...for your life?")
    print('''
o
 \_/\o
( Oo)                    \|/
(_=-)  .===O-  ~~Z~A~P~~ -O-
/   \_/U'                /|\

||  |_/
\\   |
{K ||
 | PP
 | ||
 (__\\
''')
    print("Opps...his buddy has a lazer gun...")
    input("Scratch everything I said, KEEP RUNNING!-->")
    
else:
    lives = lives - 1
    if lives > 0:
        print("Good try, they aliens seem to have some tough questions up their sleeves")
        print("You currently have "+str(lives)+" remaining")
        print("Hey it looks like the aliens are chasing you on foot now")
        print("oh look... one of them is waving?")
        print('''
"Hello there hooman
 we just need to borrow
 you for 'science'"
    \
  .--.   |V|
     /    \ _| /
     q .. p \ /
      \--/  //
     __||__//
    /.    _/
   // \  /
  //   ||
  \   /  \  
   )\|    |
  / || || |
  |/\| || |
     | || |
     \ || /
   __/ || \__
  \____/\____/
''')
        print("awww, I think they're nice aliens. ")
        input("want to go towards them and negotiate a deal?...for your life?")
        print('''
o
 \_/\o
( Oo)                    \|/
(_=-)  .===O-  ~~Z~A~P~~ -O-
/   \_/U'                /|\

||  |_/
\\   |
{K ||
 | PP
 | ||
 (__\\
''')
        print("Opps...his buddy has a lazer gun...")
        input("Scratch everything I said, KEEP RUNNING!-->")
    else:
        print("OH NO! you're out of lives they're comi-")
        print("well hello there species 385, we're taking you to our planet for testing")
        extraLife = input("In the meantime we need you to tell us everything, so, what do you know about Planet 7054(Earth)-->")
        if extraLife == ("i don't know anything") or extraLife == ("i dont know anything") or extraLife == ("nothing") or extraLife == ("Nothing") or extraLife == ("I Don't Know Anything") or extraLife == ("no") or extraLife == ("No"):
            lives = lives + 1
            print("Congrats, you remembered the rule from the start, aka, the hidden riddle")
            print("You have been granted an extra life!")
            input("Ready to continue your escape? -->")
        else:
            print("Game over, you forgot the rule at the beginning")
            print("If you get abducted, you don't know anything")
            input("By answering your next riddle you escape the UFO, ready? -->")
fourthRiddle()
answerfour = input("The killer was arrested immediately, who was it? -->")
if answerfour == ("Math Teacher") or answerfour == ("math teacher"):
    print("Congrat! You beat the aliens!")
    time.sleep(3)
    print("Well...now let's find you a ride home")
    time.sleep(3)
    print("And I think I should tell you... the police were never on their way...")
    time.sleep(3)
    print("Non of them wanted to die")
    time.sleep(3)
    print("Ok yea sorry bye hope you find a ride, sorry about your find!")
    time.sleep(3)
    comment = input("Leave a comment. -->")
    print('''
        .       .    )        .           .
   .       *             .         .
                 .                      .
   .       .          o        .
                    .'            *        .
      .   '       .'      .              .
  __        .   .'           ______        __
    |           '.          |      |      |  |
    |            .'         |      |      |  |
    |                       |      |   ___|  |_
  __|_______________________|__..--~~~~        ~--.
''')
    print("        "+comment+"")
    print('''
               _ /         
              /_\    
              \_/   
             /   \    
             \|_|/     
              |||      
              |||  
             (_|_) 
''')
else:
    if lives > 0:
        print("Congrat! You beat the aliens!")
        time.sleep(3)
        print("Well...now let's find you a ride home")
        time.sleep(3)
        print("And I think I should tell you... the police were never on their way...")
        time.sleep(3)
        print("Non of them wanted to die")
        time.sleep(3)
        print("Ok yea sorry bye hope you find a ride, sorry about your friend!")
        time.sleep(3)
        comment = input("Leave a comment. -->")
        print('''
        .       .    )        .           .
   .       *             .         .
                 .                      .
   .       .          o        .
                    .'            *        .
      .   '       .'      .              .
  __        .   .'           ______        __
    |           '.          |      |      |  |
    |            .'         |      |      |  |
    |                       |      |   ___|  |_
  __|_______________________|__..--~~~~        ~--.
''')
        print("      "+comment+"")
        print('''
               _          
              /_\    
              \_/   
             /   \    
             \|_|/     
              |||      
              |||  
             (_|_) 
''')
        print("play again?")
    if lives == 0: 
        print("Yeah I'm not even gonna bother giving you your score, trust me you don't wanna see it")
        time.sleep(3)
        print("but umm")
        time.sleep(2)
        print("want to play again?")
        
        
        