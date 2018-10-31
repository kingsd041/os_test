# coding = utf-8
# Create date: 2018-10-29
# Author :Bowen Lee


def test_environment(ros_kvm):
    """
    Test case for check enviroment after rancher os has been installed succeed.
    :param ros_kvm:
    :return:
    """
    command = 'sudo system-docker inspect env | grep A=A'
    feed_back = 'A=A'
    client = ros_kvm(cloud_config='http://192.168.1.24/ros/test_environment/cloud-config.yml')
    client.sendline(command)
    number = client.expect(feed_back, timeout=20)

    command_b = 'sudo system-docker inspect env | grep BB=BB'
    feed_back_b = 'BB=BB'
    client.sendline(command_b)
    number_b = client.expect(feed_back_b, timeout=20)

    command_c = 'sudo system-docker inspect env | grep BC=BC'
    feed_back_c = 'BC=BC'
    client.sendline(command_c)
    number_c = client.expect(feed_back_c, timeout=20)

    assert (number == 0 and number_b == 0 and number_c == 0)
