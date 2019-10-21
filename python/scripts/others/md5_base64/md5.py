'''
import md5
src = 'this is a md5 test.'
m1 = md5.new()
m1.update(src)
print m1.hexdigest()
'''


import hashlib

s = 'addr="192.168.10.0"'

m2 = hashlib.md5()
m2.update(s)
print m2.hexdigest()
