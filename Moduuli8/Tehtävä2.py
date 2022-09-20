import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentopeli',
         user='root',
         password='0532189764',
         autocommit=True
         )

def getAirportTypeCount(y, iso, type):
    kursori = y.cursor()
    kursori.execute(f"SELECT COUNT(*) FROM airport WHERE iso_country='{iso}' AND type='{type}';")
    return kursori.fetchone()[0]
def getAirportTypes(y):
    kursori=y.cursor()
    kursori.execute(f"SELECT DISTINCT type FROM airport")
    return kursori.fetchall()
iso=input('Anna maatunniste: ')
if getAirportTypeCount(yhteys, iso, 'small_airport')==0: print('Virheellinen maakoodi')
print(f'Koodilla "{iso}" löytyi: ')
aTypes=getAirportTypes(yhteys)
for i in aTypes:
    print(f'{i[0].replace("_", " ")}: {getAirportTypeCount(yhteys, iso, i[0])}')