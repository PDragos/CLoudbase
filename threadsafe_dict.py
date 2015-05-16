import threading

def apply_lock(func):
	def wrapper(inst,*arg,**kwargs):
		with inst._lock:
			return func(inst,*args,**kwargs)
	return wrapper


class threadsafeDict(dict):
	_lock = threading.Lock()

	@apply_lock
	def __getitem__(self, key):
		#with self._lock: #context manager , aplic lock
		return super(threadsafeDict,self).__getitem__(key)

	@apply_lock
	def __setitem__(self,key,value):
		#with self._lock: #context manager , aplic lock
		return super(threadsafeDict,self).__setitem__(key,value)


#PEP OP -> reguli de a se scrie cod
#citesc din fisier
#with open('nume_fisier','w') as f:
#	f.write('tes')

mydict = threadsafeDict()
mydict['test'] = 10
print mydict['test'] 