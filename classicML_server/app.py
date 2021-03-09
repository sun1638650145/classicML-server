import argparse

import numpy as np
import classicML as cml
from flask import Flask
from flask import request
from flask import jsonify

parser = argparse.ArgumentParser()
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def flask_predict():
    data = request.get_json()

    x = np.asarray(data['x'])
    if len(x.shape) == 1:
        x = np.expand_dims(x, axis=0)

    model = cml.models.LogisticRegression()
    model.load_weights(parser.parse_args().model_path)

    y_pred = model.predict(x).tolist()

    return jsonify({'predictions': y_pred})


def main():
    parser.add_argument('-mt', '--model_type', help='模型的类型')
    parser.add_argument('-mp', '--model_path', help='模型的存放路径')
    parser.add_argument('-H', '--host', default='127.0.0.1', help='服务监听的主机名')
    parser.add_argument('-P', '--port', type=int, default=5000, help='Web服务的端口')
    # 运行服务.
    app.run(host=parser.parse_args().host, port=parser.parse_args().port)