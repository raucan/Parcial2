import flask
from flask import request, jsonify, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

vacunas = [
    {'id':0,
     'year': 1990,
     'vacunados': 73
     },
    {'id':1,
     'year': 2000,
     'vacunados': 97
     },
    {'id':2,
     'year': 2011,
     'vacunados': 97
     },
    {'id':3,
     'year': 2012,
     'vacunados': 98
     },
    {'id':4,
     'year': 2013,
     'vacunados': 92
     },
    {'id':5,
     'year': 2014,
     'vacunados': 90
     },
    {'id':6,
     'year': 2015,
     'vacunados': 93
     },
    {'id':7,
     'year': 2016,
     'vacunados': 95
     },
    {'id':8,
     'year': 2017,
     'vacunados': 98
     },
    {'id':9,
     'year': 2018,
     'vacunados': 98
     },
    {'id':10,
     'year': 2019,
     'vacunados': 98
     },
    {'id':11,
     'year': 2020,
     'vacunados': 97
     }
]

@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/vacunas/all', methods=['GET'])
def api_all():
    return jsonify(vacunas)

@app.route('/vacunas/', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "ERROR"
    resultado = []
    for vacuna in vacunas:
        if vacuna['id'] == id:
            resultado.append(vacuna)

    return jsonify(resultado)

app.run()