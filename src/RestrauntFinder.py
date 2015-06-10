# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "alex"
__date__ = "$Jun 1, 2015 10:46:55 PM$"

from math import radians, sin,cos,sqrt,asin
from bs4 import BeautifulSoup
from types import SimpleNamespace
import urllib.request
import urllib.parse
import json

class Restraunt:
    def __init__(self,name,address,last_inspection,category):
        self.name= name
        self.address = address
        self.last_inspection = last_inspection
        self.category = category
        
        

scheme_host = "http://www.healthspace.com"
vdh_detail_translate = {
  'Phone Number:': 'phone_number',
  'Facility Type:': 'facility_type',
  '# of Priority Foundation Items on Last Inspection:': 'priority_foundation_items',
  '# of Priority Items on Last Inspection:': 'prioirty_items',
  '# of Core Items on Last Inspection:': 'core_items',
  '# of Critical Violations on Last Inspection:': 'critical_items',
  '# of Non-Critical Violations on Last Inspection:': 'non_critical_items'
  
  }
  
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
  
def get_food_list_by_name(): #get all restraunts
     path="/Clients/VDH/Norfolk/Norolk_Website.nsf/Food-List-ByName"
    
     form = {
        "OpenView": "",
        "RestrictToCategory":"faa4e68b1bbbb48f008d02bf09dd656f",
        "count":"400",
        "start":"1",
     }
     query=urllib.parse.urlencode(form)
     with urllib.request.urlopen(scheme_host+path+"?"+query) as data:
         soup = BeautifulSoup(data.read())
     return soup
 
def food_table_iter(soup):
     """Columns are 'Name', '' , 'Facility Location', 'Last Inspection',
     Plus an unnamed column with a RestrictToCategory key"""
     
     table = soup.html.body.table
     for row in table.find_all("tr"):
         columns = [td.text.strip() for td in row.find_all("td")]
         for td in row.find_all("td"):
             if td.a:
                 url = urllib.parse.urlparse(td.a["href"])
                 form = urllib.parse.parse_qs(url.query)
                 columns.append (form['RestrictToCategory'][0])
         yield columns
     
def food_row_iter(table_iter):
     heading = next(table_iter)
     for row in table_iter:
         yield Restraunt( name=row[0],address=row[2],last_inspection = row[3],category=row[4])
     
def geocode_detail(business):
     form = {
      "address": business.address + ", Norfolk, VA",
      "sensor":"false",
      }
     
     query = urllib.parse.urlencode(form,safe=",")
     scheme_netloc_path = "http://maps.googleapis.com/maps/api/geocode/json"
     with urllib.request.urlopen(scheme_netloc_path+"?"+query) as geocode:
         response= json.loads(geocode.read().decode("UTF-8"))   
     lat_lon = response['results'][0]['geometry']['location']
     business.latitude = lat_lon['lat']
     business.longitude=lat_lon['lng']
     return business
 
def get_food_facility_history(cat_key):
     url_detail = "/Clients/VDH/Norfolk/Norolk_Website.nsf/Food-FacilityHistory"
     form = {
        "OpenView": "",
        "RestrictToCategory":cat_key
      
     }
     query=urllib.parse.urlencode(form)
     with urllib.request.urlopen(scheme_host+url_detail+"?"+query) as data:
         soup = BeautifulSoup(data.read())
     return soup
 
 
def inspection_detail(business):
     soup = get_food_facility_history(business.category)
     business.name2 = soup.body.h2.text.strip()
     table = soup.body.table
     for row in table.find_all("tr"):
          column = list(row.find_all("td"))
          name = column[0].text.strip()
          value = column[1].text.strip()
          setattr(business,vdh_detail_translate[name],value)
     return business
 
 
def get_chicago_json():
     form = {
      "accessType": "DOWNLOAD",
      "$where": "inspection_date>2015-01-01",
      }
     
     query = urllib.parse.urlencode(form)
     scheme_netloc_path = "https://data.cityofgchicago.org/api/views/4ijn-s7e5/rows.json"
     with urllib.request.urlopen(scheme_netloc_path+"?"+query) as data:
         with open("chicago_data.json","w") as output:
             output.write(data.read())
             
def food_row_iter():#create object from json
    with open ("chicago_data.json",encoding="UTF-8") as data_file:
        inspections = json.load(data_file)
        headings = [item['fieldName'] for item in inspections["meta"]["view"]["columns"]]
        for row in inspections["data"]:
            data= SimpleNamespace(**dict(zip(headings,row)))
            yield data
            
def parse_details(business):
    business.latitude = float (business.latitude)
    business.longitude = float (business.longitude)
    if business.violations is None:
        business.details = []
    else:
        business.details = [v.strip for v in business.violations.split("|")]
    
    return business

def choice_iter_norfolk():
     n_base=SimpleNamespace(address = '333 Waterside Drive')
     geocode_detail(n_base)
     print (n_base)
     soup = get_food_list_by_name()
     for row in food_row_iter ():
         for row in food_table_iter(soup):
          geocode_detail( row )
          inspection_detail(row)
         row.distance = harversine ((row.latitude,row.longitude),(n_base.latitude,n_base.longitude))
         yield row    
   
def choice_iter_chicago():
     c_base=SimpleNamespace(address = '3420 W GRACE ST')
     geocode_detail(c_base)
     print(c_base)
     for row in food_row_iter():
         try:
             parse_details(row)
             row.distance = harversine((row.latitude,row.longitude),
             (c_base.latitude,c_base.longitude))
             yield row
         except TypeError:
             pass
         

 # main code of the app
soup = get_food_list_by_name()
raw_column = food_table_iter(soup)

for business in choice_iter_norfolk():
     print('name ',business.name,' address ', business.address,' lat ',  business.latitude,' lon ',business.longitude,
     ' phone ',business.phone_number,' type ',business.facility_type )
     
get_chicago_json()
for business in choice_iter_chicago():
     print('name ',business.dba_name,' address ', business.address,' lat ',  business.latitude,' lon ',business.longitude,
     ' phone ',business.phone_number,' type ',business.facility_type, ' results ', business.results )
     
