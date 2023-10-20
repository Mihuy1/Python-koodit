def alkuluku(luku):
    luku = int(luku)

    flag = True

    if luku < 2:
        flag = False
    else:
        for i in range(2, luku):
            if luku % i == 0:
                flag = False
                break

    vastaus = {
        "Number": luku,
        "isPrime": flag
    }

    return vastaus
