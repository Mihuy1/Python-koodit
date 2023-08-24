i = 1

correctUser = "python"
correctPassword = "rules"

while i <= 5:
    userName = input("käyttäjätunnus: ")
    userPassword = input("salasana: ")

    if userName == correctUser and userPassword == correctPassword:
        print("Oikein!")
        break
    elif userName != correctUser or userPassword != correctPassword:
        print("Kokeile uudestaan!")
        i += 1
        continue

if i >= 5:
    print("Pääsy evätty.")