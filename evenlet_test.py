import eventlet

def count():
	for i in xrange(10):
		print i
#la event-uri se face mocking patching -> adica un modul se inlocuieste la runtime
# grija la imbinare de corutine cu thread-uri
worker = eventlet.spawn(count)
