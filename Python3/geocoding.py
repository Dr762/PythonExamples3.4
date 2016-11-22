import urllib.parse
import json


# geocoding

def geocode(send_form):
    query = urllib.parse.urlencode(form, safe=",")  # safe= "," - replace % in res
    scheme_netloc_path = "http://maps.googleapis.com/maps/api/geocode/json"
    print(scheme_netloc_path + "?" + query)

    with urllib.request.urlopen(scheme_netloc_path + "?" + query) as geocode:
        print(geocode.info())
        response = json.loads(geocode.read().decode("UTF-8"))

    return response


form = {
    "address": "24 Kutuzovsky Prospeky,Moscow,121151",
    "sensor": "false",
}

resp = geocode(form)
print(resp)

# reverse geocode
form = {
    "latlng": "36.844305,-76.29112",
    "sensor": "false",
}
resp = geocode(form)
for alt in resp['results']:
    print(alt['types'], alt['formatted_address'])
