minSize = 37

userInput = int(input("Anna kuhan pituus: "))

if userInput < 37:
    print("Laske kuha takaisin järveen!")
    print(f"Kuha on {minSize - userInput} senttiä pienempi kuin minimi koko")
