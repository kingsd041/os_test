# coding = utf-8
# Create date: 2018-10-29
# Author :Bowen Lee


def test_hostname(ros_kvm_with_paramiko, cmd_opt):
    """
    Test case for check hostname after rancher os has been installed succeed.
    :param ros_kvm_with_paramiko:
    :return:
    """

    command = 'hostname'
    feed_back = 'rancher-test'
    client = ros_kvm_with_paramiko(cloud_config='{url}/test_hostname.yml'.format(url=cmd_opt))

    stdin, stdout, stderr = client.exec_command(command, timeout=10)
    output = stdout.read().decode('utf-8')
    assert (feed_back in output)

    command_etc = 'cat /etc/hosts'
    stdin, stdout, stderr = client.exec_command(command_etc, timeout=10)
    output_command = stdout.read().decode('utf-8')
    client.close()
    assert (feed_back in output_command)
