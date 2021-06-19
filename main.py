from flask import Flask, request
from flask_cors import CORS, cross_origin
import SettingsManager


app = Flask(__name__)
CORS(app)

@app.route('/<string:category>', methods=["POST"])
@cross_origin()
def post_handler(category):
   data = request.get_json()
   SettingsManager.CATEGORYS[category].post(data)

   return SettingsManager.CATEGORYS[category].post(data)
   

@app.route('/<string:category>', methods=["GET"])
@cross_origin()
def get_handler(category):
   return SettingsManager.CATEGORYS[category].get()
   

app.run()
