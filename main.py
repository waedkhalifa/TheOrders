# The order server maintains
# a list of all orders received for the books.
import json

from flask import Flask, abort, request, json, jsonify
import requests

app = Flask(__name__)

@app.route('/purchase/<int:id>', methods=['POST'])
def purchase(id):
    reqGET = requests.get('http://192.168.100.8:7000/info/{}'.format(id))

    if reqGET.status_code == 200:
        dataDictionary = reqGET.json()  # content of json as dictionary
        if dataDictionary['quantity'] < 1:
            return '', 406

    elif reqGET.status_code == 404:
        return 'The server has not found anything matching the URI given', 404

    else:
        return 'Status code indicates to something ERROR!', reqGET.status_code


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
