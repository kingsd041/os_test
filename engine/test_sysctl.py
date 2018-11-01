# coding = utf-8
# Create date: 2018-09-01
# Author :Hailong


def test_sysctl(ros_kvm):
    """
    Test case for check sysctl after rancher os has been installed succeed.
    :param ros_kvm:
    :return:
    """
    command = 'sudo cat /proc/sys/kernel/domainname'
    feed_back = 'test'
    client = ros_kvm(cloud_config='http://192.168.1.24/ros/test_sysctl/cloud-config.yml')
    client.sendline(command)
    number = client.expect_exact(feed_back, timeout=10)

    command_b = 'sudo cat /proc/sys/dev/cdrom/debug'
    feed_back_b = '1'
    client.sendline(command_b)
    number_b = client.expect_exact(feed_back_b, timeout=20)
    assert (number == 0 and number_b == 0)
