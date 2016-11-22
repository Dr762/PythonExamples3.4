#!/usr/bin/python

x=0b1101
g=0b1011
global c
stat = []
for i in range(8):
  stat.append({"num_err":0,"cor_err":0,"num_fact":0}) #num_fact - really found errors
synd_list = [0b001,0b010,0b100,0b011,0b110,0b111,0b101 ]
def calc_index(err):
#multiplicity of error
  mult=bin(err)
  num=0
  for pos in mult:
     if pos=='1':
      num+=1
  return num    
def div_poly(c_err,g):
  shift=len(bin(c_err)) - len(bin(g)) 
  while shift >= 0:
    z = g << shift
#    print "c_err: %s, z: %s	, res: %s" % (bin(c_err), bin(z), bin(c_err ^ z))
    c_err = c_err ^ z
    shift=len(bin(c_err)) - len(bin(g)) 

  return c_err
   
def decode(err) :
#decoding 
  c_err= c ^ err
  synd=div_poly(c_err,g)
  #print " err: %s(%s), c_err: %s, g: %s , synd : %s" % (bin(err),err, bin(c_err), bin(g), bin(synd))
  err1 = 0
  if synd > 0 :
    err1=(1 << synd_list.index(synd))  
 # print "err1 : " , bin(err1)
#fixing
  c_err_cor=c_err^err1  
#calc stat  
  i_stat = calc_index(err)
  el_stat= stat[i_stat] #pair of all and corrected errors
  
  el_stat["num_err"]=el_stat["num_err"]+1 #found
  if synd > 0 :
    el_stat["num_fact"] +=1
  
#  print "c err : %s,c_err_cor : %s ? %s" %( bin(c_err), bin(c_err_cor), c_err_cor == c )
  if c_err_cor == c and synd > 0 : el_stat["cor_err"]+=1
  stat[i_stat]=el_stat

if __name__=="__main__":
#coding
  x1=x << 3
#  o=x1 % g
  o = div_poly(x1,g)
  c=x1 | o
  print("given vector 1101")
  print("polynom g  1011")
  print("coded vector %s (%s)" % (bin(c), c))
  for i in range(128):
    decode(i)
    
  for i in range(len(stat)):
    print "i=%s errors found %s of %s errors corrected %s Ck =%s" % (i,stat[i]["num_fact"],stat[i]["num_err"],stat[i]["cor_err"], 
           ( lambda x = stat[i]["num_err"] : 0.00 if x== 0 else stat[i]["cor_err"]/float(stat[i]["num_err"])  )() )
