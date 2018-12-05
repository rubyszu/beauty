# -*- coding: utf-8 -*-
from box import Box
from util.loader import loadSchema,loadInclude

def getStage(file):
	stage = Box(loadInclude(file))
	stage = resolveStage(stage)
	return stage

def resolveStage(stage):
	#pre_stage
	if "pre_stage" in stage:
		pre_stage = getStage(stage.pre_stage)
		stage.update({"pre_stage": pre_stage})
	#save
	request = stage.stage.request
	response = stage.stage.response
	save = {}
	if "save" in request:
		save.update(request.save)
		del request.save
	if "save" in response:
		save.update(response.save)
		del response.save

	stage.update({"save": save})
	return stage
