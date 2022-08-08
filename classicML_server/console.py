"""命令行启动工具."""
import os
import argparse

from waitress import serve

from classicML_server import create_app


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-SM', '--service_mode', type=str, help='服务的模式')
    parser.add_argument('-MT', '--model_type', type=str, help='模型的类型')
    parser.add_argument('-MP', '--model_path', type=str, help='模型的存放路径')
    parser.add_argument('-H', '--host', default='127.0.0.1', help='服务监听的主机名')
    parser.add_argument('-P', '--port', type=int, default=8051, help='Web服务的端口')

    os.environ.setdefault('CMLS_SM', parser.parse_args().service_mode)
    os.environ.setdefault('CMLS_MT', parser.parse_args().model_type)
    os.environ.setdefault('CMLS_MP', parser.parse_args().model_path)

    serve(app=create_app(),
          host=parser.parse_args().host,
          port=parser.parse_args().port)
