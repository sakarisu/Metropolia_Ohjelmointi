kanta_str = input('Anna suorakulmion kanta: ')
kanta = float(kanta_str)
korkeus_str = input('Anna suorakulmion korkeus: ')
korkeus = float(korkeus_str)
pintaala = kanta * korkeus
piiri = kanta + korkeus + kanta + korkeus
print('Suorakulmion pinta-ala on ' + str(pintaala))
print('Suorakulmion piiri on ' + str(piiri))