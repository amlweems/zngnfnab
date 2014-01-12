from xor import *
from hexutils import *
from hamming import *
from aes import *

def test1():
    print "## Program 1 ##"
    hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    base_str = htob(hex_str)
    new_hex_str = btoh(base_str)
    print "Hex:          {}".format(hex_str)
    print "Base64:       {}".format(base_str)
    print "Hex'd Base64: {}".format(new_hex_str)



def test2():
    print "## Program 2 ##"
    plain = htos("1c0111001f010100061a024b53535009181c")
    key = htos("686974207468652062756c6c277320657965")
    enc = xor(plain, key)
    print "Plain:     {}".format(stoh(plain))
    print "Key:       {}".format(stoh(key))
    print "Encrypted: {}".format(stoh(enc))

def test3():
    print "## Program 3 ##"
    enc = htos("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    key = crack(enc, key_size=1)
    plain = xor(enc, key)
    print "Encrypted: {}".format(stoh(enc))
    print "Key:       {}".format(stoh(key))
    print "Plain:     {}".format(plain)

def test4():
    print "## Program 4 ##"
    import requests
    url = "https://gist.github.com/tqbf/3132713/raw/40da378d42026a0731ee1cd0b2bd50f66aabac5b/gistfile1.txt"
    r = requests.get(url)
    lines = r.content.split("\n")
    best = ['','',total]
    for line in lines:
        if not line: continue
        line = htos(line)
        key = crack(line, key_size=1)
        score = fscore(xor(line, key))
        if score < best[2]:
            best[0] = line
            best[1] = key
            best[2] = score
    print "XOR'd: {}".format(stoh(best[0]))
    print "Plain: {}".format(xor(best[0],best[1]))

def test5():
    print "## Program 5 ##"
    plain = "Burning 'em, if you ain't quick and nimble"
    key = "ICE"
    enc = xor(plain, key)
    expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2"
    print "Plain:    {}".format(plain)
    print "Key:      {}".format(key)
    print "XOR'd:    {}".format(stoh(enc))
    print "Expected: {}".format(expected)

def test6():
    print "## Program 6 ##"
    str1 = "this is a test"
    str2 = "wokka wokka!!!"
    dist = hamming(str1, str2)
    print "str1: {}".format(str1)
    print "str2: {}".format(str2)
    print "dist: {}".format(dist)
    url = "https://gist.github.com/tqbf/3132752/raw/cecdb818e3ee4f5dda6f0847bfd90a83edb87e73/gistfile1.txt"
    r = requests.get(url)
    enc = btos(r.content)
    key = crack(enc)
    plain = xor(enc, key)
    print "XOR'd: {}".format(stoh(enc)[:80])
    print "Key:   {}".format(key)
    print "Plain: {}".format(plain[:80])

def test7():
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

def test8():
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

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test6()
    test7()
    test8()
