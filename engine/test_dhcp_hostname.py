# coding = utf-8
# Create date: 2018-10-29
# Author :Bowen Lee


def test_dhcp_hostname(ros_kvm_with_paramiko, cmd_opt):
    """
    Test case for check dncp hostname after rancher os has been installed succeed.
    :param ros_kvm_with_paramiko:
    :return:
    """

    command = 'hostname'
    feed_back = 'rancher'
    client = ros_kvm_with_paramiko(cloud_config='{url}/test_dncp_hostname.yml'.format(url=cmd_opt))
    stdin, stdout, stderr = client.exec_command(command, timeout=10)
    output = stdout.read().decode('utf-8')
    assert (feed_back in output)

    command_etc = 'cat /etc/hosts'
    stdin, stdout, stderr = client.exec_command(command_etc, timeout=10)
    output_etc = stdout.read().decode('utf-8')
    client.close()
    assert (output_etc in output_etc)
