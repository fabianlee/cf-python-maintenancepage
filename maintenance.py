"""Cloud Foundry test"""
from flask import Flask
from flask import jsonify
import os

app = Flask(__name__)

port = int(os.getenv("PORT"))

@app.route('/')
def return_maintenance_message():
    return "INDEX: " + os.getenv("MAINTENANCE_MESSAGE")

@app.route('/503')
def maintenance_503():
    return '<h1>503 ' + os.getenv("MAINTENANCE_MESSAGE")  + '</h1>', 503

@app.route('/json')
def maintenance_json():
    return jsonify(type='Exception',status=503,response=os.getenv("MAINTENANCE_MESSAGE")), 200, {'StatusHeader': 'Status: maintenance window'}

@app.route('/<path:dummy>')
def fallback(dummy):
    return "FALLBACK trying to reach /" + dummy + ": " + os.getenv("MAINTENANCE_MESSAGE")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
