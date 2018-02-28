import random
def roll_two_dice():
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6) 
    total = die_1 + die_2
    return total
   
def guess_letter():
    letters=('q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m')
    for x in range(10):
        print (random.choice(letters))
           