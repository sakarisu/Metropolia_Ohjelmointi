lento = {}
alku = input('Anna "S" syöttääksesi uuden lentokentän, "H" hakeaksi lentokenttää tai "L" jos haluat lopettaa: ')
while alku != 'L':
    if alku == 'S':
        lento[input('Anna lentokentän ICAO-koodi: ')] = input('Anna lentokentän nimi:')
        print('Lentokenttä on lisätty tietokantaan.')
        alku = input('Anna "S" syöttääksesi uuden lentokentän, "H" hakeaksi lentokenttää tai "L" jos haluat lopettaa: ')
    elif alku == 'H':
       koodi = input('Anna lentokentän ICAO-koodi: ')
       if koodi in lento: print(lento[koodi])
       else: print('Lentokenttää ei ole vielä lisätty tietokantaan.')
       alku = input('Anna "S" syöttääksesi uuden lentokentän, "H" hakeaksi lentokenttää tai "L" jos haluat lopettaa: ')
