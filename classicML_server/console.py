"""命令行启动工具."""
import os
import json
import argparse

parser = argparse.ArgumentParser()


def main():
    if not os.path.exists('.classicML-server/'):
        os.makedirs('.classicML-server/')

    parser.add_argument('-MT', '--model_type', type=str, help='模型的类型')
    parser.add_argument('-MP', '--model_path', type=str, help='模型的存放路径')
    parser.add_argument('-H', '--host', default='127.0.0.1', help='服务监听的主机名')
    parser.add_argument('-P', '--port', type=int, default=5000, help='Web服务的端口')

    with open('.classicML-server/conf.json', mode='w+') as fp:
        json.dump({
            'model_type': parser.parse_args().model_type,
            'model_path': parser.parse_args().model_path,
        }, fp)

    command = ('gunicorn --bind=%s:%d '
               'classicML_server.service_wrapper:service_app') % (parser.parse_args().host, parser.parse_args().port)
    os.system(command)
