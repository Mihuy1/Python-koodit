vuodenajat = {1: "talvi", 2: "talvi", 3: "talvi", 4: "kevät", 5: "kevät", 6: "kevät", 7: "kesä",
              8: "kesä", 9: "kesä", 10: "syksy", 11: "syksy", 12: "talvi"}


kuukausiNumero = int(input("Anna kuukauden numero: "))

if kuukausiNumero in vuodenajat:
    vuodenaika = vuodenajat[kuukausiNumero]
    print(f"{kuukausiNumero}. kuukausi on {vuodenaika}")




