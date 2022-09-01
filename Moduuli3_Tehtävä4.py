vuosi=int(input('Anna vuosiluku:'))
div=int(4 or 400)
if vuosi&div==0:print('Tämä vuosi on karkausvuosi.')
else:
    print('Tämä vuosi ei ole karkausvuosi.')