import json
import requests
import logging.config
import sys
import os
import sqlite3
from flask import Flask, request, jsonify
from itertools import cycle
app = Flask(__name__)

class DataBase:    
    def __init__(self):
        print("BBDD")

    def confirmarSeleccion(self):

        try:
             # We save in a variable the request that comes from eva
            req_body = request.json
            items_list = ( req_body['openContext']['selectedMaterialsList'])
            
            result = {
                "openContext":req_body["openContext"],
                "visibleContext":req_body["visibleContext"],
                "hiddenContext":req_body["hiddenContext"],
                #It is strict to put this option since the previous validations indicate that this option will be carried out and the flow will end
                "option" : "CONFIRMED_SELECTION"
            }
            result["hiddenContext"]["selectedMaterialsList"] = items_list

            # returns in JSON format the response in eva format
            return result
        

        except:
        # If any error happens, this is the answer with the formatvo eva
           result = {
                "openContext" : {},
                "visibleContext" : {},
                "hiddenContext": {},
                "option" : "ERROR"
            }
        # returns in JSON format the response in eva format
        return result


@app.route("/confirmar_seleccion", methods=["POST"])

def test_functions(self):
    database = DataBase()    
    return database.confirmarSeleccion()
    
if __name__ == "__main__":
    app.run(debug=True, port=8002, ssl_context='adhoc')