import os
import processing


a=[]
q = processing.Queue()

def some_work():
    a.append(2)
    child_pid = os.fork()
    if child_pid ==0:
        a.append(3)
        print "Child process"
        print "child process pid %d " % os.getpid()
        print str(a)
    else:
        a.append(4)
        print "Parent process"
        print "child pid %d" % child_pid
        print "parent pid %s" % os.getpid()
        print str(a)


some_work()

