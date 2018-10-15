# coding=utf-8

from utils import *

CLIENT = None


def init_client(ip):
    global CLIENT
    client = init_ssh_client(ip)
    CLIENT = client
    if client:
        return True
    else:
        return False


def test_example():
    command = 'sudo mkdir /etc/test/ && sudo chmod 777 /etc/test/ && cd /etc/test/'
    try:
        stdin, stdout, stderr = CLIENT.exec_command(command)

        st = stdout.read()
    except Exception as e:
        raise e
    else:
        assert st is not None
    finally:
        CLIENT.close()
