"""classicML web service"""
__version__ = '0.1a1'

import logging

# 配置系统logger
logging.basicConfig(level=logging.INFO)
CLASSICML_SERVER_LOGGER = logging.getLogger(name='classicML-server')

from flask import Flask
service_app = Flask(__name__)

from classicML_server.service import predict
from classicML_server.utils import load_model
