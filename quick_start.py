from sacred import Experiment

ex = Experiment('quick_start')

@ex.config
def my_config():
	a = 10
	b = 'test'

@ex.automain
def my_main(a, b):
	print("a =", a)
	print("b =", b)