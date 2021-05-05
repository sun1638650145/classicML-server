"""classicML web service."""
__version__ = '0.1a3'

import logging

from flask import Flask

# 配置系统logger
logging.basicConfig(level=logging.INFO)
CLASSICML_SERVER_LOGGER = logging.getLogger(name='classicML-server')


def create_app():
    """创建应用.

    Returns:
        flask 应用.
    """
    CLASSICML_SERVER_LOGGER.info('classicML Web 服务已经启动')
    app = Flask(__name__)

    from classicML_server.service import predict
    app.register_blueprint(predict.predict_bp)

    return app
