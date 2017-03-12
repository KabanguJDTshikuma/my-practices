def kebabize(string):
	a = ''
	if string.isupper():
		return('-'.join(string).lower())
	else:
		b = list(string)
		for i in b:
			if i.isdecimal():
				a +=''
			elif not i.isupper():
				a +=i
			else:
				a += '-' + i
		if a.startswith('-'):
			b = a.split('-')
			b.remove('')
			return('-'.join(b).lower())
		else:
			return(a.lower())
		
		
print(kebabize('FelixNgoyi'))
			
