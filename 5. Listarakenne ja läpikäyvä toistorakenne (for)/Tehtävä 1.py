import random as r

userInput = int(input("arpakuutioiden lukumäärä: "))

numbers = []

for i in range(0, userInput):
    randomNumber = r.randint(1, 6)
    numbers.append(randomNumber)
    print(f"Nopan arvo: {randomNumber}")


print(f"Summa: {sum(numbers)}")



