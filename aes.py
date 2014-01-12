from Crypto.Cipher import AES
from hexutils import *
from xor import xor
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

def cbc_encrypt(text, key, iv, block_size=16):
    cipher = AES.new(key, AES.MODE_ECB)
    enc = ''
    prev = iv
    for n in range(0, len(text), block_size):
        block = xor(text[n:n+block_size], prev)
        enc_block = cipher.encrypt(block)
        enc += enc_block
        prev = enc_block
    return enc

def cbc_decrypt(enc, key, iv, block_size=16):
    cipher = AES.new(key, AES.MODE_ECB)
    dec = ''
    prev = iv
    for n in range(0, len(enc), block_size):
        block = enc[n:n+block_size]
        dec_block = cipher.decrypt(block)
        dec += xor(dec_block, prev)
        prev = block
    return dec
