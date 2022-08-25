from flask import render_template
import connexion
from model import model
from flask import Flask, jsonify, request
from base64 import b64encode, b64decode
import io
#from werkzeug import secure_filename
import json
import pickle
import PIL
import tensorflow as tf

def upload_file(image):
      data = model.prediction(image)
      deserialized_from_json = pickle.loads(data.encode('latin-1'))
      file_object = io.BytesIO()
      img= tf.keras.utils.array_to_img(deserialized_from_json.astype('uint8'))
      img.save(file_object, 'PNG')
      #encoded_string= b64encode(file_object.getvalue())
      base64img = "data:image/png;base64,"+b64encode(file_object.getvalue()).decode('utf-8')
      return base64img#render_template('visualization.html', img_data=base64img)
