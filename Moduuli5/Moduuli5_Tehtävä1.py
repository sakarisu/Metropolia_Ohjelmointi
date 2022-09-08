import random
arvat = int(input('Kuinka monta arpakuutiota heitetään? '))
for i in range(arvat):
    arpa = random.randint(1, 6)
summa = (arpa*arvat)
print('Heittämiesi arpojen silmälukujen summa on ' + str(summa))