#!/bin/bash
PATH=${PATH}:/usr/local/bin

for i in {1..1000}
do
	python module/task/test_add_one_task_200.py --branch=$1
done

