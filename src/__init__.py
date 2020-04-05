from flask import Flask
from flask import request
from ShoppingList import *
import json

app = Flask(__name__)
list = ShoppingList()
list.addElement("patate", 5)
list.addElement("patate", 3)
list.addElement("fogli", 18)
list.addElement("mela", 5)


@app.route('/test')
def hello_world():
    return {'name': 'gian', 'surname': 'bodas'}


@app.route('/shopping_list')
def getElementList():
    elementList = '{"count":' + str(list.getElementListCount()) + ','
    elementList = elementList + '"data":['
    for index, element in enumerate(list.getElementList()):
        if index:
            elementList = elementList + ','
        elementList = elementList + \
            '{ "name":"' + element.name + '", "quantity":' + \
            str(element.quantity) + "}"
    elementList = elementList + "]}"
    return elementList


@app.route('/shopping_list/add', methods=['POST', 'GET'])
def addElement():
    if request.method == 'POST':
        try:
            name = request.form['name']
            quantity = request.form['quantity']
        except Exception:
            return "Error on the input data you dumb ass"
        result = list.addElement(name, quantity)
        return '{"result":"' + result + \
            '","name":"'+name+'","quantity":' + \
            str(list.getElementQuantity(name))+'}'
    return "Get request nop"


app.run(host='127.0.0.1', port=80, debug=True)
