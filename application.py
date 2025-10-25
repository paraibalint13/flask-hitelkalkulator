from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kalkulal', methods=['POST'])
def kalkulal():
    osszeg = float(request.form['osszeg'])
    ev = int(request.form['ev'])
    kamat = float(request.form['kamat']) / 100

    havi_kamat = kamat / 12
    honapok = ev * 12
    havi_torleszto = osszeg * (havi_kamat * (1 + havi_kamat)**honapok) / ((1 + havi_kamat)**honapok - 1)

    return render_template('eredmeny.html', havi_torleszto=round(havi_torleszto, 0))

if __name__ == '__main__':
    app.run(debug=True)
