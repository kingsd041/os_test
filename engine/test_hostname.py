# coding = utf-8
# Create date: 2018-10-29
# Author :Bowen Lee


def test_hostname(ros_kvm, cmd_opt):
    """
    Test case for check hostname after rancher os has been installed succeed.
    :param ros_kvm:
    :return:
    """

    command = 'hostname'
    feed_back = 'rancher-test'
    client = ros_kvm(cloud_config='{url}/test_hostname.yml'.format(url=cmd_opt))
    client.sendline(command)
    number = client.expect(feed_back, timeout=20, searchwindowsize=None)
    feed_back_content = str(client.after, encoding='utf-8')

    command_etc = 'cat /etc/hosts'
    client.sendline(command_etc)
    number_etc = client.expect(feed_back, timeout=20, searchwindowsize=None)
    feed_back_etc_content = str(client.after, encoding='utf-8')
    assert ((number == 0 and feed_back == feed_back_content)
            and (number_etc == 0 and feed_back == feed_back_etc_content))
