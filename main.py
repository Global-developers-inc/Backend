from flask import Flask, request, jsonify
import SettingsManager


app = Flask(__name__)

@app.route('/<string:category>', methods=["POST"])
def post_handler(category):
   data = request.get_json()
   SettingsManager.CATEGORYS[category].post(data)

   return SettingsManager.CATEGORYS[category].post(data)
   

@app.route('/<string:category>', methods=["GET"])
def get_handler(category):
   return SettingsManager.CATEGORYS[category].get()
   

app.run()
