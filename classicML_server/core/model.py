import classicML as cml
from flask import g

from classicML_server import CLASSICML_SERVER_LOGGER


def load_model(model_type, model_path):
    """加载模型以及对应的权重文件.

    Arguments:
        model_type: str, cml模型的名称.
        model_path: str, cml模型权重的位置.

    Returns:
        cml.models.Model 模型实例.

    Raises:
        AttributeError: 模型加载失败, 请检查你的模型名称.
    """
    if 'model' not in g:
        if model_type == 'AdaBoostClassifier':
            g.model = cml.models.AdaBoostClassifier()
        elif model_type in ('AveragedOneDependentEstimator', 'AODE'):
            g.model = cml.models.AveragedOneDependentEstimator()
        elif model_type in ('BackPropagationNeuralNetwork', 'BPNN'):
            g.model = cml.models.BackPropagationNeuralNetwork()
        elif model_type == 'BaggingClassifier':
            g.model = cml.models.BaggingClassifier()
        elif model_type == 'DecisionTreeClassifier':
            g.model = cml.models.DecisionTreeClassifier()
        elif model_type == 'KMeans':
            g.model = cml.models.KMeans()
        elif model_type in ('LinearDiscriminantAnalysis', 'LDA'):
            g.model = cml.models.LinearDiscriminantAnalysis()
        elif model_type == 'LogisticRegression':
            g.model = cml.models.LogisticRegression()
        elif model_type in ('NaiveBayesClassifier', 'NB'):
            g.model = cml.models.NaiveBayesClassifier()
        elif model_type in ('RadialBasisFunctionNetwork', 'RBF'):
            g.model = cml.models.RadialBasisFunctionNetwork()
        elif model_type in ('SuperParentOneDependentEstimator', 'SPODE'):
            g.model = cml.models.SuperParentOneDependentEstimator()
        elif model_type in ('SupportVectorClassifier', 'SVC'):
            g.model = cml.models.SupportVectorClassifier()
        else:
            CLASSICML_SERVER_LOGGER.error('模型加载失败, 请检查你的模型名称')
            raise AttributeError('模型加载失败, 请检查你的模型名称')

        # 加载对应的权重文件.
        g.model.load_weights(model_path)

    return g.model
