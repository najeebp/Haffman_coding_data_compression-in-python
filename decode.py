def decode(tree,str):
	output=""
	for bit in str:
		if bit=='0' :p=p[0]
		else        :p=p[1]
		if type(p)==type(""):
			output+=p
			p=tree
	return output
			
