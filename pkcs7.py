
def encode(text, block_size):
    padding = block_size - len(text)%block_size
    return text + chr(padding)*padding

def decode(text):
    padding = ord(text[-1])
    if len(text) < padding:
        return text
    for i in range(2, padding+1):
        if text[-i] != chr(padding):
            return text
    return text[:-padding]
