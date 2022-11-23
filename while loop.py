# 01 > create a program count 10 to 100 sum of 10:
sum10 = 10
while sum10 <= 100:
    print(sum10)
    sum10 += 10

# 02 >
'''
The current population town is 10000. The population of the town is 
increasing at the rate if 10% per year. Ypu have to write a program to find out the 
population at the end of each of the last 10 year.
'''
now_days = 10000
for i in range(10,0,-1):
    print(round(now_days),0)
    now_days = now_days - 0.1*now_days


current_pop = 10000
for i in range(0,11):
    current_pop=current_pop+0.1*current_pop
    print(round(current_pop),0)

