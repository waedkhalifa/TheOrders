#The order server maintains
# a list of all orders received for the books.


from flask import Flask


app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=7000)