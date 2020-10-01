lives = 3
def storyLine():
    import time
    print("     =========================Story Line=========================")
    print("Date: September 20, 2019")
    time.sleep(2)
    print("You and a friend are headed to Neveda for the Area 51 Raid")
    time.sleep(3)
    print("Being the genius that you are, you forgot to fuel the car all the way when you left")
    time.sleep(3)
    print("Half way into the Neveda Desert you run out of gas...")
    time.sleep(3)
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

def loadingScreen(): #Yes...another student who has also added in a loading screen. But just one time for the start o.O
    import random
    import time

    loading = 0

    while loading <= 100:
        print (str(loading)+'% loaded')
        loading += random.randint (4,11)
        time.sleep(0.2)
    print ('Game Loaded')
    return

    
def welcomeScreen():
    import time
    if lives == 3:
        time.sleep(6)
        print("*static * white noise. something is interupting our radio sign- *buzz, hello? *bzzzz")
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
    print("Here is your second riddle, you got this!")
    print('''
Can you name three consecutive days without using the words Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?
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
    storyLine()
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
        print("You still have 3 left")
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
        print("You are on a roll! Keep going!")
    