import random

diceNumber = 0


def RandomDice():
    number = random.randint(1,6)
    return number

while diceNumber != 6:

    diceNumber = RandomDice()

    print(f"Nopan arvo: {diceNumber}")


