# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "alex"
__date__ = "$May 7, 2015 12:02:39 AM$"


class MyClass(object):
    attribute = "attribute"
    def __init__(self):
        self._my_secret_thing = 1

    def _i_get(self):
        return self._my_secret_thing

    def _i_set(self,value):
        self._my_secret_thing = value

    def _i_delete(self):
        print 'hah!'

    my_thing = property(_i_get,_i_set,_i_delete,'the thing')


instance_of = MyClass()
print instance_of.my_thing
instance_of.my_thing = 10
print instance_of.my_thing
del instance_of.my_thing

print instance_of.attribute
instance_of.attribute = 'my value'
print instance_of.attribute
instance_of.__dict__ = {}
instance_of.new_att = 1
print instance_of.__dict__

print MyClass.__doc__
instance = MyClass()
print instance.__doc__

help(instance_of)
