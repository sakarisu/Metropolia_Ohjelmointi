luvut = []
luku = input('Anna luku tai paina Enter: ')
while luku != '':
    luvut.append(luku)
    luku = input('Anna seuraava luku tai paina Enter: ')
else:
    jono = sorted(luvut)
    print('Antamasi luvut suuruusjärjestyksessä: ' + str(jono))
