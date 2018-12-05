# -*- coding: utf-8 -*-

import inspect
from jsonschema import validate
from util.loader import loadSchema
from util.dict_util import mergeDict
from util import comparators

comparators_functions = inspect.getmembers(comparators, inspect.isfunction)
validate_rule = {}

def generateValidateRule():
	for (name, func) in comparators_functions:
		validate_rule[name] = func

def validateResponseSchema(stage, response):
	# schema_file = loadSchema(stage.variables.response.schema)
	pass

def validateResponse(stage, response):
	'''
	Args:
		stage(dcit): stage
		response(requests.models.Response): response
		response_schema(dict): schema for response
	'''
	# status code
	status_code = stage.stage.response.status_code
	assert response.status_code == status_code

	# response schema
	validateResponseSchema(stage, response)

	# 读取规则动态生成规则映射字典
	if not validate_rule:
		generateValidateRule()

	# business
	if "business" not in stage.stage.response:
		return
	business = stage.stage.response.business
	for i in business:
		for key, value in i.items():
			validate_rule[key](*value)

def saveParamsToContext(stage, context):
	'''
	Args:
		stage(dict): stage
		context(dict): context
	'''
	if "save" not in stage:
		return {}
	mergeDict(context, stage.save)

if __name__ == '__main__':
	generateValidateRule()
	argumets = [1,1]
	validate_rule["equal"](*argumets)