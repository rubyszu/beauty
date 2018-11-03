# -*- coding: utf-8 -*-
from os.path import join, dirname, realpath
import jsonref
import re
import json,yaml
import sys
PY3 = sys.version_info[0] >= 3
if PY3:
    from urllib import parse as urlparse
    from urllib.request import urlopen
else:
    import urlparse
    from urllib2 import urlopen

#修改JsonLoader类方法，支持解析yaml文件$ref部分，转换成json
class FileLoader(jsonref.JsonLoader):
    def is_yaml_file(self,uri):
        return re.search(r'\w+.yaml', uri) != None

    def get_remote_json(self, uri, **kwargs):
        if self.is_yaml_file(uri):
            # yaml in ref
            ref_yaml, _ = urlparse.urldefrag(uri)
            result = yaml.load(urlopen(ref_yaml).read().decode("utf-8"))
            return result
        else:
            if PY3:
                return super().get_remote_json(uri,**kwargs)
            else:
                return super(FileLoader,self).get_remote_json(uri,**kwargs)


#读json/yaml格式的文件，转换成dictionary类型的数据
def loadFile(filename):
    #Loads the given schema file
    base_path = realpath('.')
    base_url = 'file://{}/'.format(base_path)

    return jsonref.load_uri(urlparse.urljoin(base_url,filename), loader=FileLoader(), base_uri=base_url, jsonschema=True)




