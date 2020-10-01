def whatDayIsIt(dayNumberIn):
    '''Return the text for the day given it's numeric value '''

    if dayNumber == 0:
        return("Sunday");
    elif dayNumber == 1:
        return("Monday")
    elif dayNumber == 2:
        return("Tuesday")
    elif dayNumber == 3:
        return("Wednesday")
    elif dayNumber == 4:
        return("Thursday")
    elif dayNumber == 5:
        return("Friday")
    elif dayNumber == 6:
        return("Saturday")
    else: #This part is not required, but it shows simple error checking
        return("Error")


def countUp():
    '''Count from 0 to 10'''

    count = 1;
    while count <= 10:
        print (count)
        count = count +1;


def displayMenu():
    '''Display a menu and ask the user what they want to do'''
    print('Program Menu')
    print()
    print('1. Count up!')
    print('2. Day of the Week Selector')
    print('3. Exit')
    print()
    answer = input('Which program would you like to choose?')
    return answer



answer = "" #Why does this need to be here?
while answer != '3':
    answer = displayMenu()

    if answer == '1':
        countUp()

    elif answer == '2':
        #Get user input
        dayNumber = int(input("Please enter the number of the day: "))

        #Call the function AND print results at the same time
        print("The day of the week is " + whatDayIsIt(dayNumber))
        print()

    elif answer == '3':
        print('Goodbye!')

    else:
        print ('\r\nSorry, that is not a valid responce.')
        print ('Please try again \r\n')