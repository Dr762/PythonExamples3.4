import urllib.request
import pprint
import json
from collections import defaultdict

# currency conversion ()
query_exchange_rates = "https://api.coinbase.com/v1/currencies/exchange_rates"
with urllib.request.urlopen(query_exchange_rates) as document:
    pprint.pprint(document.info().items())
    exchange_rates = json.loads(document.read().decode("utf-8"))
    rates = defaultdict(list)
    for conversion, rate in exchange_rates.items():
        source, _, target = conversion.upper().partition("_TO_")
        rates[source].append((target, float(rate)))
        for c in 'USD', 'GBP', 'EUR':
            print(c, rates[c])
