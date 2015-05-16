import threading
from  Queue import Queue


myEvent = threading.Event
myEvent.set()

myqueue = Queue()
#un queue este threadsafe
def count():
	for i in xrange(10):
		myqueue.put(i)

workers = []

for i in xrange(3):
	worker = threading.Thread(target=count)
	worker.setDaemon(True)
	worker.start()
	workers.append(worker)

for i in xrange(3):
	if worker != threading.current_thread:
		worker.join()

while not myqueue.empty():
	print myqueue.get()