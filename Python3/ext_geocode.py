# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import urllib.request
import urllib.parse
import json
import string
from math import radians, sin, cos, sqrt, asin



MI = 3959
NM = 3440
KM = 6371


def harversine(point1, point2, R=KM):
    lat_1, lon_1 = point1
    lat_2, lon_2 = point2

    delta_lat = radians(lat_2 - lat_1)
    delta_lon = radians(lon_2 - lon_1)
    lat_1 = radians(lat_1)
    lat_2 = radians(lat_2)

    a = sin(delta_lat / 2) ** 2 + cos(lat_1) * cos(lat_2) * sin(delta_lon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return R * c


def geocode(address):
    form = {
        "address": "",
        "sensor": "false",
    }
    form["address"] = address
    query = urllib.parse.urlencode(form, safe=",")
    scheme_netloc_path = "http://maps.googleapis.com/maps/api/geocode/json"
    print(scheme_netloc_path + "?" + query)

    with urllib.request.urlopen(scheme_netloc_path + "?" + query) as geocode:
        response = json.loads(geocode.read().decode("UTF-8"))

    loc_dict = [r['geometry']['location'] for r in response['results']]
    loc_pairs = [(l['lat'], l['lng']) for l in loc_dict]

    return loc_pairs




def maidenhead(lat, lon):
    def let_num(v):  # creates letter_num pair
        l, n = divmod(int(v), 10)
        return string.ascii_uppercase[l], string.digits[n]

    f_lat = lat + 90
    f_lon = (lon + 180) / 2
    y0, y1 = let_num(f_lat)
    x0, x1 = let_num(f_lon)
    f_lat = 240 * (f_lat - int(f_lat))
    f_lon = 240 * (f_lon - int(f_lon))
    y2, y3 = let_num(f_lat)
    x2, x3 = let_num(f_lon)
    f_lat = 240 * (f_lat - int(f_lat))
    f_lon = 240 * (f_lon - int(f_lon))
    y4, y5 = let_num(f_lat)
    x4, x5 = let_num(f_lon)
    return "".join([x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5])


def decode_maid(grid):
    lon = grid[0::2]
    lat = grid[1::2]
    assert len(lon) == len(lat)
    decode = [string.ascii_uppercase, string.digits, string.ascii_uppercase, string.digits, string.ascii_uppercase,
                  string.digits]
    lons = [lookup.find(char.upper()) for char, lookup in zip(lon, decode)]
    lats = [lookup.find(char.upper()) for char, lookup in zip(lat, decode)]
    weights = [10.0, 1.0, 1 / 24, 1 / 240, 1 / 240 / 24, 1 / 240 / 240]
    lon = sum(w * d for w, d in zip(lons, weights))
    lat = sum(w * d for w, d in zip(lats, weights))
    return lat - 90, 2 * lon - 180


georef_uppercase = string.ascii_uppercase.replace("O", "").replace("I", "")

def georef(lat, lon):
    f_lat, f_lon = lat + 90, lon + 180
    lat_0, lat_1 = divmod(int(f_lat), 15)
    lon_0, lon_1 = divmod(int(f_lon), 15)
    lat_m, lon_m = 6000 * (f_lat - int(f_lat)), 6000 * (f_lon - int(f_lon))
    return georef_uppercase[lat_0], georef_uppercase[lon_0], georef_uppercase[lat_1], georef_uppercase[lon_1], int(
            lat_m), int(lat_m)


nac_uppercase = "0123456789BCDFGHJKLMNPQRSTVWXZ"

def nac(lat, lon):
    f_lon = (lon + 180) / 360
    x0 = int(f_lon * 30)
    x1 = int((f_lon * 30 - x0) * 30)
    x2 = int(((f_lon * 30 - x0) * 30 - x1) * 30)
    x3 = int(0.5 + (((f_lon * 30 - x0) * 30 - x1) * 30 - x2) * 30)

    f_lat = (lat + 90) / 180
    y0 = int(f_lat * 30)
    y1 = int((f_lat * 30 - y0) * 30)
    y2 = int(((f_lat * 30 - y0) * 30 - y1) * 30)
    y3 = int(0.5 + (((f_lat * 30 - y0) * 30 - y1) * 30 - y2) * 30)
    return "".join(
            [nac_uppercase[x0], nac_uppercase[x1], nac_uppercase[x2], nac_uppercase[3], " ", nac_uppercase[y0],
             nac_uppercase[y1], nac_uppercase[y2], nac_uppercase[y3], ])


def nac_decode(grid):
    X, Y = grid[:4], grid[5:]
    x = [nac_uppercase.find(c) for c in X]
    y = [nac_uppercase.find(c) for c in Y]
    lon = (x[0] / 30 + x[1] / 30 ** 2 + x[2] / 30 ** 3 + x[3] / 30 ** 4) * 360 - 180
    lat = (y[0] / 30 + y[1] / 30 ** 2 + y[2] / 30 ** 3 + y[3] / 30 ** 4) * 180 - 90
    return lat, lon

base = geocode("24 Kutuzovsky Prospekt,Moscow,121151")[0]  # pick first res
old_base = geocode("35 Sverdlov Street,Podolsk,142114")[0]
reserve_base = geocode("41 Miklukho-Maklaya ,Moscow, 117342")[0]

print("Base", base)
print("Old Base", old_base)
print("Reserve Base", reserve_base)
print("Distance to the old base", harversine(base, old_base))
print("Distance to  reserve base", harversine(base, reserve_base))
maiden = maidenhead(base[0], base[1])
print("Encode base to maiden", maiden)
gref = georef(base[0], base[1])
print("Encode base to georef", gref)
n = nac(base[0], base[1])
print("Encode base to NAC", n)
print("Decode base from maidenhead", decode_maid(maiden))
print("Decode base from NAC", nac_decode(n))
