import os
import argparse

parser = argparse.ArgumentParser()


def main():
    if not os.path.exists('.classicML-server/'):
        os.makedirs('.classicML-server/')

    parser.add_argument('-mt', '--model_type', help='模型的类型')
    parser.add_argument('-mp', '--model_path', help='模型的存放路径')
    parser.add_argument('-H', '--host', default='127.0.0.1', help='服务监听的主机名')
    parser.add_argument('-P', '--port', type=int, default=5000, help='Web服务的端口')

    with open('.classicML-server/server.conf', mode='w+') as fp:
        fp.write(parser.parse_args().model_type + '\n')
        fp.write(parser.parse_args().model_path + '\n')

    command = ('gunicorn --bind=%s:%d '
               'classicML_server.service_wrapper:service_app') % (parser.parse_args().host, parser.parse_args().port)
    os.system(command)
