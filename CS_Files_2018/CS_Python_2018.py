# 1.3.2
# @Author: Nicholas Stull
# @Date:   2018, Wed, 17 Jan 
from __future__ import print_function # use Python 3.0 printing
from __future__ import print_function # must be first in file
import random
def add_tip(total, tip_percent): 
    ''' Return the total amount including tip'''
    tip = tip_percent*total
    return total + tip

def mean(a,b,c):
    '''returnes the total of three numbers'''
    numsum=a+b+c
    total=numsum/3.0
    return total
    
def perimeter(base, height):
    '''returnes the perimiter of rectangle'''
    p=(base+height)*2
    return p 
    
def hyp(leg1, leg2):
    '''returnes Hypotenuse of right triangle'''
    leg1=leg1**2
    leg2=leg2**2
    leg3=(leg1+leg2)**0.5
    return leg3
    

# 1.3.3
# @Author: Nicholas Stull


def age_limit_output(age):
    '''Step 6a if-else example'''
    AGE_LIMIT = 18  # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT)


def report_grade(percent):
    '''Step 6b if-else'''
    Passing_grade = 80  # convention: use CAPS for constants
    if percent < Passing_grade:
        print("A grade of", percent,
              ' does not indicate mastery.\n Seek extra practice or help.')

    else:
        print("A grade of", percent, ' indicates mastery.\nKeep up the good work!')


def vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False
# should check len(letter)==1letter_in_word('t', 'secret hangman phrase')


def letter_in_word(guess, word):
    if guess in word:
        return True
    else:
        return False
# should check len(letter)==1letter_in_word('t', 'secret hangman phrase')


def hint(color, secret):
    if color in secret:
        print('The color', color, 'IS in the secret sequence of colors')

    else:
        print('The color', color, 'IS NOT in the secret sequence of colors')


# 1.3.4


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
    if int(x) == x:
        if x % 2 == 0:
            if x % 3 == 0:
                print('x is multipule of 6')
            else:
                print('x is even')
        else:
            print('x is odd')
    else:
        print('x is not an integer')


def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(input('Guess: '))
    if guess < secret:
        print('Too low - my number was ', secret, '.', sep='')
    elif guess > secret:
        print('Too high, my number was ', secret, '.', sep='')
    else:
        print('Right, my number is', guess, end='!\n')


def quiz_decimal(low, high):
    print('Type a number between', low, 'and', high, ':', sep=' ')
    guess = float(input())
    if guess < low:
        print('No ', guess, 'is less than', low)
    elif guess > high:
        print('No ', guess, 'is greater than', high)
    else:
        print('Good! ', low, '<', guess, '<', high)


# 1.3.5
# if input('One character: ') == '!':
   # print('Wow', end='!')


def how_eligible(essay):
    score = 0
    if '?' in essay:
        score += 1
        if ',' in essay:
            score += 1
            if '"' in essay:
                score += 1
                if '!' in essay:
                    score += 1
    return score

    
    
