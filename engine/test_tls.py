# coding = utf-8
# Create date: 2018-10-31
# Author :Hailong
# Editor:Bowen Lee


def test_tls(ros_kvm_with_paramiko, cmd_opt):
    """
    Test case for check tls after rancher os has been installed succeed.
    :param:ros_kvm_with_paramiko,cmd_opt
    :return:
    """
    command = 'set -e -x && sudo ros tls gen && docker --tlsverify version'
    feed_back = 'Client'
    client = ros_kvm_with_paramiko(cloud_config='{url}/test_tls.yml'.format(url=cmd_opt))
    stdin, stdout, stderr = client.exec_command(command, timeout=10)
    # Must be save in local constant
    output_content = stdout.read().decode('utf-8')
    client.close()
    assert (feed_back in output_content)
