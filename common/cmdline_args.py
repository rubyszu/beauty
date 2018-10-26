# -*- coding: utf-8 -*-
import sys
import argparse

def getCmdlineArgs(key=1):
  parser = argparse.ArgumentParser(description='get api testcase running args')
  parser.add_argument('--env',nargs='?',help='api running environment' , choices=['production','development'],default='production')
  parser.add_argument('--branch',nargs='?',help='api running branch',required=False)
  parser.add_argument('--case_path',nargs='?',help='loading cases file path')
  # parser.add_argument('unittest_args', nargs='*')
  parser.add_argument('--pattern',nargs='?',help='testcase name rule')
  args = parser.parse_args(sys.argv[1:]).__dict__
  if args.has_key(key):
    return args[key]
  else:
    return None

if __name__ == '__main__':
  getCmdlineArgs("branch")