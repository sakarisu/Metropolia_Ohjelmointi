suuri = pieni = luku = input('Anna luku: ')
while ((luku.strip('-')).replace('.', '')).isnumeric():
    if float(luku)<float(pieni):
        pieni=float(luku)
    elif float(luku)>float(suuri):
        suuri=float(luku)
    luku=input('Anna luku: ')
print('Suurin luku on ' + str(suuri) + ' ja pienin luku on ' + str(pieni))
