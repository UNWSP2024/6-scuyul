import random
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.

def randDice():
    randNum1 = random.randint(1,6)
    randNum2 =  random.randint(1,6)
    return randNum1 + randNum2
#########
total = 0

for i in range(100):
    total = total + randDice()
average = total/100
round(average,2)
print(average)