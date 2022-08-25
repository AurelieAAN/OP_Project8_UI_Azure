import numpy as np
import base64
import json                
import requests
import pickle
import tensorflow as tf

url = 'https://app-project8-weu-001.azurewebsites.net/predict'

def prediction(image_file):
    im_bytes = tf.keras.utils.load_img(image_file)      
    #im_b64 = base64.b64encode(tf.keras.utils.img_to_array(im_bytes))#.decode("utf8")
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    img = tf.keras.utils.img_to_array(im_bytes)
    serialized_as_json = json.dumps({"image":pickle.dumps(img).decode('latin-1')})
    response = requests.post(url, data=serialized_as_json, headers=headers)
    data = response.json()
    return data