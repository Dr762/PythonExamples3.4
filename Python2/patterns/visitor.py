# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="alex"
__date__ ="$May 14, 2015 1:59:51 AM$"


class Vlist(list):
    def accept(self,visitor):
        visitor.visit_list(self)


class Vdict(dict):
    def accept(self,visitor):
        visitor.visit_dict(self)


class Printer(object):
    def visit_list(self,ob):
        print 'list content:'
        print str(ob)
    
    def visit_dict(self,ob):
        print 'dict keys: %s' % ','.join(ob.keys())


a_list = Vlist([1, 2, 5])
print a_list.accept(Printer())

a_dict = Vdict({'one': 1, 'two': 2, 'three': 3})
print a_dict.accept(Printer())
