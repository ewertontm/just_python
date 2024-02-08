!pip install flask_ngrok


import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request, jsonify, Flask
import random as rk
app = Flask(__name__) #the name of the application package run_with_ngrok(app)


d = [{ "number": 1, "name": "Nikola", "age": 60, "city": "Bangalore", "country": "India" }, { "number": 2, "name": "Alex", "age": 20, "city": "London", "country": "UK" }, { "number": 3, "name": "Samantha", "age": 28, "city": "San Francisco", "country": "USA" }, { "number": 4, "name": "Carly", "age": 30, "city": "Toronto", "country": "Canada" }, { "number": 5, "name": "John", "age": 25, "city": "Paris", "country": "France" }]

@app.route("/") 
@app.route("/input")
def input_route():
    return jsonify({"data": d})

if __name__ == "__main__":
    app.run()
    app.run()
