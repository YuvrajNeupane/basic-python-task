# Create a gussing game using while loop

# Impoer random number generator 
import random

generator = random.randint(1,10)

guess = int(input('Guess a right number: '))
attemp = 1

while guess != generator:
    if guess < generator:
        print('Try higher number again!')
    else:
        print('Try Lower value! ')
    guess = int(input('Guess a right number: '))
    attemp += 1

else:
    print('Correct.')
    print('attemp:', attemp)

print('jackpot: ',generator)