# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "alex"
__date__ = "$May 13, 2015 7:52:51 PM$"

class DistinctError(Exception):
    pass

class distinctdict(dict):
    def __setitem__(self,key,value):
        try:
            value_index =self.values().index(value) 
            #keys and values return lists and dict ins't changed 
            #between two calls. dict type doesn't guarantee ordering
            existing_key = self.keys()[value_index]
            if existing_key != key:
              raise DistinctError(("The value already exists for '%s' ") % str (self[existing_key]))
        except ValueError:
            pass
        
        super(distinctdict,self).__setitem__(key,value)


dd = distinctdict()
dd['key'] = ' value '
print dd
dd['other_key'] = ' value2 '
print dd
dd['other_key'] = ' value '
print dd
