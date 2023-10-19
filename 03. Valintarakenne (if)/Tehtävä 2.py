userInput = input("Anna laivan hyttiluokka (LUX, A, B, C): ")

if userInput == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif userInput == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif userInput == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif userInput == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")

