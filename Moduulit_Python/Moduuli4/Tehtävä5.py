toistot = 0
while toistot<5 and (input('Kirjoita käyttäjätunnuksesi: ')!='python' or input('Kirjoita salasanasi: ')!='rules'):
    toistot+=1
if toistot<5:
    print('Tervetuloa.')
else:
    print('Pääsy evätty.')
