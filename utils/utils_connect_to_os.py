# coding=utf-8

import os
import pytest
import paramiko
from config import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Function tips, It was defined that function can be used by a parameter. Init once time
# @pytest.fixture(scope='session')
def init_ssh_client():
    try:
        # TODO Need to check folder which was named logs
        paramiko.util.log_to_file(BASE_DIR + '/logs/ssh.log')
        config = _get_os_config()
        key = paramiko.RSAKey.from_private_key_file(config.get('amazon_hvm').get('private_key_path'))
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(hostname=config.get('amazon_os').get('ip'),
                       username=config.get('amazon_os').get('username'),
                       pkey=key, allow_agent=False, look_for_keys=False)
        command = 'uname -a'
        stdin, stdout, stderr = client.exec_command(command)
        st = stdout.read()
        print(st.__repr__())
    except Exception as e:
        client.close()
        raise e
    else:
        return client


def _get_os_config():
    return hvm_configs


def pull_file():
    try:
        paramiko.util.log_to_file(BASE_DIR + '/logs/amazon_os.log')
        config = _get_os_config()
        key = paramiko.RSAKey.from_private_key_file(config.get('amazon_os').get('private_key_path'))
        transport = paramiko.Transport(config.get('amazon_os').get('ip'), 22)
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
