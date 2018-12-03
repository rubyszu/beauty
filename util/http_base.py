#  -*- coding: utf-8 -*-

# 构造API域名和分支
def httpBase(cli_args):
	env = cli_args["env"]
	branch = cli_args["branch"]
	product = cli_args["product"]

	http_base = {
		"branch":branch,
		"product": product
	}
	if env == "development":
		http_base.update({"host":"https://api.ones.team"})
		
	elif env == "production":
		http_base.update({"host":"https://api.ones.ai"})

	return http_base



