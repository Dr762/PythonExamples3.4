import processing
import Queue
from processing import Process

def work():
    print 'Process with id: %d' % os.getpid()



q = processing.Queue()
ps=[]
for i in range(4):
    p = Process(target=work)
    ps.append(p)
    p.start()

    print ps
    for p in ps:
        p.join()


print "We have %d CPUs"  % processing.cpuCount()
pool = processing.Pool()
for i in ('f1','f2','f3','f4','f5'):
         q.put(i)

while True:
    try:
        result = pool.apply_async(worker)
        print result.get(timeout=2)
    except Queue.Empty:
        break


def worker():
    file = q.get_nowait()
    return 'worked on' + file
