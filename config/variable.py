# -*- coding: utf-8 -*-
import json
import os

class GlobalVariable(object):
  def __init__(self, filename=None):
    self.json = dict()
    self.filename = filename or "variable.json"
    self.read()

  def read(self):
    if not os.path.exists(self.filename):
      open(self.filename, 'w').close()
    else:
      with open(self.filename) as f:
        data = f.read()
        if data:
          self.json = json.loads(data)

  def store(self, key, value):
    self.json[key] = value
    return self

  def write(self):
    data = json.dumps(self.json, indent=2)
    with open(self.filename, 'w') as f:
      f.write(data)
    self.json = None


def main():
  variable = GlobalVariable()
  variable.write()

if __name__ == '__main__':
  main()