import random

randomNumber = random.randint(1, 10)
print(randomNumber)

userInput = int(input("Anna luku: "))

while userInput != randomNumber:
    if userInput < randomNumber:
        print("Liian pieni arvaus!")
    elif userInput > randomNumber:
        print("Liian suuri arvaus!")

    userInput = int(input("Anna luku: "))

print("Oikein!")