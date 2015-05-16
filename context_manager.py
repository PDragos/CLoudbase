#fd = open('myfile.txt','w')

#with open('myfile.txt','w') as fd:
#	fd.write('test')

#cum ne facem noi context manager
import contextlib

@contextlib.contextmanager
def myopen(*args,**kwargs):
	fd = None

	try:
		fd = open(*args,**kwargs)
		yield fd
	except Exception as exc:
		print "Got exception %s" % exc
	finally:
		if fd:
			fd.close()


with myopen('myfile.txt','w') as fd:
	fd.write('test')
