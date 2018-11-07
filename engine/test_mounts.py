# coding = utf-8
# Create date: 2018-10-29
# Author :Bowen Lee


def test_modules(ros_kvm_with_paramiko, cloud_config_url):
    command = 'lsmod | grep btrfs'
    client = ros_kvm_with_paramiko(cloud_config='{url}/test_modules.yml'.format(url=cloud_config_url))

    stdin, stdout, stderr = client.exec_command(command, timeout=10)
    output = stdout.read().decode('utf-8')
    print(output)
