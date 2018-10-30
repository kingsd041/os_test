# coding = utf-8
# Create date: 2018-10-29
# Author :Bowen Lee

from utils import *


def test_example(init_virtual_machine):
    command = 'hostname'
    feed_back = 'rancher-test'
    client = init_virtual_machine
    client.sendline(command)
    number = client.expect(feed_back, timeout=10)
    assert (number == 0)
