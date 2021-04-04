from classicML_server import predict
from classicML_server import service_app
from classicML_server import load_model


@service_app.route('/predict', methods=['POST'])
def service_wrapper():
    with open('.classicML-server/server.conf', mode='r') as fp:
        conf = fp.readlines()

    # TODO(Steve R. Sun): 模型加载需要改进成, 仅启动一次.
    model = load_model(model_type=conf[0][:-1],
                       model_path=conf[1][:-1])

    return predict.predict_service(model)
