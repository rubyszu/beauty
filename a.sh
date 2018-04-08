#!/bin/bash
PATH=${PATH}:/usr/local/bin

#pip install -U pytest
# py.test --junitxml results.xml tests.py

cd run && python run_all_test.py

# cd module/login && py.test --junitxml results.xml test_login_200.py