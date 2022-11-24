# 01 > create a program count 10 to 100 sum of 10:
'''sum10 = 10
while sum10 <= 100:
    print(sum10)
    sum10 += 10
'''
# 02 >
'''
The current population town is 10000. The population of the town is 
increasing at the rate if 10% per year. Ypu have to write a program to find out the 
population at the end of each of the last 10 year.
'''
'''current_pop = 10000
for i in range(10,0,-1):
    print(round(current_pop),0)
    current_pop = current_pop - 0.1*current_pop'''

'''for i in range(0,11):
    current_pop=current_pop+0.1*current_pop
    print(round(current_pop),0)'''

'''current_pop = 1000
for i in range(10,0,-1):
    print(i,round(current_pop),0)
    current_pop = current_pop/1.1'''

# 03 > sum of Nth values. (1-1!+ 2/2!+ 3/3!.....)

#Guessing game
# stap 01 import library 
import random
#create a jackpot variable
jackpot = random.randint(1,100)
# taking input from user
guess = int(input('Enter a correct number. '))
attemp = 1
#use while loop
while guess != jackpot:
    if guess<jackpot:
        print('Try again with higher number! ')
    else:
        print('Try againg lower number! ')
    guess = int(input('Enter a correct number. '))
    attemp +=1
else:
    print(jackpot,'Correct!')
    print(attemp, 'attempt.')