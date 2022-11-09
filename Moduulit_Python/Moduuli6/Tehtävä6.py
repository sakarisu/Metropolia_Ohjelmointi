import math
def arvo(halkaisija, hinta):
    return math.pi/4*(halkaisija/100)**2/hinta
pizhal1 = int(input('Anna ensimmäisen pizzan halkaisija sentteinä: '))
pizhin1 = int(input('Ja hinta: '))
pizhal2 = int(input('Anna toisen pizzan halkaisija sentteinä: '))
pizhin2 = int(input('Ja hinta: '))
if arvo(pizhal1, pizhin1) >= arvo(pizhal2, pizhin2):
    print('Ensimmäinen pizza on halvempi.')
elif arvo(pizhal1, pizhin1) <= arvo(pizhal2, pizhin2):
    print('Toinen pizza on halvempi.')
