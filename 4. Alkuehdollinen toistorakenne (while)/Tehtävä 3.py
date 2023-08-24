numerot = []

while True:
    userInput = input("Anna luku: ")

    if userInput == "":
        break

    numerot.append(int(userInput))
print(f"Suurin luku: {max(numerot)}")
print(f"Pienin luku: {min(numerot)}")