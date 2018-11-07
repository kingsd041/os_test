# coding = utf-8
# Create date: 2018-10-31
# Author :Hailong



def test_tls(ros_kvm):
    """
    Test case for check tls after rancher os has been installed succeed.
    :param ros_kvm:
    :return:
    """
    command = 'set -e -x && sudo ros tls gen && docker --tlsverify version'
    feed_back = 'Server'
    client = ros_kvm(cloud_config='http://192.168.1.24/ros/test_tls/cloud-config.yml')
    client.sendline(command)
    number = client.expect(feed_back, timeout=10)
    client.close()
    assert (number == 0)