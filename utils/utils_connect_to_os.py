# coding=utf-8

import os
import pytest
import paramiko
from config import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IP_OR_HOST = None


# Function tips, It was defined that function can be used by a parameter. Init once time
def init_ssh_client(ip):
    """

    :param ip:
    :return:
    """
    try:
        global IP_OR_HOST
        IP_OR_HOST = ip
        paramiko.util.log_to_file(BASE_DIR + '/logs/ssh.log')
        config = _get_hvm_config()
        key = paramiko.RSAKey.from_private_key_file(config.get('amazon_hvm').get('private_key_path'))
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(hostname=ip,
                       username=config.get('amazon_hvm').get('username'),
                       pkey=key, allow_agent=False, look_for_keys=False)
    except Exception as e:
        client.close()
        raise e
    else:
        return client


def pull_file():
    """
    Upload file to remote server.
    :return:
    """
    try:
        global IP_OR_HOST
        paramiko.util.log_to_file(BASE_DIR + '/logs/amazon_os.log')
        config = _get_hvm_config()
        key = paramiko.RSAKey.from_private_key_file(config.get('amazon_hvm').get('private_key_path'))
        transport = paramiko.Transport(IP_OR_HOST, 22)
        transport.connect(username=config.get('amazon_hvm').get('username'), pkey=key)
        sftp = paramiko.SFTPClient.from_transport(transport)
        p = sftp.put(BASE_DIR + '/logs/amazon_os.log', '/etc/test/amazon_os.log')
        # sftp.get('remove_path', 'local_path')
        transport.close()
    except Exception as e:
        transport.close()
        raise e
    else:
        return transport


def _get_hvm_config():
    """
    Get hvm config
    :return:
    """
    return hvm_configs


def get_ip_tuple():
    """

    :return:
    """
    ip_tuple = hvm_configs.get('amazon_hvm').get('ip')
    if not ip_tuple:
        raise Exception('Config is None')
    else:
        return ip_tuple
