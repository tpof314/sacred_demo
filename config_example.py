from sacred import Experiment
ex = Experiment('config_example')

@ex.config
def my_config():
	a = 10

	foo = {
		"a_squared": a**2,
		"bar": "my_string %d" % a
	}

	if a > 8:
		e = a / 2

@ex.main
def run():
	pass