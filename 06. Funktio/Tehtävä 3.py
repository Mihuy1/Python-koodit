

# Yksi gallona on 3,785 litraa

gallon = 3.785

def Bensiini(gallonia):
    litra :float = gallonia * gallon

    return litra

userInput = float(input("Anna gallonamäärän: "))

while userInput > 0:
    print(Bensiini(userInput))

    userInput = float(input("Anna gallonan määrä: "))


