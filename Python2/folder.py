# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "alex"
__date__ = "$May 13, 2015 7:55:58 PM$"


class Folder(list):
    def __init__(self,name):
        self.name = name
        
    def dir(self):
        print 'I am the %s folder' % self.name
        
        for element in self:
            print element

ff = folder ('shit')
ff.append('dog shit')
ff.append('bad energy')
print ff.dir()
