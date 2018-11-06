# os_test

Automation test tool.


[![GitHub issues](https://img.shields.io/github/issues/Aisuko/os_test.svg)](https://github.com/Aisuko/os_test/issues) [![GitHub forks](https://img.shields.io/github/forks/Aisuko/os_test.svg)](https://github.com/Aisuko/os_test/network) [![GitHub stars](https://img.shields.io/github/stars/Aisuko/os_test.svg)](https://github.com/Aisuko/os_test/stargazers) [![Build Status](https://travis-ci.com/Aisuko/os_test.svg?branch=tox)](https://travis-ci.com/Aisuko/os_test) [![GitHub license](https://img.shields.io/github/license/Aisuko/os_test.svg)](https://github.com/Aisuko/os_test/blob/tox/LICENSE)


# Requirement

> It's necessary that your operation system have been installed python succeed.

 Tox was used `virtualenv` to create environment, so, there was must be installed `virtualenv` for your base python environment.
 
 ```angular2html
# If you have py3

pip3 install virtualenv

```

* Second step, let's create virtualenv with `virtualenv`

```angular2html
virtualenv --python='python version had been install your operations system'  your_env_name

# exec in your env
source /your_env_name/bin/activate

```

* Initializing environment which you have been created with requirements.txt

 ```angular2html
    pip install -r requirements.txt
 ```

* Run your test case with command `pytest -s engine/ --cloud-config-url=cloud config path`

# Succeed tested with tox

![Scucceed pic](https://github.com/Aisuko/os_test/blob/tox/succeed.png)

# License

Copyright 2018 [Aisuko](https://github.com/Aisuko/os_test/blob/master/LICENSE)

Licensed under the Apache License, Version 2.0 (the "License");you may not use this file except in compliance with the License.You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS,WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
