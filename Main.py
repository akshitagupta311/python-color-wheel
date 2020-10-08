from flask import Flask, render_template, request
from flask_cors import CORS
import json

import Calculations

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def home():
   return render_template("Home.html")
 
@app.route('/calculate-color', methods=['POST'])
def calculate():
    data = request.get_data().decode('UTF-8')
    print ("Data: ", data)
    rgb = Calculations.hexa2rgb(data)
    print("RGB of ", data, " is ", rgb)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

app.run(debug=True)