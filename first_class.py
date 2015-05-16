class MyClass(object):
	#clasa mosteneste object; astfel am metodele magic; self este obiectul instantiat(tis)
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def my_method(self):
		print self.a , self.b

#python are mostenire multipla
class MyClass1(object):
	def __init__(self,e):
		self.e = e

	def my_method(self):
		print "My method MyClass1"

class MyClassExtended(MyClass,MyClass1):
	def __init__(self,a,b,c):
		super(MyClassExtended, self ).__init__(a,b)
		self.c = c
	
	#python - nu se poate face overloading
	

