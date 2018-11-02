# -*- coding: utf-8 -*-
from common import getCmdlineArgs

def httpBase():
	env = getCmdlineArgs("env")
	branch = getCmdlineArgs("branch")

	http_base = {
		"branch":branch
	}
	if env == "development":
		http_base.update({"host":"https://api.ones.team"})
		
	elif env == "production":
		http_base.update({"host":"https://api.ones.ai"})

	return http_base


if __name__ == '__main__':
	print httpBase()



