# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "alex"
__date__ = "$May 7, 2015 12:18:37 AM$"


class MyClass(object):
    def __new__(cls):
        print '__new__ called'
        return object.__new__(cls) # factory
    
    def  __init__(self):
        print '__init__ called'
        self.a =1


class NoConstr(MyClass):
    pass


class Other(MyClass):
    def __init__(self):
        print 'Other __init__ called'
        super(Other,self).__init__()
        self.b = 2


class MyClass1(object):
    __metaclass__=equip
    
    def alright(self):
        """the ok method """
        return 'okay'


inst = MyClass()
print inst
inst1 = NoConstr()
print inst1
inst2 = Other()
print inst2