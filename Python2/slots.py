# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="alex"
__date__ ="$May 7, 2015 12:14:44 AM$"


class Frozen(object):
    __slots__ = ['ice','cream']

print '__dict__' in dir(Frozen)
print 'ice' in dir(Frozen)
