# coding=utf-8


from engine import *

if __name__ == '__main__':
    print('===================================')
    print('Init system by following the config')
    print('===================================')

    number = input('Amazon os please input y:')
    if str(number).lower().strip() == 'y':
        get_amazon_client()
    else:
        get_client()
    print('===================================')
    pytest.main()
