import random
def sum(n):
    summa = 0
    for x in n:
        summa += x
    return summa
luvut = []
for i in range(10):
    l = random.randint(1, 10)
    luvut.append(l)
print('Listan luvut ovat ' + str(luvut))
print('Lukujen summa on ' + str(sum(luvut)))