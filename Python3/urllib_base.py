import urllib.request
import urllib.parse
import sys
import json

# urllib base

url_list = ["http://upload.wikimedia.org/wikipedia/commons/7/72/IPhone_Internals.jpg",
            "http://upload.wikimedia.org//wikipedia/en/2/26/Common_face_of_one_euro_coin.jpg"]

for url in url_list:
    with urllib.request.urlopen(url) as response:
        print("Status:", response.status)
        _, _, filename = response.geturl().rpartition("/")
        print("Writing:", filename)
        with open(filename, "wb") as image:
            image.write(response.read())

# urllib for ftp
readme = "ftp://ftp.ibiblio.org/pub/docs/books/gutenberg/README"
with urllib.request.urlopen(readme) as response:
    sys.stdout.write(response.read().decode("ascii"))

# parse get data via REST
query_currencies = "https://api.coinbase.com/v1/currencies/"
with urllib.request.urlopen(query_currencies) as document:
    print(document.info().items())
    currencies = json.loads(document.read().decode("utf-8"))
    for c in currencies:
        print(c)
