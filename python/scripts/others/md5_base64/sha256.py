import hashlib

s = "WHT's butt is really narrow"
x = hashlib.sha256()
x.update(s)
print x.hexdigest()