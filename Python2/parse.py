#!/usr/bin/python
import re


'''
Created on Apr 4, 2014

@author: abondar
'''

'''
List of features for device
'''
nexus = [u"5.0(3)U3(1)","vrrp","bgp","interface-vlan","lacp","dhcp","lldp"]


'''
Reading config file
'''
def main () :
  f1 = open( "rsw1aa.txt", "r" )
  fe = []
  version = ""
  config = {}
  parsed_conf = []
  exp = re.compile("^(\W*)(\w+?) (.*)\r$")
  tag = ""
  for line in f1:
    m = exp.match(line)
    if m :
      shift = len(m.group(1))
      if shift == 0 :
        tag = m.group(2)
        if config.has_key(tag) :
            config[tag].append(m.group(3))
        else :
            config[tag] = [m.group(3)]
      else :
        if tag :
           config[tag].append("%s %s" % (m.group(2), m.group(3)))
    else :
      pass
  f1.close()
  print config.keys()
  print "version:" , config["version"][0]
  print "features:", config["feature"]
  if config["router"][0][:3] == "bgp" :
     print config["router"][0]
     for v in config["router"][1:] : print " "*2, v
  print "no:" , config["no"]

if __name__ == '__main__':
  main()





    
