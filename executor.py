# coding = utf-8
# Create date: 2018-10-29
# Author :Bowen Lee


import pytest

if __name__ == '__main__':

    try:
        pytest.main()
    except Exception as e:
        print(e.args[0])
