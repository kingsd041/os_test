# coding = utf-8
# Create date: 2018-10-29
# Author :Bowen Lee


def test_hostname(ros_kvm):
    """
    Test case for check hostname after rancher os has been installed succeed.
    :param ros_kvm:
    :return:
    """
    command = 'hostname'
    feed_back = 'rancher-test'
    client = ros_kvm(cloud_config='http://192.168.1.24/ros/cloud-config.yml')
    client.sendline(command)
    number = client.expect(feed_back, timeout=20)

    command_etc = 'cat /etc/hosts'
    client.sendline(command_etc)
    number_etc = client.expect(feed_back, timeout=20)
    assert (number == 0 and number_etc == 0)
