# coding=utf-8

import os
import pytest
import paramiko
from config import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# @pytest.fixture()
def setup_os():
    try:
        paramiko.util.log_to_file(BASE_DIR + '/logs/os.log')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        configs = _get_os_config()
        ip = configs.get('os').get('ip')
        port = configs.get('os').get('port')
        username = configs.get('os').get('username')
        password = configs.get('os').get('password')

        ssh.connect(ip, username=username, password=password, allow_agent=True)
    except Exception as e:
        ssh.close()
        raise e
    else:
        return ssh


# Function tips, It was defined that function can be used by a parameter. Init once time
# @pytest.fixture(scope='session')
def setup_amazon():
    try:
        paramiko.util.log_to_file(BASE_DIR + '/logs/amazon_os.log')
        config = _get_os_config()
        key = paramiko.RSAKey.from_private_key_file(config.get('amazon_os').get('private_key_path'))
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(hostname=config.get('amazon_os').get('ip'),
                       username=config.get('amazon_os').get('username'),
                       pkey=key)
        command = 'uname -a'
        stdin, stdout, stderr = client.exec_command(command)
        st = stdout.read()
        # std = stderr.read()
    except Exception as e:
        client.close()
        raise e
    else:
        return client


def _get_os_config():
    return example_configs


def pull_file():
    try:
        paramiko.util.log_to_file(BASE_DIR + '/logs/amazon_os.log')
        config = _get_os_config()
        key = paramiko.RSAKey.from_private_key_file(config.get('amazon_os').get('private_key_path'))
        transport = paramiko.Transport((config.get('amazon_os').get('ip'), 22))
        transport.connect(username=config.get('amazon_os').get('username'), pkey=key)
        sftp = paramiko.SFTPClient.from_transport(transport)
        p = sftp.put(BASE_DIR + '/logs/amazon_os.log', '/etc/test/amazon_os.log')
        # sftp.get('remove_path', 'local_path')
        transport.close()
    except Exception as e:
        transport.close()
        raise e
    else:
        return transport


@pytest.fixture()
def teardown():
    print('Tear down all link')
