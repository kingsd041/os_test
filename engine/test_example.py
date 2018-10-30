# coding = utf-8
# Create date: 2018-10-29
# Author :Bowen Lee


def test_example(init_virtual_machine):
    command = 'hostname'
    feed_back = 'rancher-test'
    client = init_virtual_machine(cloud_config='http://192.168.1.24/ros/cloud-config.yml')
    client.sendline(command)
    number = client.expect(feed_back, timeout=10)
    assert (number == 0)
