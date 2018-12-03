# -*- coding: utf-8 -*-
from resolve_stage import getStage
from context.context import Context
from request import Request
from response import saveParamsToContext, validateResponse

def runStage(stage, cli_args):
    
    context = Context(cli_args)
	# 前提条件
    if "pre_stage" in stage:
        pre_stage, _ = Request(stage.pre_stage).sendRequest(context.data) 
    
    stage, response = Request(stage).sendRequest(context.data)
    
    try:
        validateResponse(stage, response)
    except Exception as e:
        e.stage = stage
        e.response = response
        raise e
        
    saveParamsToContext(stage, context.data)
    context.sync()