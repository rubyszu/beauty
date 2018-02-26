#!/bin/bash
PATH=${PATH}:/usr/local/bin

#pip install -U pytest
py.test --junitxml results.xml tests.py