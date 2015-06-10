# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from decimal import Decimal
import zipfile
import zlib
import http.client
import contextlib
import ftplib
import sys
import urllib.request
import urllib.parse
import json
import pprint
from collections import defaultdict
import glob
from PIL import Image
import PIL.ExifTags
import os
import hashlib
import hmac
import string
from math import radians, sin,cos,sqrt,asin
from bs4 import BeautifulSoup
from types import SimpleNamespace
__author__ = "alex"
__date__ = "$May 15, 2015 7:31:22 PM$"

if __name__ == "__main__":
  
  #ex1 - create file and read from it
#  text = """We are the people """
#  
#  with open("message.txt","w") as target:
#      target.write(text)
#      
#  with open("message.txt","r") as source:
#      text = source.read()
#  
#  print (text)      
  
  #ex2 - read a word corpus
#  count =0
#  corpus_file = "/usr/share/dict/words"
#  with open (corpus_file) as corpus:
#      for line in corpus:
#          word = line.strip()
#          if len(word) == 10:
#              print (word)
#              count +=1
#  print (count)   
  
#  #ex3 - read a zipfile
#  with zipfile.ZipFile("docs.zip","r") as archive:
#      archive.printdir()
#      first = archive.infolist()[0] ##info about each member
#      with archive.open(first) as member:
#          text = member.read()
#          print(text)
      
    #ex4 - brute-force search
#  corpus_file = "/usr/share/dict/words"
#  with zipfile.ZipFile("docs.zip","r") as archive:
#   first = archive.infolist()[0] ##info about each member
#   with open (corpus_file) as corpus:
#       for line in corpus:
#           word = line.strip().encode("ASCII")
#           try:
#               with archive.open(first,'r',pwd=word) as member:
#                   text = member.read()
#               print ("Password",word)
#               print (text)
#               break
#           except (RuntimeError,zlib.error,zipfile.BadZipFile):
#               pass
           
    #ex5 - http client which gets two pictures and changing request headers
    
#    path_list = ["/wikipedia/commons/7/72/IPhone_Internals.jpg",
#                     "/wikipedia/en/c/c1/1drachmi_1973.jpg"]
#    host = "upload.wikimedia.org"                 
#    with contextlib.closing(http.client.HTTPConnection( host ))   as connection:
#        for path in path_list:
#            connection.request("GET",path,headers = {
#            'User-Agent': 'Mozilla/5.0(iPhone;CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53',})
#            response = connection.getresponse()
#            print("Status:",response.status)
#            print("Headers:",response.getheaders())
#            _, _, filename = path.rpartition("/") #locate right-most in path
#            print("Writing:",filename)
#            with open(filename,"wb") as image:
#                image.write( response.read())


    #ex6 -ftp (coonect to the server)
#    host = "ftp.ibiblio.org"
#    root = "/pub/docs/books/gutenberg/"
    
#    def directory_list(path):
#        with ftplib.FTP(host, user="anonymous") as connection:
#            print ("Welcome",connection.getwelcome())
#            for name, details in connection.mlsd(path):
#                print(name,details['type'],details.get('size'))
#                
#                
#    directory_list(root)            
#    

    #ex7 - ftp download(#host and root from ex6) -doesn\twork properly/ need a check with another FTP
#    def get(fullname,output=sys.stdout):
#        download = 0
#        expected = 0
#        dots = 0
#        def line_save(aLine):  ##callback 
#            download,expected,dots
#            file = output
#            print (aLine,file)
#            if output != sys.stdout:
#                download +=len(aLine)
#                show = (20*dowload)//expected #Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed.
#                if show > dots:
#                    end=""
#                    file=sys.stdout
#                    print ("-",end,file  )
#                    sys.stdout.flush()
#                    dots = show
#        with ftplib.FTP(host,user="anonymous") as connection:
#              print ("Welcome",connection.getwelcome())
#              expected  = connection.size(fullname)
#              print ("Getting",fullname,"to",output,"size",expected)
#              connection.retrlines("RETR {0}".format(fullname),line_save)
#        if output != sys.stdout:
#            print() # End the "dots"
#            
#   #  get(root+"README")             
#    with open("GUTINDEX.ALL","w",encoding="UTF-8") as output:
#        get(root+"GUTINDEX.ALL",output)
#   
    #ex8 - urllib base
    
#    url_list= ["http://upload.wikimedia.org/wikipedia/commons/7/72/IPhone_Internals.jpg",
#                    "http://upload.wikimedia.org//wikipedia/en/2/26/Common_face_of_one_euro_coin.jpg"]
#    
#    for url in url_list:
#        with urllib.request.urlopen(url) as response:
#            print ("Status:",response.status)
#            _, _, filename = response.geturl().rpartition("/")
#            print ("Writing:",filename)
#            with open(filename,"wb") as image:
#                image.write(response.read())



    #ex9 - urllib for ftp
#    readme = "ftp://ftp.ibiblio.org/pub/docs/books/gutenberg/README"
#    with urllib.request.urlopen(readme) as response:
#        sys.stdout.write( response.read().decode("ascii"))

#    ex10 - parse get data via REST 
#    query_currencies = "https://api.coinbase.com/v1/currencies/"
#    with urllib.request.urlopen(query_currencies) as document:
#        print(document.info().items())
#        currencies=json.loads(document.read().decode("utf-8"))
#        for c in currencies:
#            print (c)
        
        
    #ex11 - get currency by code (parse json here) + encoding for URL +save data to local json file
#    def get_spot_rate(currency):
#        form = {"currency":"GBP"}
#        scheme_netloc_path = "https://api.coinbase.com/v1/prices/spot_rate"
#        query = urllib.parse.urlencode(form)
#        with urllib.request.urlopen(scheme_netloc_path+"?"+query ) as document:
#             pprint.pprint(document.info().items())
#             spot_rate =json.loads(document.read().decode("utf-8"))
#             print (spot_rate)
#        return spot_rate
#    
#    rates = [get_spot_rate("USD"),get_spot_rate("GBP"),get_spot_rate("EUR")]
#    
#    with open("rate.json","w") as save:
#        json.dump(rates,save)
#             
   #ex12  - tuple
   
#   a,b = "FOO","BAR"
#   print (a,b)
#   key=lambda x:x[1]
#   print ((key)((a,b)))

   #ex13 - currency conversion ()
#    query_exchange_rates = "https://api.coinbase.com/v1/currencies/exchange_rates"
#    with urllib.request.urlopen(query_exchange_rates) as document:
#        pprint.pprint(document.info().items())
#        exchange_rates=json.loads(document.read().decode("utf-8"))
#    rates = defaultdict(list)
#    for conversion,rate in exchange_rates.items():
#       source,_,target = conversion.upper().partition("_TO_")
#       rates[source].append((target,float(rate)))
#       for c in 'USD','GBP','EUR':
#         print (c,rates[c])
  
   #ex14 - images(used images from first examples,requires pillow lib)
#   pix = Image.open("1drachmi_1973.jpg")
#   print (pix)
#   pix.save("test.tiff")
#   print (pix.info.keys())
#   pix = Image.open("Common_face_of_one_euro_coin.jpg")
#   exif = pix._getexif()
#   print(exif.keys())
#   
#   for k,v in pix._getexif().items():
#       print(PIL.ExifTags.TAGS[k],v)
#       
       
   #ex15 - resizing images and creating thumb copy
#   for filename in glob.glob("*.jpg"):
#       name,ext = os.path.splitext(filename)
#       if name.endswith("_thumb"):
#           continue
#       img = Image.open(filename)
#       thumb = img.copy()
#       w,h = img.size
#       largest= max(w,h)
#       w_n,h_n = w*128//largest, h*128//largest
#       print ("Resize",filename,"from",w,h,"to",w_n,h_n)
#       thumb.thumbnail((w_n,h_n),PIL.Image.ANTIALIAS) #resample PIL.Image.ANTIALIAS
#       thumb.save(name+"_thumb"+ext)
# 
   
   #ex16 - cropping images
#   pix = Image.open("DSC_0811.JPG")
#   print (pix.size)
#   w,h = pix.size
#   pix.crop(box=(w//3,0,2*2//3,h//3)).show()
#   pix.crop(box=(w//3,h//3,2*2//3,h//3)).show()
#   
# 
  #ex17 hashing
#  md5 = hashlib.new("md5")
#  with open ("DSC_0811.JPG","rb") as some_file:
#      md5.update(some_file.read())
#  print (md5.hexdigest())

  #ex18 adding key to hashing
#  with open ("DSC_0811.JPG","rb") as some_file:
#      keyed = hmac.new( b"Bibizyan Govnokoder",some_file.read() )
#  print (keyed.hexdigest())    
#  


  #ex19 - geocoding
#  form = {
#  "address":"24 Kutuzovsky Prospeky,Moscow,121151",
#  "sensor":"false",
#  }
#  query = urllib.parse.urlencode(form,safe=",") ###safe= "," - replace % in res
#  scheme_netloc_path = "http://maps.googleapis.com/maps/api/geocode/json"
#  print (scheme_netloc_path+"?"+query)
#  
#  with urllib.request.urlopen(scheme_netloc_path+"?"+query) as geocode:
#      print(geocode.info())
#      response= json.loads(geocode.read().decode("UTF-8"))
      
#  print (response)  
  
  #ex20 - reverse geocode
#  form = {
#  "latlng":"36.844305,-76.29112",
#  "sensor":"false",
#  }
#  query = urllib.parse.urlencode(form,safe=",") ###safe= "," - replace % in res
#  scheme_netloc_path = "http://maps.googleapis.com/maps/api/geocode/json"
#  print (scheme_netloc_path+"?"+query)
#  
#  with urllib.request.urlopen(scheme_netloc_path+"?"+query) as geocode:
#      print(geocode.info())
#      response= json.loads(geocode.read().decode("UTF-8"))
#      
#  print (response)  
#  for alt in response['results']:
#      print (alt['types'],alt['formatted_address'])

  #ex21 - calc distance for two points and geoCode it + maidenhead grid coding +geoRef + NAC
  
  MI = 3959
  NM = 3440
  KM = 6371

  def harversine(point1,point2, R=KM):
      lat_1,lon_1 = point1
      lat_2,lon_2 = point2
      
      delta_lat = radians(lat_2-lat_1)
      delta_lon = radians(lon_2-lon_1)
      lat_1 = radians(lat_1)
      lat_2 = radians(lat_2)
      
      a = sin(delta_lat/2)**2 + cos(lat_1)*cos(lat_2)*sin(delta_lon/2)**2
      c = 2*asin(sqrt(a))
      
      return R*c
  
  def geocode (address):
      
     form = {
      "address":"",
      "sensor":"false",
      }
     form["address"]=address
     query = urllib.parse.urlencode(form,safe=",")
     scheme_netloc_path = "http://maps.googleapis.com/maps/api/geocode/json"
     print (scheme_netloc_path+"?"+query)
  
     with urllib.request.urlopen(scheme_netloc_path+"?"+query) as geocode:
         response= json.loads(geocode.read().decode("UTF-8"))
      
     loc_dict = [r['geometry']['location'] for r in response['results']]
     loc_pairs = [(l['lat'],l['lng']) for l in loc_dict] 
      
     return loc_pairs
  
  
  base = geocode("24 Kutuzovsky Prospekt,Moscow,121151")[0] #pick first res
  old_base = geocode("35 Sverdlov Street,Podolsk,142114")[0]
  reserve_base = geocode ("41 Miklukho-Maklaya ,Moscow, 117342")[0]
  
  
  def maidenhead(lat,lon):
      def let_num(v):  ##creates letter_num pair
          l,n = divmod(int(v),10)
          return string.ascii_uppercase[l],string.digits[n]
      f_lat = lat+90
      f_lon = (lon+180)/2
      y0, y1 = let_num(f_lat)
      x0, x1 = let_num(f_lon)
      f_lat = 240*(f_lat-int(f_lat))
      f_lon = 240*(f_lon-int(f_lon))
      y2,y3 = let_num(f_lat)
      x2,x3 = let_num(f_lon)
      f_lat = 240*(f_lat-int(f_lat))
      f_lon = 240*(f_lon-int(f_lon))
      y4,y5 = let_num(f_lat)
      x4,x5 = let_num(f_lon)
      return "".join([x0,y0,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5])
      
  
  def decode_maid(grid):
      lon = grid[0::2]
      lat = grid[1::2]
      assert len(lon)==len(lat)
      decode = [string.ascii_uppercase,string.digits,string.ascii_uppercase,string.digits,string.ascii_uppercase,string.digits]
      lons = [lookup.find(char.upper()) for char,lookup in zip(lon,decode)]
      lats = [lookup.find(char.upper())for char,lookup in zip(lat,decode)]
      weights = [10.0,1.0,1/24,1/240,1/240/24,1/240/240]
      lon = sum(w*d for w,d in zip(lons,weights))
      lat = sum (w*d for w,d in zip(lats,weights))
      return  lat - 90,2*lon-180
  
  
  georef_uppercase = string.ascii_uppercase.replace("O","").replace("I","")
  def georef (lat,lon):
      f_lat,f_lon = lat+90,lon+180
      lat_0,lat_1 = divmod (int(f_lat),15)
      lon_0,lon_1 = divmod (int(f_lon),15)
      lat_m,lon_m = 6000*(f_lat-int(f_lat)),6000*(f_lon-int(f_lon))
      return georef_uppercase[lat_0],georef_uppercase[lon_0],georef_uppercase[lat_1],georef_uppercase[lon_1],int(lat_m),int(lat_m)
   
  nac_uppercase = "0123456789BCDFGHJKLMNPQRSTVWXZ"
  def nac(lat,lon):
      f_lon=(lon+180)/360
      x0 = int (f_lon*30)
      x1 = int ((f_lon*30-x0)*30)
      x2 = int (((f_lon*30-x0)*30-x1)*30)
      x3 = int(0.5+(((f_lon*30-x0)*30-x1)*30-x2)*30)
      
      f_lat = (lat+90)/180
      y0 = int (f_lat*30)
      y1 = int ((f_lat*30-y0)*30)
      y2 = int(((f_lat*30-y0)*30-y1)*30)
      y3 = int(0.5+(((f_lat*30-y0)*30-y1)*30-y2)*30)
      return "".join([nac_uppercase[x0],nac_uppercase[x1],nac_uppercase[x2],nac_uppercase[3]," ",nac_uppercase[y0],nac_uppercase[y1],nac_uppercase[y2],nac_uppercase[y3],])
      
  def nac_decode(grid):
      X,Y = grid[:4],grid[5:]
      x = [nac_uppercase.find(c) for c in X]
      y = [nac_uppercase.find(c) for c in Y]
      lon = (x[0]/30+x[1]/30**2+x[2]/30**3+x[3]/30**4)*360-180
      lat =  (y[0]/30+y[1]/30**2+y[2]/30**3+y[3]/30**4)*180-90
      return lat,lon
   
  print ("Base",base)
  print ("Old Base",old_base)
  print ("Reserve Base",reserve_base)
  print ("Distance to the old base",harversine(base,old_base))
  print ("Distance to  reserve base",harversine(base,reserve_base))
  maiden =maidenhead(base[0],base[1])
  print ("Encode base to maiden",maiden)
  gref = georef(base[0],base[1])
  print("Encode base to georef",gref)
  n = nac(base[0],base[1])
  print ("Encode base to NAC",n)
  print ("Decode base from maidenhead",decode_maid(maiden))
  print ("Decode base from NAC",nac_decode(n))


 #ex22 -restraunt_finder app (see module RestrauntFinder)

