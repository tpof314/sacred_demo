from sacred import Experiment
ex = Experiment('config_func')

@ex.config
def my_config():
	a = 10
	b = 'test'

@ex.capture
def print_a_and_b(a, b):
	print("a =", a)
	print("b =", b)

@ex.automain
def my_main():
	print_a_and_b()
	print_a_and_b(3)
	print_a_and_b(3, 'foo')
	print_a_and_b(b='foo')