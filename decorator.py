import functools

def my_decorator(functie):
	#@functools.wraps(functie)
	def wrapper(*args,**kwargs):
		print 'inainte de functie %s' %functie.func_name
		functie(*args,**kwargs)
		print 'dupa functie %s' % functie.func_name

	return wrapper

def f():
	print 'Hello word fin f'

@my_decorator #decorare automata
def f1(a):
	print a
	raise Exception("My_message")
#f1 = my_decorator(f1)