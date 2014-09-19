def freequency(strr):
	freeq={}
	for ch in strr:
		freeq[ch]=freeq.get(ch,0)+1
	return freeq

