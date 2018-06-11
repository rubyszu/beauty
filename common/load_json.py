# -*- coding: utf-8 -*-
from os.path import join, dirname, realpath
import jsonref

def load_json_schema(filename):
    """ Loads the given schema file """

    base_path = realpath('./')
    absolute_path = realpath(filename)

    base_uri = 'file://{}/'.format(base_path)

    with open(absolute_path) as schema_file:
        return jsonref.loads(schema_file.read(), base_uri=base_uri, jsonschema=True)
        