# -*- coding: utf-8 -*-

import sys
import argparse

def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('--branch', help='branchs')
  parser.add_argument('unittest_args', nargs='*')
  args = parser.parse_args()
  # TODO: Go do something with args.input and args.filename
  # Now set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
  return [args.branch, [sys.argv[0]] + args.unittest_args]
