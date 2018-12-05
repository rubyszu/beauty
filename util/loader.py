#  -*- coding: utf-8 -*-
import os
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

# 修改JsonLoader类方法，支持解析yaml文件$ref部分，转换成json
class SchemaLoader(jsonref.JsonLoader):
    def is_yaml_file(self,uri):
        return re.search(r'\w+.yaml', uri) != None

    def get_remote_json(self, uri, **kwargs):
        if self.is_yaml_file(uri):
            #  yaml in ref
            # import pdb;pdb.set_trace()
            ref_yaml, _ = urlparse.urldefrag(uri)
            result = yaml.load(urlopen(ref_yaml).read().decode("utf-8"))
            return result
        else:
            if PY3:
                return super().get_remote_json(uri,**kwargs)
            else:
                return super(SchemaLoader,self).get_remote_json(uri,**kwargs)

# 读json/yaml格式的文件，转换成dictionary类型的数据
def loadSchema(file):
    # Loads the given schema file
    real_path = os.path.realpath('.')
    base_url = 'file://{}/'.format(real_path)

    abs_path = os.path.abspath(file)
    base_path = 'file://{}/'.format(abs_path)
    dir_path = os.path.dirname(base_path)
    
    return jsonref.load_uri(urlparse.urljoin(base_url,file), loader=SchemaLoader(), base_uri=dir_path, jsonschema=True)

class IncludeLoader(yaml.SafeLoader):
    """YAML Loader with `!include` constructor."""

    def __init__(self, stream):
        """Initialise Loader."""

        try:
            self._root = os.path.split(stream.name)[0]
        except AttributeError:
            self._root = os.path.curdir

        super(IncludeLoader, self).__init__(stream)


def construct_include(loader, node):
    """Include file referenced at node."""

    filename = os.path.abspath(os.path.join(loader._root, loader.construct_scalar(node)))
    extension = os.path.splitext(filename)[1].lstrip('.')

    with open(filename, 'r') as f:
        if extension in ('yaml', 'yml'):
            return yaml.load(f, IncludeLoader)
        elif extension in ('json', ):
            return json.load(f)
        else:
            return ''.join(f.readlines())

yaml.add_constructor('!include', construct_include, IncludeLoader)

def loadInclude(file):
    with open(file, 'r') as f:
        data = yaml.load(f, IncludeLoader)
    return data

if __name__ == '__main__':
    file = "./api_schemas/api/project/auth/login1.yaml"
    print loadSchema(file)




