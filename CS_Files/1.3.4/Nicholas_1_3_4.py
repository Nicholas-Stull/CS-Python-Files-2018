from __future__ import print_function # must be first in file 
def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
            
            
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not    
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False


def f(x):
    if int(x)==x:
        if x%2==0:
            if x%3==0:
                print ('x is multipule of 6')
            else:
                print('x is even')
        else:
            print('x is odd')
    else:
        print('x is not an integer')                  
           

import random

def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(input('Guess: '))
    if guess < secret:
        print('Too low - my number was ', secret, '.', sep='')
    elif guess >secret:
        print('Too high, my number was ', secret, '.', sep='')
    else:
        print('Right, my number is', guess, end='!\n')
      
def quiz_decimal(low, high):
    print('Type a number between' , low , 'and', high ,':',sep=' ')
    guess=float(input())
    if guess < low:
        print('No ',guess,'is less than',low )
    elif guess > high:
        print('No ',guess,'is greater than',high)
    else:
        print('Good! ',low,'<',guess,'<',high)
      

