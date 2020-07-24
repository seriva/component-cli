import sys
import platform
import json
import socket
import os
import subprocess

from Log import Log
from Config import Config

def info():
    logger = Log('info')
    config = Config()

    def dump_external_info(title, args):
        logger.info('')
        logger.info(f'*****{title}******')
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        out, err = p.communicate()
        lines = filter(lambda x: x.strip(), out.decode("utf-8").splitlines())
        for l in lines: 
            logger.info(l)

    def dump_class(title, clazz):
        logger.info('')
        logger.info(f'*****{title}******')
        for attr in clazz.__dict__:
            if attr.startswith('_'):
                logger.info('%s = %r' % (attr[1:], getattr(config, attr)))

    def dump_dict(title, dic):
        logger.info('')
        logger.info(f'*****{title}******')
        for x, y in dic.items():
            logger.info('%s = %r' % (x, y))

    logger.info('*****COMPONENT******')
    name = os.environ.get('C_NAME')
    version = os.environ.get('C_VERSION')
    logger.info(f'Name: {name}')
    logger.info(f'Version: {version}')

    dump_class('*****CONFIG******', config)

    dump_dict('*****SYSTEM******', {
        'platform':platform.system(),
        'release':platform.release(),
        'type': platform.uname().system,
        'arch': platform.uname().machine,
        'cpus': json.dumps(os.cpu_count()),
        'hostname': socket.gethostname()
    })

    dump_dict('*****ENVIROMENT VARS******', dict(os.environ))

    dump_dict('*****PYTHON******', {
        'python_version':platform.python_version(),
        'python_build':platform.python_build(),
        'python_revision': platform.python_revision(),
        'python_compiler': platform.python_compiler(),
        'python_branch': platform.python_branch(),
        'python_implementation': platform.python_implementation()
    })

    dump_external_info('TERRAFORM VERSION', ['terraform', '--version'])
    dump_external_info('AZURECLI VERSION', ['az', '--version'])
    dump_external_info('ANSIBLE VERSION', ['ansible', '--version'])
    dump_external_info('ANSIBLE CONFIG', ['ansible-config', 'dump'])
    dump_external_info('ANSIBLE-VAULT VERSION', ['ansible-vault', '--version'])

    return 0