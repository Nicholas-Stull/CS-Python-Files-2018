# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt # standard short name
import random

plt.ion() # sets “interactive on”: figures redrawn when updated

def picks():
    a = [] # make an empty list

    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list      ]
    #    random.choice(   [brackets here to choose from a list] )
    a += [random.choice([1, 3, 10])]

    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.show()
    
def roll_hundred_pair():
    a = []
    die1 = 0
    die2 = 0
    
    for i in range
    

           

