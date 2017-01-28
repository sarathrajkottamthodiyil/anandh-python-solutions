def lensort(a):
        #a =  a
	a.sort(key=lambda x: len(x))
        #print "welcome"
	return a
	

print lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
	[6, 4, 4, 1,7,4]
        [1,4,4,4, 6,7]
	

