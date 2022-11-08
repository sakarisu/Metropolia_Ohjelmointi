import requests
paikkakunta = input('Minkä paikkakunnan sääilmoituksen haluat? ')
parametrit = {
    'q' :paikkakunta,
    'appid' :'469d78a39ed8448ec2da938882a7d6a7'
}
sijainti = requests.get('http://api.openweathermap.org/geo/1.0/direct', parametrit)
tulos = sijainti.json()
pituus = tulos[0]['lon']
leveys = tulos[0]['lat']
parametrit = {
    'lon' :pituus,
    'lat' :leveys,
    'appid' :'469d78a39ed8448ec2da938882a7d6a7',
    'lang' : 'FI'
}
sää = requests.get('https://api.openweathermap.org/data/2.5/weather', parametrit)
tulos = sää.json()
keli = tulos['weather'][0]['description']
lämpö = tulos['main']['temp']
print(f'Paikkakunnalla {paikkakunta} lämpötila on {round(lämpö - 273.15, 1)}°C \n Keli: {keli}')
