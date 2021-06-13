from flask import jsonify

from classicML_server.service import fit_bp
from classicML_server.utils.status_codes import STATUS_CODES


@fit_bp.route('/', methods=['POST'])
def fit():
    """classicML-server的训练服务api.
    """
    response_dict = dict()

    response_dict['status_code'] = STATUS_CODES['OK']
    response_dict['information'] = 'Test information.'

    return jsonify(response_dict)
