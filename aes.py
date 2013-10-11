from Crypto.Cipher import AES
from hexutils import *
import requests

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

if __name__ == "__main__":
	_test7()