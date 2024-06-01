from flask import Flask, jsonify, render_template, url_for
import random
import json

app = Flask(__name__)

with open('pokeneas.json', 'r') as f:
    pokeneas = json.load(f)

@app.route('/api/pokeneas', methods=['GET'])
def get_pokeneas():
    return render_template('pokeneas.html', pokeneas=pokeneas)

@app.route('/api/random_pokenea', methods=['GET'])
def get_random_pokenea():
    pokenea = random.choice(pokeneas)
    return render_template('random_pokenea.html', pokenea=pokenea)

@app.route('/')
def index():
    pokenea = random.choice(pokeneas)
    return render_template('index.html', pokenea=pokenea)

if __name__ == '__main__':
    app.run(debug=True)
