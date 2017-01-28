def dups(a):
	b=[] 
	for i in a:
        	if i not in b:
        		b.append(i)
	print b

dups([1,2,3,4,1,2])


