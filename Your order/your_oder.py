def order(sentence):
	b = []
	c= {}
	d = []
	for i in sentence.split():
		for e in i:
			if e.isdecimal():
				c[e] = i
				b.append(e)
	for k in sorted(b):
		d.append(c[k])
			
	return ' '.join(d)
	
		
				
  
print(order(""))
