"""classicML web service."""
__version__ = '0.1a3'

import logging
import os

from flask import Flask

# 配置系统logger
logging.basicConfig(level=logging.INFO)
CLASSICML_SERVER_LOGGER = logging.getLogger(name='classicML-server')

# 配置使用CC后端
os.environ['CLASSICML_ENGINE'] = 'CC'

# api版本描述信息
api_version = 'v0'


def create_app():
    """创建应用.

    Returns:
        flask 应用.
    """
    CLASSICML_SERVER_LOGGER.info('classicML Web 服务已经启动')
    app = Flask(__name__)

    from classicML_server.service import fit
    from classicML_server.service import predict

    if os.environ['CMLS_SM'] == 'fit_service':
        app.register_blueprint(fit.fit_bp)
    elif os.environ['CMLS_SM'] == 'predict_service':
        app.register_blueprint(predict.predict_bp)

    return app
