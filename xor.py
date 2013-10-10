from nltk.corpus import brown
from hexutils import *

char_counts = [1 for i in range(256)]
for char in brown.raw():
    char_counts[ord(char)] += 1
total = float(sum(char_counts))

def xor(plain, key):
    return ''.join(chr(ord(plain[i])^ord(key[i%len(key)])) for i in range(len(plain)))

def fscore(enc, key):
    length = float(len(enc))
    summation = 0
    text_counts = [0 for i in range(256)]
    for letter in enc:
        text_counts[ord(letter)^ord(key)] += 1
    for c in range(256):
        summation += ((text_counts[c]/length) / (char_counts[c]/total)) ** 2
    return summation

def crack(enc, key_length=1):
    if key_length > 1: return '\x04'
    guesses = [0 for i in range(256)]
    for key in range(256):
        guesses[key] = fscore(enc, chr(key))
    best = guesses.index(min(guesses))
    return chr(best)

if __name__ == "__main__":
    # Program 2 Tests
    print "## Program 2 ##"
    plain = htos("1c0111001f010100061a024b53535009181c")
    key = htos("686974207468652062756c6c277320657965")
    enc = xor(plain, key)
    print "Plain:     {}".format(stoh(plain))
    print "Key:       {}".format(stoh(key))
    print "Encrypted: {}".format(stoh(enc))
    # Program 3 Tests
    print "## Program 3 ##"
    enc = htos("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    key = crack(enc)
    plain = xor(enc, key)
    print "Encrypted: {}".format(stoh(enc))
    print "Key:       {}".format(stoh(key))
    print "Plain:     {}".format(plain)
    # Program 4 Tests
    print "## Program 4 ##"
    import requests
    url = raw_input("URL: ")
    r = requests.get(url)
    lines = r.content.split("\n")
    best = ['','',total]
    for line in lines:
        if not line: continue
        line = htos(line)
        key = crack(line)
        score = fscore(line, key)
        if score < best[2]:
            best[0] = line
            best[1] = key
            best[2] = score
    print "XOR'd: {}".format(stoh(best[0]))
    print "Plain: {}".format(xor(best[0],best[1]))
