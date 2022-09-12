def muuntaja(gallona):
    neste = gallona*3.785411784
    return neste
gallona = int(input('Anna bensan määrä gallonissa: '))
while gallona >= 0:
    print(str(gallona) + ' gallon(a)a bensaa on litroina ' + str(muuntaja(gallona)) + '.')
    gallona = int(input('Anna bensan määrä gallonissa: '))