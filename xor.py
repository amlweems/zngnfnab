from hexutils import *

def xor(plain, key):
    return ''.join(chr(ord(plain[i])^ord(key[i%len(key)])) for i in range(len(plain)))

if __name__ == "__main__":
    # Program 2 Tests
    print "## Program 2 ##"
    plain = htos("1c0111001f010100061a024b53535009181c")
    key = htos("686974207468652062756c6c277320657965")
    enc = xor(plain, key)
    print "Plain:     {}".format(stoh(plain))
    print "Key:       {}".format(stoh(key))
    print "Encrypted: {}".format(stoh(enc))