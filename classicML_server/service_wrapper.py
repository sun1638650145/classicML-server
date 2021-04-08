"""将服务添加上路由信息."""
import json

from classicML_server import service_app
from classicML_server.service import predict
from classicML_server.core import load_model


@service_app.route('/predict', methods=['POST'])
def service_wrapper():
    """服务修饰器, 将服务映射到服务器后台.
    """
    with open('.classicML-server/conf.json', mode='r') as fp:
        conf = json.load(fp)

    # TODO(Steve R. Sun): 模型加载应仅硬启动一次.
    model = load_model(model_type=conf['model_type'],
                       model_path=conf['model_path'])

    return predict.predict_service(model)
