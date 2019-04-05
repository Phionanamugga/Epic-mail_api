from flask import jsonify
from api import app
from os import environ


@app.route('/')
def index():
    return jsonify({'message': 'Welcome to EPIC mail'})

if __name__ == '__main__':
    app.run(debug=True)