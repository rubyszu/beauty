from jsonschema import validate

# A sample schema, like what we'd get from json.load()
schema = {
	"type" : "object",
	"properties" : {
	"price" : {"type" : "number"},
	"name" : {"type" : "string"},
	},
	'required': ['price']
}

# If no exception is raised by validate(), the instance is valid.
validate({"name" : "Eggs", "priceeeeeeqw" : 11}, schema)