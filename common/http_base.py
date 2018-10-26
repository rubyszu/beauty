# -*- coding: utf-8 -*-
from common import getCmdlineArgs

def httpBase():
	http_base = {
		"host":	"https://api.ones.ai",
		"branch": "v1"
	}
	env = getCmdlineArgs("env")
	if env == "development":
		branch = getCmdlineArgs("branch")
		http_base["host"] = "https://api.ones.team"
		http_base["branch"] = branch
		
	return http_base


if __name__ == '__main__':
	print httpBase()



