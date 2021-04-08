import classicML as cml

from classicML_server import CLASSICML_SERVER_LOGGER


def _get_model(model_type):
    """获取使用的模型.

    Arguments:
        model_type: str, cml 模型的名称.

    Returns:
        cml.models.Model 模型实例或None
    """
    if model_type in ('AveragedOneDependentEstimator', 'AODE'):
        return cml.models.AveragedOneDependentEstimator()
    elif model_type in ('BackPropagationNeuralNetwork', 'BPNN'):
        return cml.models.BackPropagationNeuralNetwork()
    elif model_type == 'DecisionTreeClassifier':
        return cml.models.DecisionTreeClassifier()
    elif model_type in ('LinearDiscriminantAnalysis', 'LDA'):
        return cml.models.LinearDiscriminantAnalysis()
    elif model_type == 'LogisticRegression':
        return cml.models.LogisticRegression()
    elif model_type in ('NaiveBayesClassifier', 'NB'):
        return cml.models.NaiveBayesClassifier()
    elif model_type in ('RadialBasisFunctionNetwork', 'RBF'):
        return cml.models.RadialBasisFunctionNetwork()
    elif model_type in ('SuperParentOneDependentEstimator', 'SPODE'):
        return cml.models.SuperParentOneDependentEstimator()
    elif model_type in ('SupportVectorClassifier', 'SVC'):
        return cml.models.SupportVectorClassifier()
    else:
        return None


def load_model(model_type, model_path):
    """加载模型, 并载入权重文件.

    Arguments:
        model_type: str, cml模型的名称.
        model_path: str, cml模型权重的位置.

    Returns:
        cml.models.Model 模型实例.

    Raises:
        AttributeError: 模型加载失败, 请检查你的模型名称.
        OSError: 模型权重初始化失败, 请检查你的模型文件.
    """
    try:
        model = _get_model(model_type)
        model.load_weights(filepath=model_path)
    except AttributeError:
        CLASSICML_SERVER_LOGGER.error('模型加载失败, 请检查你的模型名称')
        raise AttributeError('模型加载失败, 请检查你的模型名称')
    except OSError:
        CLASSICML_SERVER_LOGGER.error('模型权重初始化失败, 请检查你的模型文件')
        raise OSError('模型权重初始化失败, 请检查你的模型文件')

    return model
