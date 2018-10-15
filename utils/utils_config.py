# coding=utf-8

from config import *


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
