
def hamming(a, b):
	bits = 0
	for i in range(len(a)):
		if i < len(b):
			bit = ord(a[i])^ord(b[i])
			while bit:				
				bits += bit&1
				bit>>=1
		else:
			bits += (len(a)-len(b))*8
			break
	if i < len(b):
		bits += (len(b)-len(a))*8
	return bits

if __name__ == "__main__":
	# Program 6 Test
	print "## Program 6 ##"
	str1 = "this is a test"
	str2 = "wokka wokka!!!"
	dist = hamming(str1, str2)
	print "str1: {}".format(str1)
	print "str2: {}".format(str2)
	print "dist: {}".format(dist)
