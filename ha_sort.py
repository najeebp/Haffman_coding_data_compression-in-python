def sortFreq(freeq):
	letters=freeq.keys()
	tuples=[]
	for th in letters:
		tuples.append((freeq[th],th))
	tuples.sort()
	return tuples
