# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "alex"
__date__ = "$May 13, 2015 7:54:48 PM$"

class context (object):
    
    def __enter__(self):
        print 'entering the zone'
        
    def __exit__(self,exception_type,exception_value,exception_trace):
        print 'leaving the zone'
        if exception_type is None:
            print 'with no error'
        else:
            print 'with an error (%s)' % exception_value




with context():
    print 'I am bug zone'
    raise TypeError('I am the bug')