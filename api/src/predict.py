import numpy as np

from darkflow.net.build import TFNet
from flask import Flask, request, jsonify
from flask_cors import CORS

from api.src import *


flask_app = Flask(__name__)
flask_app.config['JSON_AS_ASCII'] = False
CORS(flask_app)

tf_net = TFNet({'model': MODEL_PATH, 'load': WEIGHTS_PATH, 'threshold': MODEL_THRESHOLD})


@flask_app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    try:
        frame = np.array(data['frame']).astype('float32')
        results = tf_net.return_predict(frame)
        for idx in range(0, len(results)):
            if 'confidence' in results[idx]:
                results[idx]['confidence'] = float(results[idx]['confidence'])
    except Exception as e:
        print(f'Exception: [{e}]')
        return jsonify(error=True, results=None)

    return jsonify(error=False, results=results)
