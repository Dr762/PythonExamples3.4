import urllib.parse
import pprint
import json



def get_spot_rate(currency):
    form = {"currency": "GBP"}
    scheme_netloc_path = "https://api.coinbase.com/v1/prices/spot_rate"
    query = urllib.parse.urlencode(form)
    with urllib.request.urlopen(scheme_netloc_path + "?" + query) as document:
        pprint.pprint(document.info().items())
        spot_rate = json.loads(document.read().decode("utf-8"))
        print(spot_rate)
    return spot_rate


rates = [get_spot_rate("USD"), get_spot_rate("GBP"), get_spot_rate("EUR")]

with open("rate.json", "w") as save:
    json.dump(rates, save)
