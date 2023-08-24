import calendar

userInput = int(input("Anna vuosi: "))

if calendar.isleap(userInput):
    print("Vuosi on karkavuosi.")
else:
    print("Vuosi ei ole karkavuosi.")

