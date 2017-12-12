#!/bin/bash
pip install -U pytest
py.test --junitxml results.xml tests.py