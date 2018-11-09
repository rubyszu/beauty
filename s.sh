#!/bin/bash
PATH=${PATH}:/usr/local/bin

for i in {1..10}
do
	python module/auth/verify_sms.py --branch=$0
	sleep 1m
done

