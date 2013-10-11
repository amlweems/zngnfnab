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
    url = "https://gist.github.com/tqbf/3132713/raw/40da378d42026a0731ee1cd0b2bd50f66aabac5b/gistfile1.txt"
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
    # Program 5 Tests
    print "## Program 5 ##"
    plain = "Burning 'em, if you ain't quick and nimble"
    key = "ICE"
    enc = xor(plain, key)
    expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2"
    print "Plain:    {}".format(plain)
    print "Key:      {}".format(key)
    print "XOR'd:    {}".format(stoh(enc))
    print "Expected: {}".format(expected)
