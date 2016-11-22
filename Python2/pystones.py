from test import pystone


def seconds_to_pystones(seconds):
    benchtime, pystones = pystone.pystones()
    return (pystones * seconds) / 1000


print pystone.pystones()
benchtime, pystones = pystone.pystones()
print benchtime, pystones
print seconds_to_pystones(3)
