from nltk.corpus import brown
from hexutils import *
from hamming import hamming
import requests
import sys

KEY_DEPTH     = 3
HAMMING_DEPTH = 10
MAX_KEY_SIZE  = 40

char_counts = [1 for i in range(256)]
for char in brown.raw():
    char_counts[ord(char)] += 1
total = float(sum(char_counts))

def xor(plain, key):
    return ''.join(chr(ord(plain[i])^ord(key[i%len(key)])) for i in range(len(plain)))

def fscore(text):
    length = float(len(text))
    summation = 0
    text_counts = [0 for i in range(256)]
    for letter in text:
        text_counts[ord(letter)] += 1
    for c in range(256):
        summation += ((text_counts[c]/length) / (char_counts[c]/total)) ** 2
    return summation

def _hammingcrack(enc):
    key_sizes = []
    for key_size in range(1, MAX_KEY_SIZE):
        dist = 0.0
        for i in range(HAMMING_DEPTH):
            block1 = enc[key_size*i:key_size*(i+1)]
            block2 = enc[key_size*(i+1):key_size*(i+2)]
            dist += hamming(block1, block2)
        dist /= key_size*HAMMING_DEPTH
        key_sizes.append([key_size, dist])
    key_sizes.sort(key=lambda x: x[1])
    keys = []
    for index in range(KEY_DEPTH):
        key_size = key_sizes[index][0]
        key = crack(enc, key_size)
        plain = xor(enc, key)
        keys.append([key, fscore(plain)])
    keys.sort(key=lambda x: x[1])
    return keys[0][0]

def crack(enc, key_size=-1):
    if key_size == -1: return _hammingcrack(enc)
    key = ''
    for i in range(key_size):
        block = enc[i::key_size]
        guesses = [0 for i in range(256)]
        for k in range(256):
            guesses[k] = fscore(xor(block, chr(k)))
        best = guesses.index(min(guesses))
        key += chr(best)
    return key
