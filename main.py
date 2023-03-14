import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    dt = datetime.datetime.now()
    return render_template('index.html', date=dt)

@app.route('/mappa/<width>', methods=['GET'])
def mappa(width,height):
    return render_template('mappa.html', width=width)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)