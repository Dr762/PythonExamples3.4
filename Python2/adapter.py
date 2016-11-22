# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from os.path import split,splitext
__author__ = "alex"
__date__ = "$May 14, 2015 1:36:29 AM$"


class DublinCoreAdapter(object):
    def __init__(self,filename):
        self._filename = filename
        
    def title(self):
        return splitext(split(self._filename)[-1])[0]
    
    def creator(self):
        return 'Unknown' 
    
    def languages(self):
        return ('en',)


class DublinCoreInfo(object):
    def summary(self,dc_ob):
        print 'Title: %s' % dc_ob.title()
        print 'Creator: %s' % dc_ob.creator()
        print 'Languages: %s' % ', '.join(dc_ob.languages())
        

adapted = DublinCoreAdapter('cmd_profile.py')
info = DublinCoreInfo()
print info.summary(adapted)