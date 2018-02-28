from __future__ import print_function # use Python 3.0 printing 
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
        print("A grade of",percent,' does not indicate mastery.\n Seek extra practice or help.')

    else:
        print("A grade of",percent,' indicates mastery.\nKeep up the good work!')
        
        
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


    
def  hint(color, secret):
    if color in secret:
        print( 'The color',color,'IS in the secret sequence of colors')

    else:
        print( 'The color',color,'IS NOT in the secret sequence of colors')

