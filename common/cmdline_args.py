# -*- coding: utf-8 -*-
import sys
import argparse

#获取命令行参数
def getCmdlineArgs(key):
  parser = argparse.ArgumentParser(description='get api testcase running args')
  parser.add_argument('--env',nargs='?',help='api running environment' , choices=['production','development'],default='production')
  parser.add_argument('--branch',nargs='?',help='api running branch',default='v1',required=False)
  parser.add_argument('--case_path',nargs='?',help='loading cases file path')
  parser.add_argument('--pattern',nargs='?',help='futestcase name rule')
  args = parser.parse_args(sys.argv[1:]).__dict__
  if args.has_key(key):
    return args[key]
  else:
    return None

if __name__ == '__main__':
  print getCmdlineArgs("env")
  print getCmdlineArgs("branch")