gender = input("Anna sinun biologinen sukupolvi: ")
hemoglobiini = int(input("Anna hemoglobiiniarvosi g/l: "))

if gender == "Mies":
    if hemoglobiini >= 134 and hemoglobiini <= 195:
        print("Hemoglobiini on normaali!")
    elif hemoglobiini < 134:
        print("Hemoglobiini on alhainen!")
    elif hemoglobiini > 195:
        print("Hemoglobiini on korkea!")
elif gender == "Nainen":
    if hemoglobiini >= 117 and hemoglobiini <= 175:
        print("Hemoglobiini ok!")
    elif hemoglobiini < 117:
        print("Hemoglobiini on alhainen!")
    elif hemoglobiini > 175:
        print("Hemoglobiini on korkea!")

