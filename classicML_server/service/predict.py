import os

import numpy as np
from flask import jsonify, request

from classicML_server import CLASSICML_SERVER_LOGGER
from classicML_server.core import load_model
from classicML_server.service import predict_bp


@predict_bp.route('/', methods=['POST'])
def predict():
    """classicML-server的预测服务api.

    Returns:
        JSON格式的信息, 正确将是模型预测的结果信息, 错误的话就是异常信息.

    Raises:
        KeyError: 接收的JSON格式异常, 无法解析.
    """
    data = request.get_json()

    # 加载模型.
    model = load_model(os.environ['CMLS_MT'], os.environ['CMLS_MP'])

    try:
        x = np.asarray(data['x'])
        if len(x.shape) == 1:
            x = np.expand_dims(x, axis=0)
        y_preds = model.predict(x).tolist()
    except KeyError:
        CLASSICML_SERVER_LOGGER.error('服务器接收的JSON格式异常, 无法解析.')

        return jsonify({'information': 'The received JSON format by the server is abnormal and cannot be parsed.'})

    return jsonify({'predictions': y_preds})
