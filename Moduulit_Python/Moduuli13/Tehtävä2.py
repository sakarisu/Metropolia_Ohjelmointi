import mysql.connector
from flask import Flask
import json
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentopeli',
         user='root',
         password='0532189764',
         autocommit=True
         )
app = Flask(__name__)
@app.route('/kenttä/<icao>')
def kentta(icao):
    kursori = yhteys.cursor()
                                        #Tässä kohtaa tulee ongelma: PyCharm ei löydä tietokannasta airport-taulua
    kursori.execute(f'SELECT name, municipality FROM airport WHERE ident="{icao}"')
    result = kursori.fetchall()[0]
    return json.dumps({
        'ICAO': icao,
        'Name': result[0],
        'Municipality': result[1]
    })
if __name__ == '__main__': app.run(use_reloader=True, host='127.0.0.1', port=3000)
