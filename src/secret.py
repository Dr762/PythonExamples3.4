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
  with open ("DSC_0811.JPG","rb") as some_file:
      keyed = hmac.new( b"Bibizyan Govnokoder",some_file.read() )
  print (keyed.hexdigest())    
  