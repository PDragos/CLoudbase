import multiprocessing


myqueue = multiprocessing.Queue()
#un queue este threadsafe
def count():
	for i in xrange(10):
		myqueue.put(i)

workers = []
#subprocese 
for i in xrange(3):
	worker = multiprocessing.Process(target=count)
	#worker.setDaemon(True)
	worker.start()
	workers.append(worker)

for worker in workers:
		worker.join()

while not myqueue.empty():
	print myqueue.get()