def rank(st, we, n):
	import string
	p = 0
	dic = {}
	st_split = st.split(',')
	if st == "":
		return "No participants"
	elif n > len(st_plit):
		return "Not enough participants"
	else:
		for name in st_split:
			add = 0
			ran = 0
			for i in name.lower():
				add += string.ascii_lowercase.index(i)
			ran = (add + len(name) + n) * we[p]
			p += 1
			dic[ran] = name
		sor = (list(reversed(sorted(dic.keys()))))
		return dic[(sor[n-1])]

print(rank("", [4, 2, 1, 4, 3, 1, 2], 6))
