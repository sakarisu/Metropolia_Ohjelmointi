import random
def par(n):
    parilliset = []
    for x in n:
        if x%2==0: parilliset.append(x)
    return parilliset
luvut = []
for i in range(10):
    l = random.randint(1, 10)
    luvut.append(l)
print('Listan luvut ovat ' + str(luvut))
print('Listalta löytyvät parilliset luvut ovat: ' + str(par(luvut)))
