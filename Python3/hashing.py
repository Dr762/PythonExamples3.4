import hashlib
import hmac

# hashing
md5 = hashlib.new("md5")
with open("../LICENSE", "rb") as some_file:
    md5.update(some_file.read())
print(md5.hexdigest())

# adding key to hashing
with open("../LICENSE", "rb") as some_file:
    keyed = hmac.new(b"Bibizyan Govnokoder", some_file.read())
print(keyed.hexdigest())
