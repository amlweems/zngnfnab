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

if __name__ == "__main__":
    print "## Program 1 ##"
    hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    base_str = htob(hex_str)
    new_hex_str = btoh(base_str)
    print "Hex:          {}".format(hex_str)
    print "Base64:       {}".format(base_str)
    print "Hex'd Base64: {}".format(new_hex_str)
