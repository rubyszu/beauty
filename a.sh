#!/bin/bash
PATH=${PATH}:/usr/local/bin

#pip install -U pytest
# py.test --junitxml results.xml tests.py

# cd module/test && python testsuit.py
# cd ...
# python run/run_all_test.py --branch=F5002

for i in $( seq 1 2 )
do
   python run/run_all_test.py --branch=dev
done

# cd module/login && py.test --junitxml results.xml test_login_200.py