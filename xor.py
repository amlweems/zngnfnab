from hexutils import *

def xor(p, k):
    return ''.join(chr(ord(p[i])^ord(k[i])) for i in range(len(p)))

if __name__ == "__main__":
    plain = htos("1c0111001f010100061a024b53535009181c")
    key = htos("686974207468652062756c6c277320657965")
    enc = xor(plain, key)
    print stoh(plain)
    print stoh(key)
    print stoh(enc)
