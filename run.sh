#!/bin/bash
# PATH=${PATH}:/usr/local/bin

#pip install -U pytest
# py.test --junitxml results.xml tests.py

# cd module/test && python testsuit.py
# cd ...
# pip install -U tomorrow
# pip install ones
python run/run_all_test.py --branch=v1
python module/auth/test.py
# for i in $( seq 1 957 )
# do
#    python run/run_all_test.py --branch=$1
# done


# cd module/login && py.test --junitxml results.xml test_login_200.p7

# heee
