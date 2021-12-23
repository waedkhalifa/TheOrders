# The order server maintains
# a list of all orders received for the books.
import json
from flask import Flask, abort, request, json, jsonify
import requests

app = Flask(__name__)

@app.route('/purchase/<int:id>', methods=['POST'])
def purchase(id):
    reqGET = requests.get('http://192.168.56.101:7000/info/{}'.format(id))

    if reqGET.status_code == 200:
        dataDictionary = reqGET.json()  # content of json as dictionary
        if dataDictionary['quantity'] < 1:
            return '', 406
        else:
            #requests.post('http://192.168.56.105:9999/purchase/{}'.format(id))
            dataDictionary['quantity'] = dataDictionary['quantity'] - 1
            reqPUT = requests.put('http://192.168.56.101:7000/updateinfo/{}'.format(id), json=(dataDictionary))
            #print(reqPUT.status_code)
            if reqPUT.status_code == 200:
                print('fjvivffjjvvvvvvvvvvvvvvv')
                # The order server maintains
                # a list of all orders received for the books.
                f = open('ListOfOrders.json', 'r+')

                data = json.load(f)
                # for loop to
                data.append({'id': id, 'title': dataDictionary['title'], 'price': dataDictionary['price']})
                f.close()
                f2 = open('ListOfOrders.json', 'w')
                json.dump(data, f2)
                f2.close()
                return jsonify({'id': id, 'title': dataDictionary['title'], 'price': dataDictionary['price']})
            elif reqPUT.status_code == 404:
                return 'The server has not found anything matching the given URL', reqPUT.status_code
            else:
                return 'Status code indicates to something ERROR!', reqPUT.status_code

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)