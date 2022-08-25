from flask import render_template
import connexion
from controller import controller
from flask import Flask, jsonify, request
from base64 import b64encode, b64decode
import io
#from werkzeug import secure_filename
import json
import pickle
import PIL

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

@app.route('/')
def home():
 return render_template('home.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      base64img = controller.upload_file(f.filename)
      return render_template('visualization.html', img_data=base64img)

@app.route("/health", methods=['GET'])
def test_method():         
    return "ok"
