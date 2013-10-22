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
