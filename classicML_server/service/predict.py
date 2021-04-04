import numpy as np

from flask import request
from flask import jsonify

from classicML_server import CLASSICML_SERVER_LOGGER


def predict_service(model):
    """预测服务."""
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
