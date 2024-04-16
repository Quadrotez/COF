def telephone(n):
	b=len(n)==12
	c=n[:2]=='+7'
	k = 0

	for i in n[2:]:
		if i in '0123456789':
			k+=1
	a = k == 10
	print(b==True and c==True and a==True)