from flask import Flask
import json
app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    alku = False
    luku = int(luku)
    for i in range(2, luku):
        if (luku % 1) == 0:
            alku = True
            break
    return json.dumps({
        'Number': luku,
        'isPrime': alku
    })
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
