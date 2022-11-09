ekaluku_str = input('Anna ensimmäinen luku: ')
ekaluku = float(ekaluku_str)
tokaluku_str = input('Anna toinen luku: ')
tokaluku = float(tokaluku_str)
kolmasluku_str = input('Anna kolmas luku: ')
kolmasluku = float(kolmasluku_str)
summa = ekaluku + tokaluku + kolmasluku
tulo = ekaluku * tokaluku * kolmasluku
keskiarvo = ekaluku * tokaluku * kolmasluku / 3
print('Lukujen summa on ' + str(summa))
print('Lukujen tulo on ' + str(tulo))
print('Lukujen keskiarvo on ' + str(keskiarvo))