luku = int(input('Anna luku: '))
if luku > 1:
    for i in range(2, luku):
        if (luku % i) == 0:
            print(luku, ' ei ole alkuluku.')
            break
    else:
        print(luku, ' on alkuluku.')
else:
    print(luku, 'ei ole alkuluku.')
