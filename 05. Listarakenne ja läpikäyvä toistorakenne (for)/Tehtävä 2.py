numbersList = []

while True:
    userInput = input("Anna luku: ")

    if userInput == "":
        break
    numbersList.append(userInput)

numbersList.sort(reverse=True)

if len(numbersList) >= 5:
        for i in range(0, 5):
            print(numbersList[i])
else:
    for i in range(0, len(numbersList)):
        print(numbersList[i])
