nimet = set()
uusinimi = input('Anna nimi: ')
while uusinimi != '':
   if uusinimi in nimet:
       print('Aiemmin syötetty nimi.')
   else:
       nimet.add(uusinimi)
   uusinimi = input('Anna nimi: ')
print(nimet)