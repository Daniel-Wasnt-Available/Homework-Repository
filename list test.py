spam = ['apples', 'bananas', 'tofu', 'cats']

def listPop(pop):
    for i in range(0,(len(pop))-2,1):
        print(pop[i]+', ',end='')
        
    print(pop[i+1], end='')
    print(' and', pop[i+2])
listPop(spam)