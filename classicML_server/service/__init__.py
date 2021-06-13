from flask import Blueprint

from classicML_server import api_version

predict_bp = Blueprint('predict', __name__, url_prefix='/%s/predict' % api_version)
fit_bp = Blueprint('fit', __name__, url_prefix='/%s/fit' % api_version)
