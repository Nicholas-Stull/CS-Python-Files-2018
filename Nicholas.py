
from __future__ import print_function
import random

def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale','Nicholas',)):
    '''Summarize the function in this docstring.when you CALL it asks you to guess 
    a random winner. when you guess it then spits out Guess again! or You guessed
    in', guesses, 'guesses!The people's names are a list of  strings.
    
    Provide descriptions for the arguments and say what type each one is.
    Describe the type and meaning of the value returned.
    '''
    winner = random.choice(players) 

    ####
    # it is printing out what to do. it is printing out Guess which
    #of these people won the lottery
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # Gets it ready to print 
        print(p+', ', end='')
    print(players[len(players)-1]) # prints the names of the people here 

    ####
    # if you guess correct it says you gussed in blank amount, if your wrong it says Guess again
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    

def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')

def quiz_decimal(low, high):
    print('Type a number between' , low , 'and', high ,':',sep=' ')
    guess=float(input())
    if guess < low:
        print('No ',guess,'is less than',low )
    elif guess > high:
        print('No ',guess,'is greater than',high)
    else:
        print('Good! ',low,'<',guess,'<',high)
      
def guess_once():
    secret = random.randint(1, 20)
    print('I have a number between 1 and 20.')
    guess = int(input('Guess: '))
    if guess < secret:
        print('Too low - my number was ', secret, '.', sep='')
    elif guess >secret:
        print('Too high, my number was ', secret, '.', sep='')
    else:
        print('Right, my number is', guess, end='!\n')
        
def goguessbig():
    Low = 1
    High = 6000
    print('I Have a number between ', Low,' and ',High, ' inclusive.', sep='')
   
    Answer = random.randint(Low,High)
    Guess=-1
    Guesses = 0
    
    while(Guess != Answer):
        Guess=int(raw_input('Guess: '))
        Guesses += 1
        if Guess < Answer:
            print(Guess,'Too low - Keep Trying',sep='')
        if Guess > Answer:
            print( Guess ,'Too high - Keep Trying', sep='')
    print('Right!, my number is', Answer,'! You guessed in ',Guesses,'!', sep='')
        
def goguesssmall():
    Low = 1
    High = 20
    print('I Have a number between ', Low,' and ',High, ' inclusive.', sep='')
   
    Answer = random.randint(Low,High)
    Guess=-1
    Guesses = 0
    
    while(Guess != Answer):
        Guess=int(raw_input('Guess: '))
        Guesses += 1
        if Guess < Answer:
            print(Guess,'Too low - Keep Trying',sep='')
        if Guess > Answer:
            print( Guess ,'Too high - Keep Trying', sep='')
    print('Right!, my number is', Answer,'! You guessed in ',Guesses,'!', sep='')
        
