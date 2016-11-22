from Queue import Queue
from threading import Thread
from test import pystone
import time
from cmd_profile import *
import subprocess
import logging
import os
import sys
__author__ = "alex"
__date__ = "$May 14, 2015 12:22:46 AM$"


# run python indexer.py zc.buildout-2.3.1-py.2.7.egg 1
# file indexer 
dirname = os.path.realpath(os.path.dirname(__file__))
CONVERTER = os.path.join(dirname,'converter.py')
q = Queue()
def index_file(filename):
    logging.info('indexing %s' % filename)
    f = open(filename)
    try:
        content = f.read()
        subprocess.call([CONVERTER])
    finally:
        f.close()
     
def worker():
        while True:
            index_file(q.get())
            q.task_done()
             
def index_files(files,num_workers):
         for i in range(num_workers):
             t =Threa(target=worker)
             t.setDaemon(True)
             t.start()
         for file in files:
             q.put(file)
         q.join()
     
def get_text_files(dirname):
         for root,dirs,files in os.walk(dirname):
             for file in files:
                 if os.path.splittext(file)[-1]!= '.txt':
                     continue
                 yield os.path.join(root,file)
     
def process(dirname,numthreads):
         dirname = os.path.realpath(dirname)
         if numthreads>1:
             index_files(get_text_files(dirname),numthreads)
         else:
             for f in get_text_files(dirname):
                 index_file(f)
                 

if __name__ == "__main__":
    print process(sys.argv[1],int(sys.argv[2]))
    