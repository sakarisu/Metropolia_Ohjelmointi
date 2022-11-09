tuuma = int(input('Anna tuuma: '))
sentti = float(tuuma * 2.54)
while tuuma>=0:
    print(f"{tuuma:d} tuuma(a) on {sentti:.2f} senttiä.")
    tuuma = int(input('Anna tuuma: '))
    if tuuma<=0:
        break
