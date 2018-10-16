# coding=utf-8

from utils import *

CLIENT = None


def test_example():
    command = 'sudo mkdir /etc/test/ && sudo chmod 777 /etc/test/ && cd /etc/test/'
    try:
        ip_tuple = get_ip_tuple()
        for ip in ip_tuple:
            client = init_ssh_client(ip)
            stdin, stdout, stderr = client.exec_command(command)
            st = stdout.read()
            # TODO It's necessary to add save logs to local file.
            print(st)
            client.close()
    except Exception as e:
        raise e
