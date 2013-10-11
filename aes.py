from Crypto.Cipher import AES
from hexutils import *
import requests

def dup_blocks(enc):
    if len(enc)%16 != 0: return 0
    duplicates = 0
    blocks = set()
    for block in range(0,len(enc),16):
        if block in blocks:
            duplicates += 1
        else:
            blocks.add(block)
    return duplicates

def _test7():
    print "## Program 7 ##"
    url = "https://gist.github.com/tqbf/3132853/raw/c02ff8a08ccf872f4cd278396379f4bb1ef337d8/gistfile1.txt"
    r = requests.get(url)
    enc = btos(r.content)
    key = "YELLOW SUBMARINE"
    cipher = AES.new(key, AES.MODE_ECB)
    plain = cipher.decrypt(enc)
    print "AES'd: {}".format(stoh(enc)[:80])
    print "Key:   {}".format(key)
    print "Plain: {}".format(plain[:80])

def _test8():
    print "## Program 8 ##"
    url = "https://gist.github.com/tqbf/3132928/raw/6f74d4131d02dee3dd0766bd99a6b46c965491cc/gistfile1.txt"
    r = requests.get(url)
    lines = r.content.split("\n")
    best_line = ""
    best_score = 1e10
    for line in lines:
        line = htos(line)
        score = dup_blocks(line)
        if score < best_score:
            best_line = line
            best_score = score
    print "ECB'd: {}".format(stoh(best_line))
