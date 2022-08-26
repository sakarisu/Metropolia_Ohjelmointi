LUOTI = 13.3
NAULA = 32 * LUOTI
LEIVISKA = 20 * NAULA

leiviskat_str = input('Anna leiviskät: ')
leiviskat = float(leiviskat_str)
luodit_str = input('Anna luodit: ')
luodit = float(luodit_str)
naulat_str = input('Anna naulat: ')
naulat = float(naulat_str)

leiviskatgrammoina = leiviskat * LEIVISKA
naulatgrammoina = naulat * NAULA
luoditgrammoina = luodit * LUOTI
gramma = leiviskatgrammoina + naulatgrammoina + luoditgrammoina
kilo = int(gramma/1000)

print('Massojen yhteissumma on:\n' + str(kilo) + ' kiloa ja ' + str(round(gramma%1000, 2)) + ' grammaa.'  )