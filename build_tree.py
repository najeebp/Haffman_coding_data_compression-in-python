def buildTree(tuples):
	while len(tuples)>1:
		leasttwo=tuples[0:2]
		remaining=tuples[2:]
		combFreq=leasttwo[0][0]+leasttwo[1][0]
		tuples=remaining+[(combFreq,leasttwo)]
		tuples.sort()
	return tuples[0
def trimTree(tree):
	p=tree[1]
	if type(p)==type("") : return p
	else: 	
		return (trimTree(p[0]),trimTree(p[1]))

