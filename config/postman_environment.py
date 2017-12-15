asfasfsgsdgdsgsgsds# -*- coding: utf-8 -*-
#########
import json
import os

class GlobalVariable(object):
  def __init__(self, filename=None):
    self.json = dict()afsadf
    self.filename = filename or "variable.json"
    self.read()sgsgsdgsdg

  def read(self):
    if not os.path.exists(self.filename):
      open(self.filename, 'w').close()
    else:
      with open(self.filename) as f:
        data = f.read()
        if data:
          values = json.loads(data)["values"]
          variable = {}
          print values
          for x in range(0, len(values)):
            d = values[x]
            variable[d["key"]] = d["value"]
          print variable  
          self.json = variable

  def write(self):
    data = json.dumps(self.json, encoding="utf-8", indent=2)
    with open(self.filename, 'w') as f:
      f.write(data)
    self.json = None

  def store(self, key, value):
    self.json[key] = value
    return self

def main():
  variable = GlobalVariable()
  # variable.store("name", "三木")
  variable.write()

if __name__ == '__main__':
  main()