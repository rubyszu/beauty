import sys

class Base(object):
	def __init__(self):
		self.dependent_models = []

	def str2Class(self):
		new_arr = []
		if not len(self.dependent_models):
			return []
		for i in range(len(self.dependent_models)):
			new_arr.append(getattr(sys.modules[__name__], self.dependent_models[i]))
		return new_arr



	def for_compose(self):
		return 1

	def get_dependent_models(self):
		self.dependent_models = self.str2Class()
		if not len(self.dependent_models):
			return []

		all_dependent_models = [];

		for i in range(len(self.dependent_models)):
			dependent_model = self.dependent_models[i]()
			all_dependent_models.extend(dependent_model.get_dependent_models())

		all_dependent_models.extend(self.dependent_models)
		return all_dependent_models

class A(Base):
	pass

class B(Base):
	def __init__(self):
		# rely = ["A"]
		self.dependent_models = ["A"]

class C(Base):
	def __init__(self):
		self.dependent_models = ["A"]

class D(Base):
	def __init__(self):
		self.dependent_models = ["C"]

class E(Base):
	def __init__(self):
		self.dependent_models = ["B", "D"]

dependent_models = E().get_dependent_models()

d = {}

for i in range(len(dependent_models)):
	d.update({ dependent_models[i]().__class__.__name__:dependent_models[i]()})

values = [value for _,value in d.items()]
print values
print([ v.for_compose() for v in values])

