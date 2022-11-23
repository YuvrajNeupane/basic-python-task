# Create a gussing a game!
# step 1.

import random
jackpot = random.randint(1,5)
# Taking input from user and create a variable. 
guess = int(input('Enter a number: '))
counter = 1
# using while loop
while guess != jackpot:
    if guess < jackpot:
        print('Enter a higher: ')
    else:
        print('guess lower value: ')
    counter += 1
    guess = int(input('Enter a number: '))
    
else:
    print('Correct.')
    print(counter,'atempt.')
