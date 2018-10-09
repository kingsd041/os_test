# coding=utf-8

from utils import *

client = None


def get_amazon_client():
    global client
    client = setup_amazon()
    if client:
        print('Init succeed')
    else:
        print('Init failed')


def get_client():
    global client
    client = setup_os()
    if client:
        print('Init succeed')
    else:
        print('Init failed')


def test_example():
    command = 'sudo mkdir /etc/test/ && sudo chmod 777 /etc/test/ && cd /etc/test/'
    try:
        stdin, stdout, stderr = client.exec_command(command)

        st = stdout.read()
        pull_file()

    except Exception as e:
        raise e
    else:
        assert st is not None
    finally:
        client.close()
