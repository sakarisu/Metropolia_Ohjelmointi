import random
def heitto(lkm):
    return random.randint(1, lkm)
lkm=int(input('Anna tahkojen lukumäärä: '))
noppa = 0
while noppa != lkm:
   noppa = heitto(lkm)
   print(noppa)
