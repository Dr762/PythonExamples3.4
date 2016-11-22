# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "alex"
__date__ = "$May 14, 2015 1:29:43 AM$"


class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls.instance = orig.__new__(cls, *args, **kw)
        return cls.instance


class MyClass(Singleton):
    a = 1

one = MyClass()
two = MyClass()
print two.a
print one.a
