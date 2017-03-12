def thirt(n):
	a = list(str(n))
	rem = [1, 10, 9, 12, 3, 4]
	remad = 0
	comp = []
	if len(a) > len(rem):
		b = len(a) - len(rem)
		z = a[b:]
		zipa = zip(a, rem)
		zipz = zip(z, rem)
		print(zipa)
		zipadd = zipa + zipz
		print(zipadd)
		while True:
			for i, j in zipadd:
				remad += (int(i)*int(j))
				if remad in comp:
					break
				else:
					comp.append(remad)
					zipadd = list(str(remad))
			return remad
		
print(thirt(1234567))
			
	
