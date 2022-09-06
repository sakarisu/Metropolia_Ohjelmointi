import random
luku = random.randint(1, 10)
arvaus = int(input('Arvaa luku: '))
while luku != arvaus:
    if luku < arvaus:
        print('Liian suuri luku.')
    elif luku > arvaus:
        print('Liian pieni luku.')
    arvaus = int(input('Arvaa luku: '))
print('Oikein.')