leiviskat_input = float(input("Anna leiviskät: "))
naulat_input = float(input("Anna naulat: "))
luodit_input = float(input("Anna luodit: "))

#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.

naulat = leiviskat_input * 20
naulat += naulat_input

luodit = naulat * 32
luodit += luodit_input

grammat = luodit * 13.3
jaannos = grammat % 1000
kilogrammat = grammat // 1000

print("Massa nykymittojen mukaan:")
print(f"{int(kilogrammat)} kilogrammaa ja {round(jaannos, 2)} grammaa.")
