# coding=utf-8


from engine import *

if __name__ == '__main__':
    print('===================================')
    print('Init system by following the config')
    print('===================================')

    try:
        ip_tuple = get_ip_tuple()
        for ip in ip_tuple:
            if init_client(ip):
                print('===================================')
                print('Init succeed')
                pytest.main()
                # pull_file(ip)
                print('===================================')
                print('End of test')
                print('===================================')
            else:
                print('===================================')
                print('Init failed')
                print('===================================')
    except Exception as e:
        pass
