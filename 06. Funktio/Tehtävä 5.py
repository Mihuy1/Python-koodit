

def PoistaParittomat(lista: list):

    muunnettuLista = []

    for numero in lista:
        if numero % 2 == 0:
            muunnettuLista.append(numero)
    return muunnettuLista


testiLista = [2, 4, 6, 7, 8, 10, 11, 13]
print(PoistaParittomat(testiLista))
print(testiLista)

