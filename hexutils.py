import binascii
import base64

def htos(s):
    return binascii.unhexlify(s)

def stoh(s):
    return binascii.hexlify(s)

def stob(s):
    return base64.b64encode(s)

def btos(s):
    return base64.b64decode(s)

def htob(s):
    return stob(htos(s))

def btoh(s):
    return stoh(btos(s))
