def alkuluku_tarkistus(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

userInput = int(input("Anna luku: "))

if alkuluku_tarkistus(userInput):
    print(f"{userInput} on alkuluku!")
else:
    print(f"{userInput} ei ole alkuluku!")
