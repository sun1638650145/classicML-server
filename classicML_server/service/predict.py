import os

import numpy as np
from flask import jsonify, request

from classicML_server import CLASSICML_SERVER_LOGGER
from classicML_server.core import load_model
from classicML_server.service import predict_bp
from classicML_server.utils.status_codes import STATUS_CODES


@predict_bp.route('/', methods=['POST'])
def predict():
    """classicML-server的预测服务api.

    Returns:
        JSON格式的信息, 正确将是模型预测的结果信息, 错误的话就是异常信息.

    Raises:
        KeyError: 服务器接收的JSON格式异常, 无法解析.
        OSError: 服务器内部异常.
    """
    data = request.get_json()
    response_dict = dict()

    try:
        model = load_model(os.environ['CMLS_MT'], os.environ['CMLS_MP'])

        x = np.asarray(data['x'])
        if len(x.shape) == 1:
            x = np.expand_dims(x, axis=0)
        y_preds = model.predict(x).tolist()

        response_dict['status_code'] = STATUS_CODES['OK']
        response_dict['predictions'] = y_preds
    except (KeyError, ValueError):
        CLASSICML_SERVER_LOGGER.error('服务器接收的JSON格式异常, 无法解析.')

        response_dict['status_code'] = STATUS_CODES['INVALID_REQUEST']
        response_dict['error'] = 'The received JSON format by the server is abnormal and cannot be parsed.'
    except OSError:

        response_dict['status_code'] = STATUS_CODES['INTERNAL_SERVER_ERROR']
        response_dict['error'] = 'The service is currently abnormal.'

    return jsonify(response_dict)
