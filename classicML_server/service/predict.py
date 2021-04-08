import numpy as np

from flask import request
from flask import jsonify

from classicML_server import CLASSICML_SERVER_LOGGER


def predict_service(model):
    """classicML-server的预测服务API.

    Arguments:
        model: cml.models.Model, cml的模型实例.

    Returns:
        JSON格式的信息, 正确将是模型预测的结果信息, 错误的话就是异常信息.

    Raises:
        KeyError: 接收的JSON格式异常, 无法解析.
    """
    data = request.get_json()

    try:
        x = np.asarray(data['x'])
        if len(x.shape) == 1:
            x = np.expand_dims(x, axis=0)
        y_preds = model.predict(x).tolist()
    except KeyError:
        CLASSICML_SERVER_LOGGER.error('接收的JSON格式异常, 无法解析.')

        return jsonify({'information': 'The received JSON format is abnormal and cannot be parsed.'})

    return jsonify({'predictions': y_preds})
