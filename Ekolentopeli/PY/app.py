import json
from database import Database
from flask import Flask
from flask_cors import CORS

db = Database()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'

@app.route('/haeLentokentat') #Hakee lentokentän tietokannasta @Sakari Surenkin
def haeLentokentat():
    sql = f'''SELECT ident, name FROM airport'''
    kursori = db.get_conn().cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return json.dumps(tulos)

@app.route('/haeMaanosa/<ICAO>') #Hakee maanosan ICAO-koodin perusteella @Sakari Surenkin
def haeMaanosa(ICAO):
    tuple = (ICAO,)
    sql = f'''SELECT continent FROM airport WHERE ident = %s'''
    kursori = db.get_conn().cursor(dictionary=True)
    kursori.execute(sql, tuple)
    maanosa = kursori.fetchone()
    return json.dumps(maanosa[0])

@app.route('/lentokentanSijainti') #Hakee lentokenttien sijainnit tietokannasta @Sakari Surenkin
def lentokentanSijainti():
    kursori = db.get_conn().execute(f'''SELECT latitude_deg, longitude_deg FROM airport''')
    sijainti = kursori.fetchone(dictionary=True)
    return json.dumps(sijainti)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
