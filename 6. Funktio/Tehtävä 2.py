import random

diceNumber = 0
maxSize = 0

def DiceSetup(diceSize):
    return diceSize

def RollDice():
    number = random.randint(1, maxSize)
    return number

maxSize = DiceSetup(11)

while diceNumber != maxSize:

    diceNumber = RollDice()

    print(f"Nopan arvo: {diceNumber}")
