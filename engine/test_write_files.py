# coding = utf-8
# Create date: 2018-10-31
# Author :Hailong


def test_write_files(ros_kvm):
    """
    Test case for check write files after rancher os has been installed succeed.
    :param ros_kvm:
    :return:
    """
    command = 'sudo cat /test'
    feed_back = 'console content'
    client = ros_kvm(cloud_config='http://192.168.1.24/ros/test_write_files/cloud-config.yml')
    client.sendline(command)
    number = client.expect(feed_back, timeout=20)

    command_b = 'sudo cat /test2'
    feed_back_b = 'console content'
    client.sendline(command_b)
    number_b = client.expect(feed_back_b, timeout=20)

    command_c = 'sudo system-docker exec ntp cat /test'
    feed_back_c = 'ntp content'
    client.sendline(command_c)
    number_c = client.expect(feed_back_c, timeout=20)

    command_d = 'sudo system-docker exec syslog cat /test'
    feed_back_d = 'syslog content'
    client.sendline(command_d)
    number_d = client.expect(feed_back_d, timeout=20)
    assert (number == 0 and number_b == 0 and number_c == 0 and number_d == 0)
