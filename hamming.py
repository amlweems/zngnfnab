
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
	if len(a) < len(b):
		bits += (len(b)-len(a))*8
	return bits
